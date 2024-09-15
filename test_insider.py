import pytest
from utils.driver_setup import setup_driver
from utils.screenshot_helper import capture_screenshot
from pages.home_page import HomePage
from pages.careers_page import CareersPage
from pages.careers_qa_page import CareersQAPage
from pages.job_listings_page import JobListingsPage
from pages.lever_application_form import ApplicationForm


@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_insider_careers(browser):
    driver = setup_driver(browser)

    try:
        # Step 1: Visit https://useinsider.com/ and check Insider home page is opened or not
        home_page = HomePage(driver)
        home_page.open()
        title = home_page.page_title()
        assert title == "#1 Leader in Individualized, Cross-Channel CX — Insider", f"Page title is: {title}"

        # Step 2: Select “Company” menu in navigation bar, select “Careers” and check Career
        # page, its Locations, Teams and Life at Insider blocks are opened or not
        home_page.go_to_company()
        home_page.go_to_careers()
        careers_page = CareersPage(driver)
        assert careers_page.is_section_locations_displayed(), "Locations section is not displayed"
        assert careers_page.is_section_teams_displayed(), "Teams section is not displayed"
        assert careers_page.is_section_life_displayed(), "Life at Insider section is not displayed"

        # Step 3: Go to https://useinsider.com/careers/quality-assurance/, click “See all QA
        # jobs”, filter jobs by Location - Istanbul, Turkey and department - Quality
        # Assurance, check presence of jobs list
        careers_qa_page = CareersQAPage(driver)
        careers_qa_page.open()
        careers_qa_page.click_see_all()
        job_listing_page = JobListingsPage(driver)
        job_listing_page.apply_filters()
        assert job_listing_page.check_job_list(), "Jobs list is missing"

        # Step 4: Check that all jobs’ Position contains “Quality Assurance”, Department
        # contains “Quality Assurance”, Location contains “Istanbul, Turkey”
        assert job_listing_page.check_list_items(location="Istanbul, Turkey", department="Quality Assurance"), "There is incorrect location or department"

        # Step 5: Click “View Role” button and check that this action redirects us to Lever
        # Application form page
        job_listing_page.click_view_role()
        application_form = ApplicationForm()
        assert "https://jobs.lever.co/useinsider/" in application_form.page_url(), "This is not the https://jobs.lever.co/useinsider/ page"

    except Exception as e:
        capture_screenshot(driver, "test_insider_careers", browser)
        raise e

    finally:
        driver.quit()
