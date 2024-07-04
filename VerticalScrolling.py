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

activityButton = wait1.until(
    EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="Activity"]')))
activityButton.click()

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

# Scroll with x,y value
actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.move_to_location(startX, startY)
actions.w3c_actions.pointer_action.pointer_down()
actions.w3c_actions.pointer_action.pause(2)
actions.w3c_actions.pointer_action.move_to_location(endX, endY)
actions.w3c_actions.pointer_action.release()
actions.perform()

# Scroll with Android UiAutomator from top to down
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToEnd(5)')

# Scroll with Android UiAutomator from down to top
# driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).setAsVerticalList().scrollToBeginning(5)')
