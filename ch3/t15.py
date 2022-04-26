import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import logging
from urllib.parse import urljoin
from os import makedirs
from os.path import exists
import json
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')
INDEX_URL = 'https://dynamic2.scrape.center/page/{page}'
TIME_OUT = 10
TOTAL_PAGE = 10
# options=webdriver.ChromeOptions()
# options.add_argument('--headless')
# browser = webdriver.Chrome(options=options)
browser = webdriver.Chrome()
wait = WebDriverWait(browser, TIME_OUT)
RESULT_DIR = 'results'
exists(RESULT_DIR) or makedirs(RESULT_DIR)
DETAIL_URL = 'https://dynamic1.scrape.cuiqingcai.com/api/movie/{id}'


def scrape_page(url, condition, locator):
    """
    异步加载页面，知道想要的元素被加载出来
    """
    logging.info('scraping %s', url)
    try:
        browser.get(url)
        wait.until(condition(locator))
    except TimeoutException:
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    """
    可以等待 #index .item下的元素已经加载完毕
    """
    url = INDEX_URL.format(page=page)
    scrape_page(url, condition=EC.visibility_of_all_elements_located, locator=(By.CSS_SELECTOR, '#index .item'))


def parse_index():
    """
    :return: 详情页url列表
    """
    elements = browser.find_elements(By.CSS_SELECTOR, '#index .item .name')
    for element in elements:
        href = element.get_attribute('href')
        yield urljoin(INDEX_URL, href)


# def scrape_api(url):
#     logging.info('scraping %s...', url)
#     try:
#         response = requests.get(url)
#         if response.status_code == 200:
#             return response.json()
#         logging.error('get invalid status code %s while scraping %s', response.status_code, url)
#     except requests.RequestException:
#         logging.error('error occurred while scraping %s', url, exc_info=True)

def scrape_detail(url):
    scrape_page(url, condition=EC.visibility_of_element_located,
                locator=(By.TAG_NAME, 'h2'))


def parse_detail():
    url = browser.current_url
    name = browser.find_element(By.TAG_NAME, 'h2').text
    categories = [element.text for element in browser.find_elements(By.CSS_SELECTOR, '.categories button span')]
    cover = browser.find_element(By.CSS_SELECTOR, '.cover').get_attribute('src')
    score = browser.find_element(By.CLASS_NAME, 'score').text
    drama = browser.find_element(By.CSS_SELECTOR, '.drama p').text
    return {
        'url': url,
        'name': name,
        'categories': categories,
        'cover': cover,
        'score': score,
        'drama': drama
    }


def save_data(data):
    """
    保存数据
    :param data:
    :return:
    """
    name = data.get('name')
    data_path = f'{RESULT_DIR}/{name}.json'
    json.dump(data, open(data_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)


def main():
    try:
        for page in range(1, TOTAL_PAGE + 1):
            scrape_index(page)
            detail_urls = parse_index()
            # logging.info('detail urls %s', list(detail_urls))
            for detail_url in detail_urls:
                logging.info("get detail url %s", detail_url)
                scrape_detail(detail_url)
                detail = parse_detail()
                logging.info("detail data %s", detail)
                save_data(detail)
    finally:
        browser.close()


if __name__ == '__main__':
    main()
