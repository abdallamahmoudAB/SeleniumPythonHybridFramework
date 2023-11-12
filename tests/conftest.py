import pytest
from selenium import webdriver
from utilis import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    # browser = ReadConfigurations.read_configuration("basic info","browser")
    driver = webdriver.Chrome()

    # if browser.__eq__("chrome"):
    #     driver = webdriver.Chrome()
    # elif browser.__eq__("firefox"):
    #     driver = webdriver.Firefox()
    # elif browser.__eq__("edge"):
    #     driver = webdriver.Edge()
    # else:
    #     print("please provide a valid browser name from this list chrome/firefox.edge")

    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    # driver.get(ReadConfigurations.read_configuration("basic info","url"))
    request.cls.driver = driver
    yield

    driver.quit()