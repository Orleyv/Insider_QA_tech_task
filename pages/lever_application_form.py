

class ApplicationForm:

    def __init__(self, driver):
        self.driver = driver


    def page_url(self):
        page_url = self.driver.current_url
        return page_url
