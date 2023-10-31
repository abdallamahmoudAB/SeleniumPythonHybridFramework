from datetime import datetime
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown")
class TestRegister:
    def test_register_with_mandatory_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("test")
        self.driver.find_element(By.NAME, "lastname").send_keys("user")
        self.driver.find_element(By.NAME, "email").send_keys(self.generate_email_with_timestamp())
        self.driver.find_element(By.NAME, "telephone").send_keys("987654321")
        self.driver.find_element(By.NAME, "password").send_keys("test321")
        self.driver.find_element(By.NAME, "confirm").send_keys("test321")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_heading_text = "Your Account Has Been Created!"
        assert self.driver.find_element(By.XPATH, "//div[@id='content']/h1").text.__eq__(expected_heading_text)

    def test_register_with_duplicate_email(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("test")
        self.driver.find_element(By.NAME, "lastname").send_keys("user")
        self.driver.find_element(By.NAME, "email").send_keys("dummyuser@dummy.com")
        self.driver.find_element(By.NAME, "telephone").send_keys("987654321")
        self.driver.find_element(By.NAME, "password").send_keys("test321")
        self.driver.find_element(By.NAME, "confirm").send_keys("test321")
        self.driver.find_element(By.NAME, "agree").click()
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_warning_msg = "Warning: E-Mail Address is already registered!"
        assert self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger')]").text.__eq__(expected_warning_msg)

    def test_register_without_entering_any_fields(self):
        self.driver.find_element(By.XPATH, "//span[text()='My Account']").click()
        self.driver.find_element(By.LINK_TEXT, "Register").click()
        self.driver.find_element(By.NAME, "firstname").send_keys("")
        self.driver.find_element(By.NAME, "lastname").send_keys("")
        self.driver.find_element(By.NAME, "email").send_keys("")
        self.driver.find_element(By.NAME, "telephone").send_keys("")
        self.driver.find_element(By.NAME, "password").send_keys("")
        self.driver.find_element(By.NAME, "confirm").send_keys("")
        self.driver.find_element(By.XPATH, "//input[@value='Continue']").click()
        expected_warning_msg = "Warning: You must agree to the Privacy Policy!"
        assert self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger')]").text.__eq__(expected_warning_msg)

    def generate_email_with_timestamp(self):
        timestamp = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        return "dummy"+timestamp+"@gmail.com"