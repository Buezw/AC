from playwright.sync_api import sync_playwright
import time
import re
from datetime import datetime

# 获取当前时间并格式化为小时:分钟:秒

session_file = r"session.json"


AC_Field_two = 'xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[11]/div[2]/div/button[1]'
AC_Field_three = 'xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[11]/div[2]/div/button[2]'
second_day = 'xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[10]/div[2]/div[2]/button[2]'
thrid_day = 'xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[10]/div[2]/div[2]/button[3]'
time_table_xpath = "xpath=/html/body/div[1]/div/div[3]/div[1]/div[2]/div[12]/div[2]"


def process_time_slots(input_str):
    import re
    lines = input_str.strip().split('\n')
    # 使用起始和结束锚点，确保完全匹配
    time_slot_pattern = re.compile(r'^\d+ - \d+(?::\d+)? [AP]M$')
    total_slots = 0
    book_now_info = []
    for i in range(len(lines)):
        line = lines[i].strip()
        if time_slot_pattern.fullmatch(line):
            total_slots += 1
            time_slot = line
            # 找到前一个非空行作为可用性
            j = i - 1
            while j >= 0 and lines[j].strip() == '':
                j -= 1
            availability = lines[j].strip() if j >= 0 else ''
            if 'BOOK NOW' in availability.upper():
                position = total_slots
                book_now_info.append({'time_slot': time_slot, 'position': position})
    return total_slots, book_now_info

with sync_playwright() as p:
    # 启动浏览器并创建一个新的上下文

    browser = p.chromium.launch(headless=True)
    context = browser.new_context()
    context = browser.new_context(storage_state=session_file)
    page = context.new_page()
    page.goto('https://recreation.utoronto.ca/booking/c394b167-188b-4846-994c-61e752697cc4')
    #page.goto('https://recreation.utoronto.ca/booking/9720eff9-0499-4a71-b126-115879e67a16')
    page.locator('xpath=/html/body/div[1]/div/div[3]/div[5]/div[1]/div/div/div/div[2]/div[1]/div[6]/div/button').click()
    page.locator(AC_Field_two).click()
    day_one_two = page.locator(time_table_xpath).inner_text()
    page.locator(AC_Field_three).click()
    day_one_three = page.locator(time_table_xpath).inner_text()

    page.locator(second_day).click()
    page.locator(AC_Field_two).click()
    day_two_two = page.locator(time_table_xpath).inner_text()
    page.locator(AC_Field_three).click()
    day_two_three = page.locator(time_table_xpath).inner_text()

    page.locator(thrid_day).click()
    page.locator(AC_Field_two).click()
    day_three_two = page.locator(time_table_xpath).inner_text()
    page.locator(AC_Field_three).click()
    day_three_three = page.locator(time_table_xpath).inner_text()


    print(process_time_slots(day_one_two))
    print(process_time_slots(day_one_three))
    print(process_time_slots(day_two_two))
    print(process_time_slots(day_two_three))
    print(process_time_slots(day_three_two))
    print(process_time_slots(day_three_three))
