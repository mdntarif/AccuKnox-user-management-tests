from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_btn = page.locator("a:has-text('Admin')")
        self.add_btn = page.locator("button:has-text('Add')")
        self.username_field = page.locator("input[name='username']")
        self.employee_name_field = page.locator("input[placeholder='Type for hints...']")
        self.password_field = page.locator("input[name='password']")
        self.confirm_password_field = page.locator("input[name='confirmPassword']")
        self.role_select = page.locator("select[name='userRole']")
        self.status_select = page.locator("select[name='status']")
        self.save_btn = page.locator("button:has-text('Save')")
        self.search_username = page.locator("input[placeholder='Username']")
        self.search_btn = page.locator("button:has-text('Search')")
        self.edit_btn = lambda username: page.locator(f"text={username} >> .. >> button:has-text('Edit')")
        self.success_message = page.locator("div.orangehrm-toast")
        self.no_record_msg = page.locator("span:has-text('No Records Found')")

    def navigate_admin_module(self):
        self.admin_btn.click()
        self.admin_btn.wait_for(state="visible")

    def add_user(self, username, employee_name, role="ESS", status="Enabled", password=None, confirm_password=None):
        self.add_btn.click()
        self.username_field.wait_for(state="visible")
        self.username_field.fill(username)
        self.employee_name_field.fill(employee_name)
        self.role_select.select_option(role)
        self.status_select.select_option(status)
        if password:
            self.password_field.fill(password)
            self.confirm_password_field.fill(confirm_password)
        self.save_btn.click()
        self.success_message.wait_for(state="visible")

    def add_user_without_details(self):
        self.add_btn.click()
        self.save_btn.click()
        # Wait for required field error messages
        self.page.locator("span.oxd-input-field-error-message").wait_for(state="visible")

    def search_user(self, username):
        self.search_username.fill(username)
        self.search_btn.click()
        self.page.wait_for_timeout(1000)  # wait for search results to load

    def edit_user_role(self, username, new_role):
        self.edit_btn(username).click()
        self.role_select.select_option(new_role)
        self.save_btn.click()
        self.success_message.wait_for(state="visible")
