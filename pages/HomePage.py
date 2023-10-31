from selenium.webdriver.common.by import By

class HomePage:
    def __int__(self, driver):
        self.driver =driver

    search_box_field_name = "search"
    search_btn_xpath = "//button[contains(@class, 'btn-default')]"

    def enter_product_into_search_box_field(self, productName):
        self.driver.find_element(By.NAME, self.search_box_field_name).click()
        self.driver.find_element(By.NAME, self.search_box_field_name).clear()
        self.driver.find_element(By.NAME, self.search_box_field_name).send_keys(productName)


    def click_on_search_btn(self):
        self.driver.find_element(By.XPATH, self.search_btn_xpath).click()