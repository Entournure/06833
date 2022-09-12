from appium import webdriver
import pytest

APPIUM_SERVER_ADDRESS = 'http://localhost:4723/wd/hub'
platform_name = 'Android'
platform_version = '7.1.1'
device_name = 'Android Emulator'
automation_name = 'Appium'
appPackage = ''     # 패키지 이름 / com.pakname.apkname
appActivity = ''
# 앱 경로\파일명 / C:\testapp.apk
app = 'D:\LINE.apk'
noReset = 'False'

@pytest.fixture(scope="module")
def driver():
    # 아래 필요한 정보들을 기입해 줍니다.
    android_caps = {'platformName': platform_name, 'platformVersion': platform_version, 'deviceName': device_name,
                    'automationName': automation_name, 'appPackage': appPackage,
                    'appActivity': appActivity, 'newCommandTimeout': 10000,
                    'app': app, 'noReset': noReset}
    driver = webdriver.Remote(APPIUM_SERVER_ADDRESS, android_caps)
    yield driver
    # 테스트 종료시 게임 종료
    # driver.quit()