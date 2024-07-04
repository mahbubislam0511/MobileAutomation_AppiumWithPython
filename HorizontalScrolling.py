from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.common.by import By
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

wait1 = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
viewsButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Views"]')))
viewsButton.click()

galleryButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Gallery"]')))
galleryButton.click()

photosButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="1. Photos"]')))
photosButton.click()

# Scroll with Android UiAutomator from left to right
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToEnd(5)')

# Scroll with Android UiAutomator from right to left
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollToBeginning(5)')

# Scroll with Android UiAutomator with scrollForward
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollForward(2)')

# Scroll with Android UiAutomator with scrollBackward
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsHorizontalList().scrollBackward(2)')