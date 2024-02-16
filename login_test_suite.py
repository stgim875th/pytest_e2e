import pytest
# import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from class_file.login import PrivacyPage, LoginPage

options = Options()
options.add_argument("--use-fake-ui-for-media-stream")  # 구글 카메라 동의 팝업창 해제
options.add_argument('--start-maximized')  # 브라우저가 최대화된 상태로 실행
options.add_experimental_option("detach", True) # 브라우저를 닫지 않고 유지

@pytest.fixture(scope = "module")
def browser():
    # 크롬 드라이버의 절대 경로 설정
    CHROME_DRIVER_PATH = (r"C:\chromedriver-win64\chromedriver.exe")
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