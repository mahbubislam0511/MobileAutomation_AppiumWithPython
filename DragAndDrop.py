from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotVisibleException
from selenium.common.exceptions import NoSuchElementException

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.mobeta.android.demodslv',
    'appActivity': '.Launcher',
    'language': 'en',
    'locale': 'US'
}

url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)

wait1 = WebDriverWait(driver, 15, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

continueButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="Continue"]')))
continueButton.click()

okButton = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.Button[@text="OK"]')))
okButton.click()

basicUsagesBackground = wait1.until(EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Basic usage playground"]')))
basicUsagesBackground.click()

elementList = driver.find_elements(AppiumBy.XPATH, '//android.widget.ImageView[@resource-id="com.mobeta.android.demodslv:id/drag_handle"]')
print(len(elementList))

deviceSize = driver.get_window_size()
print(deviceSize)

screenWidth = deviceSize['width']
screenHeight = deviceSize['height']
print(screenHeight)
print(screenWidth)

startX = screenWidth / 2
endX = screenWidth / 2

startY = screenHeight * 6 / 9
endY = screenHeight / 9

driver.drag_and_drop(elementList[0], elementList[5])
