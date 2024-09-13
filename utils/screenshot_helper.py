import os
from datetime import datetime


def capture_screenshot(driver, test_name, browser):
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    screenshot_name = f"{test_name}_{browser}_{timestamp}.png"
    screenshots_dir = os.path.join(os.getcwd(), "screenshots")

    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    driver.save_screenshot(os.path.join(screenshots_dir, screenshot_name))
