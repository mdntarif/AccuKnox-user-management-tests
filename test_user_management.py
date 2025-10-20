import pytest
from playwright.sync_api import sync_playwright
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

@pytest.fixture(scope="session")
def setup():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        yield page
        browser.close()

def test_navigate_admin_module(setup):
    page = setup
    login = LoginPage(page)
    login.login("Admin", "admin123")
    admin = AdminPage(page)
    admin.navigate_admin_module()
    assert page.locator("h6:has-text('Admin')").is_visible()

def test_add_user_without_details(setup):
    page = setup
    admin = AdminPage(page)
    admin.add_user_without_details()
    assert page.locator("span.oxd-input-field-error-message").is_visible()

def test_add_new_user(setup):
    page = setup
    admin = AdminPage(page)
    admin.add_user(
        username="testuser1",
        employee_name="Jobin Mathew Sam",
        role="ESS",
        status="Enabled",
        password="Test@123",
        confirm_password="Test@123"
    )
    assert admin.success_message.is_visible()

def test_search_new_user(setup):
    page = setup
    admin = AdminPage(page)
    admin.search_user("testuser1")
    assert page.locator("div:has-text('testuser1')").is_visible()

def test_search_invalid_user(setup):
    page = setup
    admin = AdminPage(page)
    admin.search_user("invaliduser")
    assert admin.no_record_msg.is_visible()

def test_edit_user_role(setup):
    page = setup
    admin = AdminPage(page)
    admin.edit_user_role("testuser1", new_role="Admin")
    assert admin.success_message.is_visible()