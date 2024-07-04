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
driver.implicitly_wait(15)

el1 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value="Create new contact")
el1.click()

el2 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="First name"]')
el2.send_keys("Wasim")

el3 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.EditText[@text="Phone"]')
el3.send_keys("01988259898")

el4 = driver.find_element(by=AppiumBy.XPATH, value="//android.widget.Spinner[@content-desc=\"Phone\"]")
el4.click()

el5 = driver.find_element(by=AppiumBy.XPATH, value="/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.CheckedTextView[2]")
el5.click()

el6 = driver.find_element(by=AppiumBy.ID, value="com.android.contacts:id/editor_menu_save_button")
el6.click()
