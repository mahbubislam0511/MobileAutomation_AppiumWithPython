import time

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

# firstName = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]')
# firstName.send_keys("RAKIB")
#
# lastName = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Last name"]')
# lastName.send_keys("HASAN")
#
# phoneNumber = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]')
# phoneNumber.send_keys("01881929350")
#
savingTypeDropdownButton = driver.find_element(AppiumBy.XPATH, '//android.widget.Spinner[@content-desc="Phone"]')
savingTypeDropdownButton.click()

options = driver.find_elements(AppiumBy.XPATH, '//android.widget.CheckedTextView[@resource-id="android:id/text1"]')
print(len(options))

for option in options:
    print(option.text)
    if option.text == "Other":
        option.click()
        break

saveButton = driver.find_element(by=AppiumBy.ID, value='com.android.contacts:id/editor_menu_save_button')
saveButton.click()
