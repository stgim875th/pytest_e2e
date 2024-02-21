import pytest
import time
import uiautomation as auto

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from class_file.login import PrivacyPage, LoginPage
from class_file.collaborate_menu_modal import CreateCollaborate

options = Options()
options.add_argument("--use-fake-ui-for-media-stream")  # 구글 카메라 동의 팝업창 해제
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행
options.add_experimental_option("detach", True) # 브라우저를 닫지 않고 유지

@pytest.fixture(scope = "module")
def browser():
    # 크롬 드라이버의 절대 경로 설정
    CHROME_DRIVER_PATH = (r'C:\chromedriver-win64\chromedriver.exe')
    service = Service(CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    # driver.quit

def test_privacy_page(browser):
    privacy_page = PrivacyPage(browser)

    # 개인 정보 보호 화면으로 이동
    privacy_page.go_to_privacy_page()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 비공개 페이지에서 고급 버튼 존재 확인
    privacy_page.advanced_button_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 비공개 페이지에서 고급 버튼 클릭
    privacy_page.click_advanced_button()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 비공개 페이지에서 (안전하지 않음) 링크 존재 확인
    privacy_page.unsafe_link_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 비공개 페이지에서 (안전하지 않음) 링크 클릭
    privacy_page.click_unsafe_link()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

def test_login(browser):
    login_page = LoginPage(browser)

    # Remote 로그인센터 화면 존재 확인
    login_page.go_to_login_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 아이디 입력 필드 존재 확인
    login_page.id_input_field_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 패스워드 입력 필드 존재 확인
    login_page.pw_input_field_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 로그인 버튼 존재 확인
    login_page.login_button_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 사용자 이름 및 비밀번호 입력 테스트
    Login_id = 'user1'
    Password = 'Admin1324'

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 아이디 입력
    user_id_input = login_page.enter_username(Login_id)

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 아이디와 입력된 값 비교
    user_id_input and login_page.compare_username(user_id_input.get_attribute("value"), Login_id)

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 패스워드 입력
    user_password_input = login_page.enter_password(Password)

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 아이디와 입력된 값 비교
    user_password_input and login_page.compare_password(user_password_input.get_attribute("value"), Password)

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 로그인 버튼 클릭
    login_page.click_login_button()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 로그인 결과 확인
    login_page.remote_layout_result()

    # 중복 로그인에 대한 예외 처리
    # 로그인 > 동일한 계정이 입력 되었을 경우 > 중복 로그인 모달창 출력 여부 확인
    login_page.duplicate_login_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 중복 로그인에 대한 예외 처리
    # 원격 종료 버튼 클릭
    login_page.click_swal2_actions()

def test_create_collaborate(browser):
    collaborate_modal = CreateCollaborate(browser)

    # 원격 협업 생성 버튼 존재 확인
    collaborate_modal.go_to_create_btn_displayed()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 원격 협업 생성 버튼 클릭
    collaborate_modal.click_create_btn()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 원격 협업 모달창 출력 확인
    collaborate_modal.collaborate_modal_displayed()

    # # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 원격 협업 생성하기 모달창 > 협업 프로필 등록 메뉴 존재 확인
    collaborate_modal.collaborate_profile_menu()

    # 3초동안 암묵적 대기
    browser.implicitly_wait(time_to_wait=3)

    # 원격 협업 생성하기 모달창 > 협업 프로필 이미지 등록 버튼 클릭
    collaborate_modal.click_profile_btn()

    # 3초동안 대기
    time.sleep(3)

    # # 이미지 업로드 테스트
    # input_file = 'barnacle.jpg'
    # collaborate_modal.upload_image(input_file)
    uploader = auto.WindowControl(searchDepth=2, Name='열기')
    time.sleep(2)
    uploader.EditControl(Name="파일 이름(N):").SendKeys('barnacle.jpg')
    uploader.EditControl(Name="파일 이름(N):").SendKeys('{ENTER}')

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 등록한 프로필 이미지가 정상적으로 업로드 되었는지 확인 절차
    # # 1. 프로필 이미지 엘리먼트 가져오기
    # # collaborate_modal.get_profile_image()

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 2. 이미지가 업로드되어 있는지 확인
    # # collaborate_modal.profile_image_upload_displayed()

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 3. 프로필 이미지 버튼 클릭 > 프로필 이미지 삭제
    # # collaborate_modal.click_profile_image_delete()

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 원격 협업 생성하기 모달창 > 협업 이름 입력창 존재 확인
    # collaborate_modal.collaborator_name_displayed()

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 원격 협업 생성하기 모달창 > default 협업 이름 지우기
    # collaborate_modal.delete_placeholder_name()

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 원격 협업 생성하기 모달창 > 협업 이름 새로 입력하기
    # input_new_name = 'E2E 테스트'
    # collaborate_modal.enter_collaborate_newname(input_new_name)

    # # 3초동안 대기
    # time.sleep(3)

    # # 원격 협업 생성하기 모달창 > 협업 설명 입력창 존재 확인
    # collaborate_modal.collaborate_description_displayed()

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 원격 협업 생성하기 모달창 > 협업 설명 입력하기
    # input_description = 'E2E 테스트 원격 협업 룸'
    # collaborate_modal.enter_collaborate_description(input_description)

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)

    # # 원격 협업 생성하기 모달창 > 시작하기 버튼 존재 확인
    # collaborate_modal.collaborator_modal_start()

    # # 3초동안 암묵적 대기
    # browser.implicitly_wait(time_to_wait=3)
