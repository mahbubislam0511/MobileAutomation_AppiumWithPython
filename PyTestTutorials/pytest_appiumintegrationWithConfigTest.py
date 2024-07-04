import allure
import pytest

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException

from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("adding_screenshot_Fail")
def test_demo(appium_driver):
    driver = appium_driver
    if driver.find_element(AppiumBy.XPATH, value='//android.widget.Button[@text="Continue"]').is_displayed():
        driver.find_element(AppiumBy.XPATH, value='//android.widget.Button[@text="Continue"]').click()

    wait = WebDriverWait(driver, 15)
    okButton = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')))
    okButton.click()

    wait1 = WebDriverWait(driver, 15, poll_frequency=1,
                          ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
    appButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="App"]')))
    appButton.click()

    alertButton = wait1.until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Alert Dialogs"]')))
    alertButton.click()

    first_AlertButton = wait1.until(EC.presence_of_element_located(
        (AppiumBy.XPATH, '//android.widget.Button[@text="OK Cancel dialog with a message"]')))
    first_AlertButton.click()

    # Two-way Alert Solution in Appium
    okButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')))
    okButton.click()

    allure.attach(driver.get_screenshot_as_png(), name="alert message2", attachment_type=AttachmentType.PNG)
