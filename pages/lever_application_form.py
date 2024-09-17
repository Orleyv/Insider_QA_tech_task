from selenium.webdriver.support.wait import WebDriverWait


class ApplicationForm:

    def __init__(self, driver):
        self.driver = driver


    def page_url(self):
        WebDriverWait(self.driver, 40).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )
        page_url = self.driver.current_url
        return page_url
