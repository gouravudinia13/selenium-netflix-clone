from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.email_input = (By.ID, "email")
        self.password_input = (By.ID, "password")
        self.login_btn = (By.ID, "loginBtn")
        self.logout_btn = (By.ID, "logoutBtn")
        self.error_msg = (By.ID, "errorMsg")
        self.forgot_link = (By.ID, "forgotLink")
        self.reset_email = (By.ID, "resetEmail")
        self.reset_submit = (By.ID, "resetSubmit")
        self.reset_success = (By.ID, "resetSuccess")

    def login(self, email, password):
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_btn).click()

    def logout(self):
        self.driver.find_element(*self.logout_btn).click()

    def get_error_msg(self):
        return self.driver.find_element(*self.error_msg).text

    def reset_password(self, email):
        self.driver.find_element(*self.forgot_link).click()
        self.driver.find_element(*self.reset_email).send_keys(email)
        self.driver.find_element(*self.reset_submit).click()
        return self.driver.find_element(*self.reset_success).text
