from playwright.sync_api import sync_playwright
import time
import re
import random
from datetime import datetime

# 获取当前时间并格式化为小时:分钟:秒

session_file = r"session.json"


with sync_playwright() as p:
    # 启动浏览器并创建一个新的上下文

    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    context = browser.new_context(storage_state=session_file)


    page = context.new_page()

    page.goto('https://recreation.utoronto.ca/booking/9720eff9-0499-4a71-b126-115879e67a16')
    thrid_day = "xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[10]/div[2]/div[2]/button[3]"
    page.locator(thrid_day).click()
    lastest_time = 'xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div[2]/div[15]/div/button'

    def timer(t):
        while 1:
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(current_time)
            if current_time == t:
                start_time = current_time
                page.locator(lastest_time).click()
                after_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                break
        print(start_time,after_time)

    timer("21:48:35.660")
    time.sleep(1000)