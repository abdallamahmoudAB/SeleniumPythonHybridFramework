import pytest
from selenium.webdriver.common.by import By

from pages.HomePage import HomePage


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_for_valid_product(self):
        homepage = HomePage(self.driver)
        homepage.enter_product_into_search_box_field("HP")
        homepage.click_on_search_btn()
        # self.driver.find_element(By.NAME, "search").send_keys("HP")
        # self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        assert self.driver.find_element(By.LINK_TEXT, "HP LP3065").is_displayed()

    def test_search_for_invalid_product(self):
        homepage = HomePage(self.driver)
        homepage.enter_product_into_search_box_field("HONA")
        homepage.click_on_search_btn()
        # self.driver.find_element(By.NAME, "search").send_keys("HONA")
        # self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)

    def test_search_without_product(self):
        homepage = HomePage(self.driver)
        homepage.enter_product_into_search_box_field("")
        homepage.click_on_search_btn()
        # self.driver.find_element(By.NAME, "search").send_keys()
        # self.driver.find_element(By.XPATH, "//button[contains(@class, 'btn-default')]").click()
        expected_text = "There is no product that matches the search criteria."
        assert self.driver.find_element(By.XPATH, "//input[@id='button-search']/following-sibling::p").text.__eq__(expected_text)
