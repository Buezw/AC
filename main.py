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

    page.goto('https://recreation.utoronto.ca/booking/c394b167-188b-4846-994c-61e752697cc4')
    second_day = "xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[10]/div[2]/div[2]/button[2]"
    third_day = 'xpath=xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[10]/div[2]/div[2]/button[2]'
    page.locator(second_day).click()
    lastest_time = 'xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div[2]/div[2]/div/button'
    court_two = 'xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[11]/div[2]/div/button[2]'
    page.locator(court_two).click()
    def timer(t):
        while 1:
            current_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
            print(current_time)
            if current_time == t:
                start_time = current_time
                page.locator(third_day).click()
                page.locator(lastest_time).click()
                after_time = datetime.now().strftime("%H:%M:%S.%f")[:-3]
                break
        print(start_time,after_time)

    timer("11:59:59.900")
    time.sleep(1000)