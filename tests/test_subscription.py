import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pages.subscription_page import SubscriptionPage

def test_subscription_success(driver):
    subscription_page = SubscriptionPage(driver)
    subscription_page.subscribe("premium", "4111111111111111", "12/26", "123")
    assert "Subscription successful" in subscription_page.get_success_message()
