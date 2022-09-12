from appium import webdriver
import pytest

APPIUM_SERVER_ADDRESS = 'http://localhost:4723/wd/hub'
automation_name = 'UiAutomator2'
platform_name = 'Android'
platform_version = '11.0'
device_name = 'Android Emulator'
app = 'D:\LINE.apk'
appPackage = 'jp.naver.line.android'
appActivity = 'activity.SplashActivity'


@pytest.fixture(scope="module")
def driver():
    # 아래 필요한 정보들을 기입해 줍니다.
    android_caps = {'automationName': automation_name, 'platformName': platform_name,
                    'platformVersion': platform_version, 'deviceName': device_name,
                    'app': app, 'appPackage': appPackage, 'appActivity': appActivity, 'noReset': True}
    driver = webdriver.Remote(APPIUM_SERVER_ADDRESS, android_caps)
    yield driver
    # 테스트 종료시 앱 종료
    # driver.quit()

def test_run(driver):
    assert True