from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

# PrivacyPage 클래스 생성
class PrivacyPage:
    def __init__(self, driver):
        self.driver = driver
        self.remote_url = 'https://192.168.0.180:8886/home'
        self.advanced_button = (By.XPATH, "//body[@class='ssl']/div[@class='interstitial-wrapper']/div[@class='nav-wrapper']/button[@id='details-button' and @class='secondary-button small-link' and contains(text(), '고급')]")
        self.unsafe_link = (By.XPATH, "//a[@id='proceed-link' and @class='small-link']")

    # 개인 정보 보호 화면으로 이동
    def go_to_privacy_page(self):
        self.driver.get(self.remote_url)
        time.sleep(3)
    
    # 비공개 페이지에서 고급 버튼 존재 확인
    def advanced_button_displayed(self):
        try:
            advanced_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.advanced_button)))
            if advanced_button.is_displayed():
                print("고급 버튼이 존재합니다.")
            else:
                print("고급 버튼이 존재하지 않습니다.")
            return advanced_button.is_displayed()
        except NoSuchElementException:
            print("고급 버튼을 찾을 수 없습니다.")
            return False
        
    # 비공개 페이지에서 고급 버튼 클릭
    def click_advanced_button(self):
        try:
            advanced_button_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.advanced_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(advanced_button_click)
            actions.click(advanced_button_click)
            actions.perform()
            print("비공개 페이지에서 [고급] 버튼을 클릭했습니다.")
        except NoSuchElementException:
            print("비공개 페이지에서 [고급] 버튼을 찾을 수 없습니다.")
    
    # 비공개 페이지에서 (안전하지 않음) 링크 존재 확인
    def unsafe_link_displayed(self):
        try:
            unsafe_link = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.unsafe_link)))
            if unsafe_link.is_displayed():
                print("비공개 페이지에 (안전하지 않음) 링크가 존재합니다.")
            else:
                print("비공개 페이지에 (안전하지 않음) 링크가 존재하지 않습니다.")
            return unsafe_link.is_displayed()
        except NoSuchElementException:
            print("비공개 페이지에 (안전하지 않음) 링크를 찾을 수 없습니다.")
            return False
    
    # 비공개 페이지에서 (안전하지 않음) 링크 클릭
    def click_unsafe_link(self):
        try:
            unsafe_link_button_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.unsafe_link)))
            actions = ActionChains(self.driver)
            actions.move_to_element(unsafe_link_button_click)
            actions.click(unsafe_link_button_click)
            actions.perform()
            print("비공개 페이지에서 (안전하지 않음) 링크를 클릭했습니다.")
        except NoSuchElementException:
            print("비공개 페이지에서 (안전하지 않음) 링크 클릭 할 수 업습니다.")

