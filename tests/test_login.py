from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestLogin:
    def test_login_with_valid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys("dummyuser@dummy.com")
        self.driver.find_element(By.ID, "input-password").send_keys("test123")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        assert self.driver.find_element(By.LINK_TEXT, "Edit your account information").is_displayed()




    def test_login_with_invalid_credentials(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Login").click()
        self.driver.find_element(By.ID, "input-email").send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.ID, "input-password").send_keys("test123")
        self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
        expected_msg = "Warning: No match for E-Mail Address and/or Password."
        assert self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert alert-danger alert-dismissible')]").text.__contains__(expected_msg)



    def generate_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "dummy"+timestamp+"@gmail.com"