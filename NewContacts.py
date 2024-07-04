from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

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

plusButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='Create new contact')
plusButton.click()

firstName = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]')
firstName.send_keys("MAHBUB2")

# Alternative locator selection with Android UiAutomator
driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, value='new UiSelector().text("Last name")').send_keys('ISLAM2')
# lastName = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Last name"]')
# lastName.send_keys("Islam")

phoneNumber = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]')
phoneNumber.send_keys("01881929347")

saveButton = driver.find_element(by=AppiumBy.ID, value='com.android.contacts:id/editor_menu_save_button')
saveButton.click()