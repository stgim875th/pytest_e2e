import uiautomation as auto
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# 오픈룸 생성 클래스 생성
class OpenRoomCreate:
    def __init__(self, driver):
        self.driver = driver
        # 오픈룸 생성 메뉴
        self.open_room_menu = (By.XPATH, "//button[@class='btn workspace-welcome__open' and contains(text(), '오픈룸 생성')]")
        
        # 오픈룸 모달창
        self.open_room = (By.XPATH, "//div[@class='modal openroom-modal']/div[@class='modal--inner']/div[2][@class='modal--body']")
        
        # 오픈룸 생성 > 협업 프로필 이미지 출력 메뉴
        self.profile_image = (By.XPATH, "//div[@class='openroom']/section[@class='openroom-info']/div[@class='profile-image group']")
        
        # 오픈룸 생성 > 협업 프로필 등록 버튼
        self.profile_btn = (By.XPATH, "//div[@class='openroom']/section[@class='openroom-info']/button[@class='btn normal openroom-info_regist-image']")
        
        # 오픈룸 생성 > 협업 프로필 이미지 등록
        self.profile_image_add = (By.XPATH, "//div[@class='openroom']/section[@class='openroom-info']/div[@class='profile-image group']/button[@class='profile-image__button']")
        
        # 열기 창 관련 UI 요소 초기화
        self.uploader = auto.WindowControl(searchDepth=2, Name='열기')
        self.file_name_edit = self.uploader.EditControl(Name="파일 이름(N):")
        
        # 오픈룸 생성 > 협업 이름 입력창
        self.collaborate_name = (By.XPATH, "//div[@class='openroom']/section[@class='openroom-info']/figure[@class='inputrow']/input[@class='inputrow-input input']")
        
        # 오픈룸 생성 > Default 협업 이름
        self.placeholder_name = (By.XPATH, "//div[@class='openroom']/section[@class='openroom-info']/figure[@class='inputrow']/input[@class='inputrow-input input']")
        
        # 오픈룸 생성 > 협업 설명 입력창
        self.collaborate_description = (By.XPATH, "//div[@class='openroom']/section[@class='openroom-info']/figure[2][@class='inputrow']/textarea[@class='inputrow-input textarea']")
        
        # 오픈룸 생성학 모달창 > 시작하기 버튼
        self.open_room_start_button = (By.XPATH, "//div[@class='openroom']/section[@class='openroom-info']/button[2][@class='btn large openroom-info__button' and contains(text(), '시작하기')]")
        
        # 오픈룸 생성 모달창 > 닫기 버튼
        self.open_room_close = (By.XPATH, "//div[@class='modal openroom-modal']/div[2][@class='modal--inner']/div[@class='modal--header']/button[@class='modal--close']")
        
    # 오픈룸 생성 메뉴 존재 확인
    def create_open_room_displayed(self):
        try:
            open_room = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.open_room_menu)))
            if open_room.is_displayed():
                print("오픈룸 생성 메뉴가 존재합니다.")
            else:
                print("오픈룸 생성 메뉴가 존재하지 않습니다.")
            return open_room.is_displayed()
        except NoSuchElementException:
            print("오픈룸 메뉴를 찾을 수 없습니다.")
            return False
    
    # 오픈룸 생성 메뉴 클릭
    def click_open_room_menu(self):
        try:
            open_room_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.open_room_menu)))
            actions = ActionChains(self.driver)
            actions.move_to_element(open_room_click)
            actions.click(open_room_click)
            actions.perform()
            print("오픈룸 생성하기 메뉴를 클릭했습니다.")
            return open_room_click
        except NoSuchElementException:
            print("오픈룸 생성하기 메뉴를 클릭하지 못했습니다.")
            return None
    
    # 오픈룸 생성 모달창 출력 확인
    def open_room_modal_displayed(self):
        try:
            open_room_modal = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.open_room)))
            if open_room_modal.is_displayed():
                print("오픈룸 생성 모달창이 존재합니다.")
            else:
                print("오픈룸 생성 모달창이 존재하지 않습니다.")
            return open_room_modal.is_displayed()
        except NoSuchElementException:
            print("오픈룸 생성 모달창을 찾을 수 없습니다.")
            
    # 오픈룸 생성하기 모달창 > 협업 프로필 이미지 메뉴 존재 확인
    def collaborator_image_displayed(self):
        try:
            profile_image = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.profile_image)))
            if profile_image.is_displayed():
                print("협업 프로필 이미지 출력 메뉴가 존재합니다.")
            else:
                print("협업 프로필 이미지 출력 메뉴가 존재하지 않습니다.")
            return profile_image.is_displayed()
        except NoSuchElementException:
            print("협업 프로필 이미지 출력 메뉴를 찾을 수 없습니다.")
            return False
        
    # 오픈룸 생성하기 모달창 > 협업 프로필 등록 메뉴 존재 확인
    def collaborator_name_displayed(self):
        try:
            collaborator_name = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((self.profile_btn)))
            if collaborator_name.is_displayed():
                print("협업 프로필 등록 메뉴가 존재합니다.")
            else:
                print("협업 프로필 등록 메뉴가 존재하지 않습니다.")
            return collaborator_name.is_displayed()
        except NoSuchElementException:
            print("협업 프로필 등록 메뉴를 찾을 수 없습니다.")
            return False
    
    # 오픈룸 생성하기 모달창 > 협업 프로필 등록 메뉴 클릭
    def click_collaborator_name(self):
        try:
            open_room_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.profile_btn)))
            actions = ActionChains(self.driver)
            actions.move_to_element(open_room_btn)
            actions.click(open_room_btn)
            actions.perform()
            print("협업 프로필 등록 메뉴를 클릭했습니다.")
            return open_room_btn
        except NoSuchElementException:
            print("협업 프로필 등록 메뉴를 클릭하지 못했습니다.")
            return None
    
    # 열기창에서 등록할 프로필 이미지 업로드
    def upload_image(self, file_path):
        # 이미지 업로드를 위한 메서드
        time.sleep(2)
        self.file_name_edit.SendKeys(file_path)
        self.file_name_edit.SendKeys('{ENTER}')
    
    # 등록한 프로필 이미지가 정상적으로 업로드 되었는지 확인 절차
    # 1. 프로필 이미지 엘리먼트 가져오기
    def get_profile_image(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.profile_image_add)))
        except NoSuchElementException:
            return False
    
    # 2. 이미지가 업로드되어 있는지 확인
    def profile_image_upload_displayed(self):
        profile_image = self.get_profile_image()
        if profile_image and profile_image.get_attribute("src") != "":
            print("프로필 이미지가 업로드되었습니다.")
            return True
        else:
            print("프로필 이미지가 업로드되지 않았습니다.")
            return False
    
     # 3. 프로필 이미지 버튼 클릭 > 프로필 이미지 삭제
    def click_profile_image_delete(self):
        try:
            profile_image_delete = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.profile_image_add)))
            actions = ActionChains(self.driver)
            actions.move_to_element(profile_image_delete)
            actions.click(profile_image_delete)
            actions.perform()
            print("프로필 이미지 삭제 버튼을 클릭했습니다.")
            return profile_image_delete
        except NoSuchElementException:
            print("프로필 이미지 삭제 버튼을 클릭하지 못했습니다.")
            return None
    
    # 오픈룸 생성하기 모달창 > 협업 이름 입력창 존재 확인
    def open_room_name_displayed(self):
        try:
            collaborate_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_name)))
            if collaborate_name.is_displayed():
                print("협업 이름 입력창이 존재합니다.")
            else:
                print("협업 이름 입력창이 존재하지 않습니다.")
            return collaborate_name.is_displayed()
        except NoSuchElementException:
            print("협업 이름 입력창을 찾을 수 없습니다.")
    
    # 오픈룸 생성하기 모달창 > Default 협업 이름 지우기
    def delete_placehoder_name(self):
        try:
            open_placehoder = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.placeholder_name)))
            open_placehoder.clear()
            print("협업 이름을 지웠습니다.")
            return open_placehoder
        except NoSuchElementException:
            print("협업 이름을 지우지 못했습니다.")
            return None
    
    # 오픈룸 생성하기 모달창 > 협업 이름 새로 입력하기
    def enter_collaborate_newname(self, newname):
        try:
            new_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.placeholder_name)))
            new_name.send_keys(newname)
            print(f"협업 이름 : '{newname}'가 정상적으로 입력되었습니다.")
            return new_name
        except NoSuchElementException:
            print(f"협업 이름 : '{newname}'가 정상적으로 입력되지 않았습니다.")
            return None
        
    # 오픈룸 생성하기 모달창 > 협업 설명 입력창 존재 확인
    def open_room_description_displayed(self):
        try:
            open_room_description = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_description)))
            if open_room_description.is_displayed():
                print("협업 설명 입력창이 존재합니다.")
            else:
                print("협업 설명 입력창이 존재하지 않습니다.")
            return open_room_description.is_displayed()
        except NoSuchElementException:
            print("협업 이름 입력창을 찾을 수 없습니다.")
    
    # 오픈룸 생성 모달창 > 협업 설명에 내용 입력하기
    def enter_open_room_description(self, description):
        try:
            description_input = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_description)))
            description_input.send_keys(description)
            print(f"협업 이름 : '{description}'가 정상적으로 입력되었습니다.")
            return description_input
        except NoSuchElementException:
            print(f"협업 이름 : '{description}'가 정상적으로 입력되지 않았습니다.")
            return None
    
    # 오픈룸 생성하기 모달창 > 시작하기 메뉴 존재 확인
    def open_room_start_button_diaplayed(self):
        try:
            start_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.open_room_start_button)))
            if start_btn.is_displayed():
                print("오픈룸 생성학 모달창에 [시작하기] 메뉴가 존재합니다.")
            else:
                print("오픈룸 생성학 모달창에 [시작하기] 메뉴가 존재하지 않습니다.")
            return start_btn.is_displayed()
        except NoSuchElementException:
            print("오픈룸 생성하기 모달창에 [시작하기] 메뉴를 찾을 수 없습니다.")
            
    # 오픈룸 생성하기 모달창 > 시작하기 메뉴 클릭
    def click_open_room_start(self):
        try:
            start_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.open_room_start_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(start_button)
            actions.click(start_button)
            actions.perform()
            print("오픈룸 생성하기 모달창에서 [시작하기] 버튼을 클릭했습니다.")
            return start_button
        except NoSuchElementException:
            print("오픈룸 생성하기 모달창에서 [시작하기] 버튼을 찾을 수 없습니다.")
    
    # 오픈룸 생성하기 모달창 > 닫기 버튼 존재 확인
    def open_room_close_button(self):
        try:
            open_close_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.open_room_close)))
            if open_close_btn.is_displayed():
                print("오픈룸 생성 모달창에 [닫기] 버튼이 존재합니다.")    
            else:
                print("오픈룸 생성 모달창에 [닫기] 버튼이 존재하지 않습니다.")
            return open_close_btn.is_displayed()
        except NoSuchElementException:
            print("오픈룸 생성 모달창에 [닫기] 버튼을 찾을 수 없습니다.")
    
    # 오픈룸 생성 모달창 > 닫기 버튼 클릭
    def click_open_room_close(self):
        try:
            close_button = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.open_room_close)))
            actions = ActionChains(self.driver)
            actions.move_to_element(close_button)
            actions.click(close_button)
            print("오픈룸 생성하기 모달창에서 [닫기] 버튼을 클릭했습니다.")
            return close_button
        except NoSuchElementException:
            print("오픈룸 생성하기 모달창에서 [닫기] 버튼을 찾을 수 없습니다.")