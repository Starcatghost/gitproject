from playwright.sync_api import sync_playwright

with sync_playwright()  as p:
    browser = p.chromium.launch(headless=False, channel = 'chrome')

    page = browser.new_page()

    page.goto('https://aphacademy.ir/')

    # page.goto('https://divar.ir')
    # # page.locator('text=اهواز').click()
    # # page.get_by_role
    # page.get_by_role("link", name="اهواز").click()
    # page.get_by_role("button", name=" ورود به حساب کاربری").click()
    # page.get_by_placeholder("۰۹۱۲ ۱۲۳ ۴۵۶۷").fill('09031681570')
    # page.get_by_role("button", name="بعدی").click()
    page.get_by_role("link", name=" ورود").click()
    page.get_by_role("link", name=" ورود").fill("09031681570")

    

    page.pause()

