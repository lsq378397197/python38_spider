import requests
import logging
import re
import pymongo
from pyquery import PyQuery as pq
from urllib.parse import urljoin
import multiprocessing

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s:%(message)s')
BASE_URL = 'https://static1.scrape.center'
TOTAL_PAGE = 10
MONGO_CONNECTION_STRING = 'mongodb://localhost:27017'
MONGO_DB_NAME = 'movies'
MONGO_COLLECTION_NAME = 'movies'

client = pymongo.MongoClient(MONGO_CONNECTION_STRING)
db = client['movies']
collection = db['movies']


def scrape_page(url):
    logging.info('scraping %s...', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        logging.error('get invalid status code %s,while scraping %s', response.status_code, url)
    except requests.RequestException:
        # 这时我们将 logging 的 error 方法的 exc_info 参数设置为 True 则可以打印出 Traceback 错误堆栈信息
        logging.error('error occurred while scraping %s', url, exc_info=True)


def scrape_index(page):
    # f-string，亦称为格式化字符串常量（formatted string literals）
    # https://blog.csdn.net/sunxb10/article/details/81036693
    index_url = f'{BASE_URL}/page/{page}'
    return scrape_page(index_url)


def parse_index(html):
    doc = pq(html)
    links = doc('.el-card .name')
    for link in links.items():
        href = link.attr('href')
        detail_url = urljoin(BASE_URL, href)
        logging.info("getting url %s", detail_url)
        # https://www.runoob.com/w3cnote/python-yield-used-analysis.html
        yield detail_url


def scrape_detail(url):
    return scrape_page(url)


def parse_detail(html):
    """
    解析详情页
    """
    doc = pq(html)
    cover = doc('img.cover').attr('src')
    name = doc('a > h2').text()
    categories = [item.text() for item in doc('.categories button span').items()]
    published_at = doc('.info:contains(上映)').text()
    # published_at=doc('div.info > span').text()
    # python的续行符号，反斜杠，后面直接换行
    published_at = re.search('(\d{4}-\d{2}-\d{2})', published_at).group(1) \
        if published_at and re.search('(\d{4}-\d{2}-\d{2})', published_at) else None
    drama = doc('.drama p').text()
    # score是p的一个属性
    score = doc('p.score').text()
    score = float(score) if score else None
    return {
        "cover": cover,
        "name": name,
        "categories": categories,
        "published_at": published_at,
        "drama": drama,
        "score": score
    }


def save_data(data):
    collection.update_one({'name': data.get('name')}, {'$set': data}, upsert=True)


def main(page):
    index_html = scrape_index(page)
    detail_urls = parse_index(index_html)
    # logging.info('detail urls %s', list(detail_urls))
    for detail_url in detail_urls:
        detail_html = scrape_detail(detail_url)
        detail = parse_detail(detail_html)
        logging.info('getting detail %s', detail)
        logging.info('saving data to mongodb')
        save_data(detail)
        logging.info('data saved successfully')


if __name__ == '__main__':
    pool = multiprocessing.Pool()
    pages = range(1, TOTAL_PAGE + 1)
    pool.map(main, pages)
    pool.close()
    pool.join()
