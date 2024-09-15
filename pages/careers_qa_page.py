import time
from selenium.webdriver.common.by import By


class CareersQAPage:
    LINK = "https://useinsider.com/careers/quality-assurance/"
    SEE_ALL_LINK = (By.LINK_TEXT, "See all QA jobs")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        return self.driver.get(self.LINK)

    def click_see_all(self):
        link = self.driver.find_element(*self.SEE_ALL_LINK)
        link.click()
        time.sleep(20)