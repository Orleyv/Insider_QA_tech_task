from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


class HomePage:
    LINK = "https://useinsider.com/"
    COMPANY_LINK = (By.LINK_TEXT, "Company")
    CAREERS_LINK = (By.LINK_TEXT, "Careers")

    def __init__(self, driver):
        self.driver = driver
        self.company_link = self.COMPANY_LINK
        self.careers_link = self.CAREERS_LINK

    def open(self):
        return self.driver.get(self.LINK)

    def page_title(self):
        page_name = self.driver.title
        return page_name

    def click_dropdown(self):
        # Wait until the dropdown button is clickable, then click
        select = Select(WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(By.ID, "navbarDropdownMenuLink")))
        select.select_by_visible_text("career")
        # WebDriverWait(self.driver, 10).until(
        #     EC.invisibility_of_element(self.dropdown_button)
        # ).click()

    def go_to_careers(self):

        # Wait for the Careers link to be visible and click it
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.careers_link)
        ).click()

    def go_to_company(self):

        # Wait for the Careers link to be visible and click it
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.company_link)
        ).click()
