import openpyxl
import pytest
from appium import webdriver
from datetime import datetime

now = datetime.now()
TC = "testcase.xlsx"    # 원본 TC 파일명
APPIUM_SERVER_ADDRESS = 'http://localhost:4723/wd/hub'  # appium 서버 주소
# appium 설정 값
automation_name = 'UiAutomator2'
platform_name = 'Android'
platform_version = '11.0'
device_name = 'Android Emulator'
app = 'D:\LINE.apk'
appPackage = 'jp.naver.line.android'
appActivity = 'activity.SplashActivity'


@pytest.fixture(scope="session")
def driver():
    android_caps = {'automationName': automation_name, 'platformName': platform_name,
                    'platformVersion': platform_version, 'deviceName': device_name,
                    'app': app, 'appPackage': appPackage, 'appActivity': appActivity, 'noReset': False}
    driver = webdriver.Remote(APPIUM_SERVER_ADDRESS, android_caps)

    return driver


@pytest.fixture(scope="session")
def tc_original():
    testcase = openpyxl.load_workbook("testcase.xlsx")

    return testcase


@pytest.fixture(scope="session")
def tc_edit():
    testcase = openpyxl.load_workbook("./result/" + now.strftime("%Y%m%d-%H%M%S") + ".xlsx")

    return testcase
