from playwright.sync_api import Page

class LoginPage:
    def __init__(self, page: Page):
        self.page = page
        self.username = page.locator("input[name='username']")
        self.password = page.locator("input[name='password']")
        self.login_btn = page.locator("button[type='submit']")

    def login(self, user: str, pwd: str):
        self.username.fill(user)
        self.password.fill(pwd)
        self.login_btn.click()
        # Wait for Admin module button to be visible
        self.page.locator("a:has-text('Admin')").wait_for(state="visible")
