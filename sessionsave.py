from playwright.sync_api import sync_playwright


session_file = r"session.json"

def save_session():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()

        # 打开页面并登录（此处替换为实际的登录页面 URL）
        page = context.new_page()
        page.goto("https://recreation.utoronto.ca/booking/9720eff9-0499-4a71-b126-115879e67a16")
        page.locator('xpath=/html/body/div[1]/div/div[3]/div[5]/div[1]/div/div/div/div[2]/div[1]/div[6]/div/button').click()
        page.locator('xpath=/html/body/div/main/div[1]/form/div[1]/input').fill("huan4194")
        page.locator('xpath=/html/body/div/main/div[1]/form/div[2]/input').fill("Jeffrey@536")
        page.locator('xpath=/html/body/div/main/div[1]/form/button').click()
        input("123")
        # 等待登录完成，确保页面已加载

        # 保存会话状态到文件
        context.storage_state(path=session_file)
        
        browser.close()

save_session()