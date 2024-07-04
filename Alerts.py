from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.hmh.api',
    'appActivity': '.ApiDemos',
    'language': 'en',
    'locale': 'US'
}

url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(25)

if driver.find_element(AppiumBy.XPATH, value='//android.widget.Button[@text="Continue"]').is_displayed():
    driver.find_element(AppiumBy.XPATH, value='//android.widget.Button[@text="Continue"]').click()

wait = WebDriverWait(driver, 15)
okButton = wait.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')))
okButton.click()

wait1 = WebDriverWait(driver, 15, poll_frequency=1,
                      ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
appButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="App"]')))
appButton.click()

alertButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Alert Dialogs"]')))
alertButton.click()

first_AlertButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="OK Cancel dialog with a message"]')))
first_AlertButton.click()

# Two-way Alert Solution in Appium
okButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')))
okButton.click()

# driver.switch_to.alert.accept()
# driver.switch_to.alert.dismiss()

