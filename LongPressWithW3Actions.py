from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.contacts',
    'appActivity': '.activities.PeopleActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(15)

contactList = driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.android.contacts:id/cliv_name_textview"]')
# mahbub = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.TextView[@content-desc="Salam"]')
print(len(contactList))

actions = ActionChains(driver)
actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
actions.w3c_actions.pointer_action.click_and_hold(contactList[1])
actions.perform()


