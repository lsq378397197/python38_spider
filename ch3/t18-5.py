import asyncio
from pyppeteer import launch

width, height = 1920, 1080


# 获取和切换选项卡
async def main():
    # 很多时候你在每次启动 Selenium 或 Pyppeteer 的时候总是一个全新的浏览器，
    # userDataDir 那这究其原因就是没有设置用户目录，如果设置了它，每次打开就不再是一个全新的浏览器了，它可以恢复之前的历史记录，也可以恢复很多网站的登录信息
    browser = await launch(headless=False, userDataDir='./userdata',
                           args=['--disable-infobars', f'--window-size={width},{height}'])
    # 开启无痕模式
    context = await browser.createIncognitoBrowserContext()
    # Create a new page in a pristine context.
    page = await context.newPage()

    await page.setViewport({'width': width, 'height': height})
    await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver",{get:()=>undefined})')
    await page.goto('https://www.taobao.com')
    await asyncio.sleep(100)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
