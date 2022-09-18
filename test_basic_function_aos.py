from datetime import datetime

import openpyxl

row = col = ''
now = datetime.now()
path = "./result/" + now.strftime("%Y%m%d-%H%M%S") + ".xlsx"


# 원본 TC 오픈해 내용 확인
def test_open_testcase(driver, tc_original):
    # noinspection PyGlobalUndefined
    global tc_edit
    sheet = tc_original["Sheet1"]
    # 원본 TC의 Sheet1 H3열의 값이 Result일 경우 result 폴더에 결과 TC 생성
    if sheet["H3"].value == "Result":
        tc_original.save(path)
        tc_edit = openpyxl.load_workbook("./result/" + now.strftime("%Y%m%d-%H%M%S") + ".xlsx")
        assert True
    else:
        driver.quit()
        assert False, "TC 로드 실패"


# 메인 화면에서 라인 이미지가 보이는지 확인
def test_ui_display_login_image(driver):
    sheet = tc_edit["Sheet1"]
    # 라인 이미지 객체를 ID로 검색
    image_login = driver.find_element("id", "jp.naver.line.android.registration:id/image")
    if image_login.is_displayed():
        sheet["H4"] = "Pass"
        tc_edit.save(path)
        assert True
    else:
        sheet["H4"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 라인 이미지가 보이지 않습니다."


# 메인 화면 웰컴 텍스트 문구 확인
def test_ui_display_login_welcome(driver):
    sheet = tc_edit["Sheet1"]
    # Welcome to LINE 텍스트 객체를 ID로 검색
    text_welcome = driver.find_element("id", "jp.naver.line.android.registration:id/header")

    # Welcome to LINE 텍스트 확인, 보이지 않을 경우 Fail 처리
    if text_welcome.is_displayed():
        sheet["H5"] = "Pass"
        tc_edit.save(path)
        assert True
    else:
        sheet["H5"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 Welcome to LINE 텍스트가 보이지 않습니다."

    # Welcome to LINE 텍스트 내용이 다를 경우 Fail 처리
    if text_welcome.text == "Welcome to LINE":
        sheet["H5"] = "Pass"
        tc_edit.save(path)
        assert True
    else:
        sheet["H5"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 Welcome to LINE 텍스트 내용이 다릅니다."


# 메인 화면 안내 텍스트 문구 확인
def test_ui_text_login_msg(driver):
    sheet = tc_edit["Sheet1"]
    # 안내 텍스트 객체를 ID로 검색
    text_msg = driver.find_element("id", "jp.naver.line.android.registration:id/desc")

    # 안내 텍스트가 보이는지 확인, 보이지 않을 경우 Fail 처리
    if text_msg.is_displayed():
        sheet["H6"] = "Pass"
        tc_edit.save(path)
        assert True
    else:
        sheet["H6"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 안내 텍스트가 보이지 않습니다."

    # 안내 텍스트 내용이 다를 경우 Fail 처리
    if text_msg.text == "Free messaging, voice and video calls, and more!":
        sheet["H6"] = "Pass"
        tc_edit.save(path)
        assert True
    else:
        sheet["H6"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 안내 텍스트 내용이 다릅니다."


# 메인 화면에서 로그인 버튼이 작동하는지 확인
def test_login_button(driver):
    sheet = tc_edit["Sheet1"]
    btn = driver.find_element("id", "jp.naver.line.android.registration:id/login")
    # 로그인 버튼이 보이는지 확인, 보이지 않을 경우 Fail 처리
    if btn.is_displayed():
        sheet["H7"] = "Pass"
        tc_edit.save(path)
        # 로그인 버튼이 보일 경우 로그인 버튼 클릭
        btn.click()
        assert True
    else:
        sheet["H7"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 로그인 버튼이 보이지 않습니다."


# 로그인 화면에서 핸드폰 로그인 버튼이 작동하는지 확인
def test_login_button_phone(driver):
    sheet = tc_edit["Sheet1"]
    btn = driver.find_element("id", "jp.naver.line.android.registration:id/auth_with_phone_number")
    if btn.is_displayed():
        sheet["H8"] = "Pass"
        tc_edit.save(path)
        # 로그인 버튼이 보일 경우 로그인 버튼 클릭
        btn.click()
        assert True
    else:
        sheet["H8"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 핸드폰 로그인 버튼이 보이지 않습니다."


# 핸드폰 로그인 화면에서 권한 팝업 노출 확인
def test_login_button_phone_access(driver):
    # jp.naver.line.android:id/common_dialog_content_text / 팝업 텍스트 ID
    # jp.naver.line.android:id/common_dialog_ok_btn / Not now 버튼 ID
    sheet = tc_edit["Sheet1"]
    btn = driver.find_element("id", "jp.naver.line.android:id/common_dialog_ok_btn")
    if btn.is_displayed():
        sheet["H9"] = "Pass"
        tc_edit.save(path)
        #  Continue 버튼이 보일 경우 버튼 클릭
        btn.click()
        assert True
    else:
        sheet["H9"] = "Fail"
        tc_edit.save(path)
        assert False, "핸드폰 로그인 화면의 권한 팝업에서 Continue 버튼이 보이지 않습니다."


# 핸드폰 로그인 화면에서 전화 허용 팝업 노출 확인
def test_login_button_phone_access_call(driver):
    # com.android.permissioncontroller:id/permission_message / 팝업 텍스트 ID
    # com.android.permissioncontroller:id/permission_deny_button / Deny 버튼 ID
    sheet = tc_edit["Sheet1"]
    btn = driver.find_element("id", "com.android.permissioncontroller:id/permission_allow_button")
    if btn.is_displayed():
        sheet["H10"] = "Pass"
        tc_edit.save(path)
        #  Allow 버튼이 보일 경우 버튼 클릭
        btn.click()
        assert True
    else:
        sheet["H10"] = "Fail"
        tc_edit.save(path)
        assert False, "핸드폰 로그인 화면의 전화 허용 팝업에서 Allow 버튼이 보이지 않습니다."


"""
# 로그인 화면에서 페이스북 로그인 버튼이 작동하는지 확인
def test_login_facebook(driver):
    sheet = tc_edit["Sheet1"]
    btn = driver.find_element("id", "jp.naver.line.android.registration:id/auth_with_facebook")
    # 페이스북 로그인 버튼이 보이는지 확인, 보이지 않을 경우 Fail 처리
    if btn.is_displayed():
        sheet["H8"] = "Pass"
        tc_edit.save(path)
        # 로그인 버튼이 보일 경우 로그인 버튼 클릭
        btn.click()
        assert True
    else:
        sheet["H8"] = "Fail"
        tc_edit.save(path)
        assert False, "로그인 화면의 페이스북 로그인 버튼이 보이지 않습니다."
"""
