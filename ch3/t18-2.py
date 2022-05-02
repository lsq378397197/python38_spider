import asyncio
from pyppeteer import launch

width, height = 1920, 1080


async def main():
    # browser = await launch(headless=False)
    # await asyncio.sleep(100)
    # 默认开启无头模式，即没有界面，devtools为开始调试模式，  # "Chrome 正受到自动测试软件的控制，关闭这个提示args=['--disable-infobars'],
    browser = await launch(devtools=True, userDataDir='./userdata',args=['--disable-infobars', f'--window-size={width},{height}'])

    page = await browser.newPage()
    await page.setViewport({'width': width, 'height': height})
    # await page.goto('https://dynamic2.scrape.center/')

    # 当遇到检测webDriver的网站时
    await page.evaluateOnNewDocument('Object.defineProperty(navigator,"webdriver",{get:()=>undefined})')
    await page.goto('https://antispider1.scrape.center/')
    await asyncio.sleep(100)
    # 当遇到检测webDriver的网站时

    await page.waitForSelector('.item .name')
    await asyncio.sleep(2)
    await page.screenshot(path='example.png')
    # 执行javascript
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor:window.devicePixelRatio
        }
    }''')
    print(dimensions)
    await browser.close()


asyncio.get_event_loop().run_until_complete(main())
