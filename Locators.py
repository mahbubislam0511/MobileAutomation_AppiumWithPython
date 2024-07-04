import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554'
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)

youTube = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='YouTube')
youTube.click()

wait = WebDriverWait(driver, 15)
searchButton = wait.until(EC.visibility_of_element_located((By.XPATH, '//android.widget.ImageView[@content-desc="Search"]')))
# searchButton = wait.until(EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.ImageView[@content-desc="Search"]')))
# searchButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Search')
searchButton.click()

searchTextButton = driver.find_element(by=AppiumBy.ID, value='com.google.android.youtube:id/search_edit_text')
searchTextButton.send_keys("Mahbub")
driver.press_keycode(66)
