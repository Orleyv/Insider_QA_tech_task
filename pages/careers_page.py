from selenium.webdriver.common.by import By


class CareersPage:
    def __init__(self, driver):
        self.driver = driver
        self.locations_section = (By.CSS_SELECTOR, "section.elementor-section:nth-child(5)")
        self.teams_section = (By.CSS_SELECTOR, "div.elementor-section:nth-child(4)")
        self.life_section = (By.CSS_SELECTOR, "section.elementor-section:nth-child(6)")

    def is_section_teams_displayed(self):
        return self.driver.find_element(*self.teams_section).is_displayed()

    def is_section_locations_displayed(self):
        return self.driver.find_element(*self.locations_section).is_displayed()

    def is_section_life_displayed(self):
        return self.driver.find_element(*self.life_section).is_displayed()
