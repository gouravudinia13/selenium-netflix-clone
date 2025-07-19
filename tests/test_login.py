import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


from pages.login_page import LoginPage

def test_valid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("test@netflix.com", "test123")

    # Handle the alert
    try:
        alert = driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # Click OK on alert
        print("Alert text:", alert_text)
    except NoAlertPresentException:
        print("No alert present")
    
    assert "dashboard" in driver.current_url or login_page.driver.find_element("id", "logoutBtn").is_displayed()

def test_invalid_login(driver):
    login_page = LoginPage(driver)
    login_page.login("invalid@netflix.com", "wrongpass")
    assert "Invalid credentials" in login_page.get_error_msg()

def test_forgot_password(driver):
    login_page = LoginPage(driver)
    msg = login_page.reset_password("forgot@netflix.com")
    assert "Reset link sent" in msg
