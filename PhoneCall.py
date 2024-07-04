from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'emulator-5554',
    'appPackage': 'com.android.dialer',
    'appActivity': '.main.impl.MainActivity',
    'language': 'en',
    'locale': 'US'
}

url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
driver.implicitly_wait(10)

recentButton = driver.find_element(by=AppiumBy.ID, value='com.android.dialer:id/call_log_tab')
recentButton.click()

keyPad = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.ImageButton[@content-desc="key pad"]')
keyPad.click()

press_0 = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='0')
press_0.click()

press_1 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="1,"]')
press_1.click()

press_8 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="8,TUV"]')
press_8.click()
press_8.click()
press_1.click()

press_9 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="9,WXYZ"]')
press_9.click()

press_2 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="2,ABC"]')

press_2.click()
press_9.click()

press_3 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="3,DEF"]')
press_3.click()

press_4 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="4,GHI"]')
press_4.click()

press_6 = driver.find_element(by=AppiumBy.XPATH, value='//android.widget.FrameLayout[@content-desc="6,MNO"]')
press_6.click()

callButton = driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='dial')
callButton.click()
