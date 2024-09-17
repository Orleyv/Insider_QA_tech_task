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
    ALL_LOADED = (By.XPATH, "//*[@id='select2-filter-by-department-container' and contains(text(),'Quality Assurance')]")
    ELEMENT_TO_HOVER_OVER = (By.XPATH, "/html/body/section[3]/div/div/div[2]/div")


    def __init__(self, driver):
        self.driver = driver


    def apply_filters1(self):
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

    def apply_filters(self):

        wait = WebDriverWait(self.driver, 30)

        while len(self.driver.find_elements(*self.ALL_LOADED)) < 1:
            time.sleep(5)

        location_dropdown = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.select2-selection--single')))
        location_dropdown.click()

        # Select a specific location (e.g., Istanbul) from the dropdown
        location_option = wait.until(
            EC.element_to_be_clickable((By.XPATH, "//li[contains(text(),'Istanbul, Turkey')]")))
        location_option.click()
        self.driver.implicitly_wait(10)



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
        while not element.is_displayed():
            self.driver.execute_script("window.scrollBy(0, 500);")  # Scroll down
            time.sleep(1)
            try:
                element_to_hover_over = self.driver.find_element(*self.ELEMENT_TO_HOVER_OVER)
                action = ActionChains(self.driver)
                action.move_to_element(element_to_hover_over).perform()
            except:
                pass

        element.click()
        time.sleep(5)

    def check_new_tab(self):

        # Get a list of all open window handles
        windows = self.driver.window_handles

        # Switch to the new window (the last one in the list)
        self.driver.switch_to.window(windows[-1])

