import allure
import pytest
from appium.webdriver import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.appium_service import AppiumService
from allure_commons.types import AttachmentType


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep


@pytest.fixture(scope="function")
def appium_driver():
    global appium_service
    appium_service = AppiumService()
    appium_service.start()
    global driver
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
    yield driver
    driver.quit


@pytest.fixture()
def adding_screenshot_Fail(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="Error1", attachment_type=AttachmentType.PNG)
