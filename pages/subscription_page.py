from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class SubscriptionPage:
    def __init__(self, driver):
        self.driver = driver
        self.plan_dropdown = (By.ID, "planSelect")
        self.card_input = (By.ID, "cardNumber")
        self.expiry_input = (By.ID, "expiry")
        self.cvv_input = (By.ID, "cvv")
        self.pay_btn = (By.ID, "payBtn")
        self.success_msg = (By.ID, "successMsg")

    def subscribe(self, plan, card, expiry, cvv):
        Select(self.driver.find_element(*self.plan_dropdown)).select_by_value(plan)
        self.driver.find_element(*self.card_input).send_keys(card)
        self.driver.find_element(*self.expiry_input).send_keys(expiry)
        self.driver.find_element(*self.cvv_input).send_keys(cvv)
        self.driver.find_element(*self.pay_btn).click()

    def get_success_message(self):
        return self.driver.find_element(*self.success_msg).text