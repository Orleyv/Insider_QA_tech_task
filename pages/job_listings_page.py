import time
from selenium.common import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class JobListingsPage:
    LINK = "https://useinsider.com/careers/open-positions/?department=qualityassurance"
    LOCATION_FILTER = (By.ID, "select2-filter-by-location-container")
    LOCATION = (By.CSS_SELECTOR, "#select2-filter-by-location-result-mlw1-Istanbul\,\ Turkey")
    DEPARTMENT_FILTER = (By.ID, "select2-filter-by-department-container")
    DEPARTMENT = (By.CSS_SELECTOR, "#select2-filter-by-department-result-y0lc-Quality\ Assurance")
    EMPTY_JOBS_LIST= (By.CLASS_NAME, "no-job-result bg-light text-secondary w-100 text-center py-3")
    JOB_LIST = (By.ID, "jobs-list")
    LIST_ITEM = (By.CLASS_NAME, "position-list-item")
    ITEM_LOCATION = (By.CLASS_NAME, "position-location")
    ITEM_DEPARTMENT = (By.CLASS_NAME, "position-department")
    VIEW_ROLE = (By.CSS_SELECTOR, "div.position-list-item:nth-child(1) > div:nth-child(1) > a:nth-child(4)")


    def __init__(self, driver):
        self.driver = driver


    def apply_filters(self):
        WebDriverWait(self.driver, 40).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.LOCATION_FILTER)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.LOCATION)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DEPARTMENT_FILTER)
        ).click()

        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.DEPARTMENT)
        ).click()


    def check_job_list(self):
        try:
            self.driver.find_element(*self.JOB_LIST)
        except NoSuchElementException:
            return False
        if len(self.driver.find_elements(*self.EMPTY_JOBS_LIST)) == 0:
            return True
        else:
            return False

    def check_list_items(self, location, department):
        WebDriverWait(self.driver, 40).until(
            lambda driver: driver.execute_script("return document.readyState") == "complete"
        )

        items = self.driver.find_elements(*self.LIST_ITEM)
        for item in items:
            item_location = item.find_element(*self.ITEM_LOCATION)
            item_department = item.find_element(*self.ITEM_DEPARTMENT)
            if location not in item_location.text or department not in item_department.text:
                return False
        return True


    def click_view_role(self):

        element = self.driver.find_element(*self.VIEW_ROLE)

        # Scroll to the element using JavaScript
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        time.sleep(2)

        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

        element.click()