# Remote LoginPage 클래스 생성
class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        # 로그인 센터 화면
        self.login_center = (By.XPATH, "//div[@class='home-section']/div[@class='container']/div[@class='row-bg el-row is-justify-center is-align-middle el-row--flex']/div[@class='el-col el-col-24']/h2[@class='title' and contains(text(), '로그인')]")
        # 아이디 입력 필드
        self.user_id_locator = (By.XPATH, "//div[@class='email-input el-input el-input--suffix']/input[@type='text' and @autocomplete='off' and @name='email']")
        # 패스워드 입력 필드
        self.user_pwd_locator = (By.XPATH, "//div[@class='password-input el-input el-input--suffix']/input[@type='password' and @autocomplete='off' and @name='password']")
        # 비활성화되어 있는 로그인 버튼
        self.disabled_login_button = (By.XPATH, "//div[@class='el-col el-col-24']/button[@disabled='disabled' and @type='button' and @class='el-button next-btn block-btn el-button--info is-disabled']")
        # 활성환된 로그인 버튼
        self.enabled_login_button = (
            By.XPATH, "//div[@class='el-col el-col-24']/button[@type='button' and @class='el-button next-btn block-btn el-button--info']")
        # Remote layout 화면
        self.remote_layout = (By.XPATH, "//section[@class='remote-layout']")
        # 중복 로그인 모달창
        self.duplicate_login_alert = (
            By.XPATH, "//div[@class='swal2-content']/div[@id='swal2-content' and @class='swal2-html-container' and @style='display: block;']")
        # 중복 로그인 모달창 > 원격 종료 버튼
        self.swal2_actions = (
            By.XPATH, "//div[@class='swal2-actions']/button[@class='swal2-confirm swal2-styled' and contains(text(), '원격종료')]")

    # Remote 로그인센터 화면 존재 확인
    def go_to_login_displayed(self):
        try:
            login_center = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.login_center)))
            if login_center.is_displayed():
                print("로그인 센터 화면이 존재합니다.")
            else:
                print("로그인 센터 화면이 존재하지 않습니다.")
            login_center.is_displayed()
        except NoSuchElementException:
            print("로그인 센터 화면을 찾을 수 없습니다.")
            return False
        
    # 아이디 입력 필드 존재 확인
    def id_input_field_displayed(self):
        try:
            id_input_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.user_id_locator)))
            if id_input_field.is_displayed():
                print("아이디 입력 필드가 존재합니다..")
            else:
                print("아이디 입력 필드가 존재하지 않습니다.")
            return id_input_field.is_displayed()
        except NoSuchElementException:
            print("아이디 입력 필드를 찾을 수 없습니다.")
            return False
        
    # 패스워드 입력 필드 존재 확인
    def pw_input_field_displayed(self):
        try:
            pw_input_field = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.user_pwd_locator)))
            if pw_input_field.is_displayed():
                print("패스워드 입력 필드가 존재합니다.")
            else:
                print("패스워드 입력 필드가 존재하지 않습니다.")
            return pw_input_field.is_displayed()
        except NoSuchElementException:
            print("패스워드 입력 필드를 찾을 수 없습니다.")
            return False
        
    # 로그인 버튼 존재 확인
    def login_button_displayed(self):
        try:
            login_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.disabled_login_button)))
            if login_button.is_displayed():
                print("로그인 버튼이 존재합니다.")
            else:
                print("로그인 버튼이 존재하지 않습니다.")
            return login_button.is_displayed()
        except NoSuchElementException:
            print("로그인 버튼을 찾을 수 없습니다.")
            return False
    
    # 아이디 입력
    def enter_username(self, username):
        try:
            user_id = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.user_id_locator))
            user_id.send_keys(username)
            print(f"아이디 '{username}'이 입력이 되었습니다.")
            return user_id
        except NoSuchElementException:
            print(f"아이디 '{username}'이 입력되지 않았습니다.")
            return None
        
    # 아이디와 입력된 값 비교
    def compare_username(self, entered_username, expected_username):
        if entered_username ==  expected_username:
            print("아이디가 일치합니다.")
        else:
            print("아이디가 일치하지 않습니다.")
                
    # # 패스워드 입력
    def enter_password(self, password):
        try:
            user_pwd = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.user_pwd_locator))
            user_pwd.send_keys(password)
            print(f"패스워드 '{password}'가 입력되었습니다.")
            return user_pwd
        except NoSuchElementException:
            print(f"패스워드'{password}'가 입력되지 않았습니다.")
            return None
    
    # 패스워드와 입력된 값 비교
    def compare_password(self, enter_password, expected_password):
        if enter_password == expected_password:
            print("패스워드가 일치합니다.")
        else:
            print("패스워드가 일치하지 않습니다.")
            
    # 로그인 버튼 클릭
    def click_login_button(self):
        try:
            login_button_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.enabled_login_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(login_button_click)
            actions.click(login_button_click)
            actions.perform()
            print("로그인 버튼을 클릭했습니다.")
            return login_button_click
        except NoSuchElementException:
            print("로그인 버튼을 클릭하지 못했습니다.")
            return None
        
    # # 로그인 결과 확인
    def remote_layout_result(self):
        try:
            remote_web_layout = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((self.remote_layout)))
            if remote_web_layout.is_displayed():
                print("Remote web 화면으로 이동했습니다.")
            else:
                print("Remote web 화면으로 이동하지 못했습니다.")
            return remote_web_layout.is_displayed()
        except NoSuchElementException:
            print("Remote web 화면을 찾을 수 없습니다.")
            return False
        
    # 중복 로그인에 대한 예외 처리
    # 로그인 > 동일한 계정이 입력 되었을 경우 > 중복 로그인 모달창 출력 여부 확인
    def duplicate_login_displayed(self):
        try:
            duplicate_login = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.duplicate_login_alert)))
            if duplicate_login.is_displayed():
                print("다른 장치에서 이미 로그인 중입니다. 계속 하시려면 상대방의 접속을 종료시켜주세요.")
            else:
                print("중복 로그인창이 출력되지 않았습니다.")
        except TimeoutException:
            pass
        
    # 원격 종료 버튼 클릭
    def click_swal2_actions(self):
        try:
            swal2_actions_btn = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.swal2_actions))
            actions = ActionChains(self.driver)
            actions.move_to_element(swal2_actions_btn)
            actions.click(swal2_actions_btn)
            actions.perform()
            print("원격 종료 버튼을 클릭했습니다.")
            return swal2_actions_btn
        except TimeoutException:
            pass
