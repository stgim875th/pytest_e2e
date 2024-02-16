import uiautomation as auto
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# 원격 협업 생성 클래스 생성
class CreateCollaborate:
    def __init__(self, driver):
        self.driver = driver
        # 원격 협업 생성 버튼
        self.create_colla_btn = (By.XPATH, "//button[@class='btn' and contains(text(), '원격 협업 생성')]")
        
        # 원격 협업 모달창
        self.remote_modal = (By.XPATH, "//div[@class='modal createroom-modal']/div[@class='modal--inner']/div[@class='modal--header']/following-sibling::div[@class='modal--body']")
        
        # 협업 프로필 등록 버튼
        self.profile_btn = (By.XPATH, "//div[@class='createroom']/section[@class='createroom-info']/button[@class='btn normal createroom-info_regist-image']")
        
        # 협업 프로필 이미지
        self.profile_image = (By.XPATH, "//div[@class='createroom']/section[@class='createroom-info']/div[@class='profile-image group']/img[@class='profile-image__image']")
        
        # 열기 창 관련 UI 요소 초기화
        # self.uploader = auto.WindowControl(searchDepth=2, Name='열기')
        # self.file_name_edit = self.uploader.EditControl(Name="파일 이름(N):")
        
        # 원격 협업 생성하기 모달창 > 협업 이름 입력창
        self.collaborator_name = (By.XPATH, "//div[@class='createroom']/section[@class='createroom-info']/figure[1][@class='inputrow']/input[@type='text' and @class='inputrow-input input']")
        
        # 원격 협업 모달창 > Default 협업 이름
        self.placeholder_name = (By.XPATH, "//div[@class='createroom']/section[@class='createroom-info']/figure[1][@class='inputrow']/input[@type='text' and @class='inputrow-input input']")
        
        # 원격 협업 모달창 > 협업 설명 입력창
        self.collaborate_description = (By.XPATH, "//div[@class='createroom']/section[@class='createroom-info']/figure[2][@class='inputrow']/textarea[@type='text' and @class='inputrow-input textarea']")
        
        # 원격 협업 모달창 > 선택한 멤버(그룹 리스트에서 user2멤버 선택)
        self.member_user2 = (By.XPATH, "//section[@class='createroom-info']/figure[3][@class='inputrow']/div[@class='profilelist']")
        
        # 원격 협업 모달창 > 시작하기 버튼
        self.start_button = (By.XPATH, "//div[@class='modal--inner']/div[2][@class='modal--body']/div[@class='createroom']/section[@class='createroom-info']/button[@class='btn large createroom-info__button disabled' and contains(text(), '시작하기')]")
        
        # 원격 협업 모달창 > 특정 그룹 선택 Select_box_button
        self.group_box_button = (By.XPATH, "//div[@class='createroom-user__header']/span[@class='popover--wrapper createroom-user--group-selects']/button[@class='select-label']")
        
        # 원격 협업 모달창 > 특정 그룹 선택  Select_box_button > 특정 그룹 옵션 박스
        self.group_option_box = (By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']")
        
        # 원격 협업 모달창 > 특정 그룹 선택 Select_box_button > 특정 그룹 버튼
        self.group_option_button = (By.XPATH, "//section[@class='remote-layout']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option active']")
        
        # 원격 협업 모달창 > 새로 고침 버튼
        self.collaborate_refresh = (By.XPATH, "//div[@class='createroom-user__header']/button[@class='icon-button refresh']")
        
        # 원격 협업 모달창 > 마우스 아래로 이동 > 마우스 위로 이동
        self.vue_scrollbar = (By.XPATH, "//div[@class='createroom-user__body']/div[@class='vue-scrollbar__wrapper']")
        
        # 원격 협업 모달창 > 멤버 리스트 
        self.collapsible_member = (By.XPATH, "//div[@class='createroom-user__body']/div[@class='vue-scrollbar__wrapper']")
        
        # 원격 협엄 모달창 > 그룹 리스트 열기/닫기 버튼
        self.group_list_option = [
            {
                "xpath" : "//div[@class='scroll--inner']/div[1]/div[@class='collapsible member-collapsible opend decorated']/button[@class='collapsible__button opend decorated']",
                "message" : "그룹 리스트 닫기 버튼을 클릭했습니다.",
                "timeout" : 5
                },
            {
                "xpath" : "//div[@class='scroll--inner']/div[1]/div[@class='collapsible member-collapsible decorated']/button[@class='collapsible__button decorated']",
                "message" : "그룹 리스트 열기 버튼을 클릭했습니다.",
                "timeout" : 5
                }
            ]
        
        # 원격 협업 생성하기 모달창 > 선택 가능한 멤버 리스트 > user2 멤버 클릭 > 멤버 해제 > 다시 user2 멤버 선택
        self.user_option = [
        {
            "xpath" : "//div[@class='collapsible member-collapsible opend decorated']/div[@class='collapsible__content opend']/div[3][@class='widecard choice']",
            "message" : "user2를 선택했습니다.",
            "timeout" : 5
            },
        {
            "xpath" : "//div[@class='collapsible member-collapsible opend decorated']/div[@class='collapsible__content opend']/div[3][@class='widecard choice selected']",
            "message" : "user2 선택 취소했습니다.",
            "timeout" : 5
            },
        {
            "xpath": "//div[@class='collapsible member-collapsible opend decorated']/div[@class='collapsible__content opend']/div[3][@class='widecard choice']",
            "message": "user2를 다시 선택했습니다.",
            "timeout": 5
            }
        ]
        # 원격 협업 생성하기 모달창 > 닫기 버튼
        self.modal_close_button = (By.XPATH, "//div[@class='modal--header']/button[@class='modal--close']")
        
    # 원격 협업 생성 버튼 존재 확인
    def go_to_create_btn_displayed(self):
        try:
            create_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.create_colla_btn)))
            if create_btn.is_displayed():
                print("원격 협업 생성 버튼이 존재합니다.")
            else:
                print("원격 협업 생성 버튼이 존재하지 않습니다.")
            return create_btn.is_displayed()
        except NoSuchElementException:
            print("원격 협업 생성 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성 버튼 클릭
    def click_create_btn(self):
        try:
            create_btn_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.create_colla_btn))
            actions = ActionChains(self.driver)
            actions.move_to_element(create_btn_click)
            actions.click(create_btn_click)
            actions.perform()
            print("원격 협업 생성 버튼을 클릭했습니다.")
            return create_btn_click
        except NoSuchElementException:
            print("원격 협업 생성 버튼을 찾을 수 없습니다.")
            return None
    
    # 원격 협업 모달창 출력 확인
    def  collaborate_modal_displayed(self):
        try:
            modal_display = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.remote_modal)))
            if modal_display.is_displayed():
                print("원격 협업 모달창이 출력되었습니다.")
            else:
                print("원격 협업 모달창이 출력되지 않았습니다.")
            return modal_display.is_displayed()
        except NoSuchElementException:
            print("원격 협업 생성 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성하기 모달창 > 협업 프로필 등록 메뉴 존재 확인
    def collaborate_profile_menu(self):
        try:
            profile_menu = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((self.profile_btn)))
            if profile_menu.is_displayed():
                print("협업 프로필 등록 메뉴가 존재합니다.")
            else:
                print("협업 프로필 등록 메뉴가 존재하지 않습니다.")
            return profile_menu.is_displayed
        except NoSuchElementException:
            print("협업 프로필 등록 메뉴를 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성하기 모달창 > 협업 프로필 등록 메뉴 클릭
    def click_profile_btn(self):
        try:
            profile_btn_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.profile_btn)))
            actions = ActionChains(self.driver)
            actions.move_to_element(profile_btn_click)
            actions.click(profile_btn_click)
            actions.perform()
            print("협업 프로필 등록 버튼을 클릭했습니다.")
            return profile_btn_click
        except NoSuchElementException:
            print("협업 프로필 등록 버튼을 찾을 수 없습니다.")
            return None
        
    # 열기창에서 등록할 프로필 이미지 업로드
    # def upload_image(self, file_name):
        # # 이미지 업로드를 위한 메서드
        # time.sleep(2)
        # self.file_name_edit.SendKeys(file_path)
        # self.file_name_edit.SendKeys('{ENTER}')
        
    # 열기창에서 등록할 프로필 이미지 업로드
    def upload_image(self, file_name):
        uploader = auto.WindowControl(searchDepth=2, Name='열기')
        time.sleep(2)
        uploader.EditControl(Name="파일 이름(N):").SendKeys(file_name)
        uploader.EditControl(Name="파일 이름(N):").SendKeys('{ENTER}')
        
    # 등록한 프로필 이미지가 정상적으로 업로드 되었는지 확인 절차
    # 1. 프로필 이미지 엘리먼트 가져오기
    def get_profile_image(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.profile_image)))
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
                EC.presence_of_element_located((self.profile_image)))
            actions = ActionChains(self.driver)
            actions.move_to_element(profile_image_delete)
            actions.click(profile_image_delete)
            actions.perform()
            print("프로필 이미지 삭제 버튼을 클릭했습니다.")
            return profile_image_delete
        except NoSuchElementException:
            print("프로필 이미지 삭제 버튼을 클릭하지 못했습니다.")
            return None
    
    # 원격 협업 생성하기 모달창 > 협업 이름 입력창 존재 확인
    def collaborator_name_displayed(self):
        try:
            collaborator_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborator_name)))
            if collaborator_name.is_displayed():
                print("협업 이름 입력창이 존재합니다.")
            else:
                print("협업 이름 입력창이 존재하지 않습니다.")
            return collaborator_name.is_displayed()
        except NoSuchElementException:
            print("협업 이름 입력창을 찾을 수 없습니다.")
            return False    
    
    # 원격 협업 생성하기 모달창 > Default 협업 이름 지우기
    def delete_placeholder_name(self):
        try:
            placeholder = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.placeholder_name)))
            placeholder.clear()
            print("협업 이름을 지웠습니다.")
            return placeholder
        except NoSuchElementException:
            print("협업 이름을 지우지 못했습니다.")
            return None
            
    # 원격 협업 생성하기 모달창 > 협업 이름 새로 입력하기
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
        
    # 원격 협업 생성하기 모달창 > 협업 설명 입력창 존재 확인
    def collaborate_description_displayed(self):
        try:
            collaborate_description = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_description)))
            if collaborate_description.is_displayed():
                print("협업 설명 입력창이 존재합니다.")
            else:
                print("협업 설명 입력창이 존재하지 않습니다.")
            return collaborate_description.is_displayed()
        except NoSuchElementException:
            print("협업 이름 설명 입력창을 찾을 수 없습니다.")
            return False
             
    # 원격 협업 생성하기 모달창 > 협업 설명 입력하기
    def enter_collaborate_description(self, newdescription):
        try:
            new_description = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_description)))
            new_description.send_keys(newdescription)
            print(f"협업 설명 : '{newdescription}'가 정상적으로 입력되었습니다.")
            return new_description
        except NoSuchElementException:
            print(f"협업 설명 : '{newdescription}'가 정상적으로 입력되지 않았습니다.")
            return None
    
    # 원격 협업 생성하기 모달창 > 시작하기 버튼 존재 확인
    def collaborator_modal_start(self):
        try:
            start_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.start_button)))
            if start_btn.is_displayed():
                print("시작하기 버튼이 존재합니다.")
            else:
                print("시작하기 버튼이 존재하지 않습니다.")
            return start_btn.is_displayed()
        except NoSuchElementException:
            print("시작하기 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성하기 모달창 > 시작하기 버튼
    def collaborator_start_button(self):
        try:
            modal_start_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.start_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(modal_start_click)
            actions.click(modal_start_click)
            actions.perform()
            print("원격 협업 생성하기 [시작하기] 버튼을 클릭했습니다.")
            return modal_start_click
        except NoSuchElementException:
            print("원격 협업 생성하기 [시작하기] 버튼을 찾을 수 없습니다.")
            return None
        
    #################################################
    # 원격 협업 생성하기 모달창 > 협업 이름 20차 초과하기
    def enter_collaborate_fullnewname(self):
        try:
            full_new_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.placeholder_name)))
            full_new_name.is_displayed()
            print()
        except NoSuchElementException:
            print()
    ################################################
    # 원격 협업 생성하기 모달창 > 특정 그룹 선택 Select_box_button 존재 확인
    def group_box_btn_displayed(self):
        try:
            group_box_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.group_box_button)))
            if group_box_btn.is_displayed():
                print("그룹 선택 버튼이 존재합니다.")
            else:
                print("그룹 선택 버튼이 존재하지 않습니다.")
            return group_box_btn.is_displayed()
        except NoSuchElementException:
            print("그룹 선택 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성하기 모달창 > 특정 그룹 선택 Select_box_button 클릭
    def click_group_box_btn(self):
        try:
            group_box_btn_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.group_box_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(group_box_btn_click)
            actions.click(group_box_btn_click)
            actions.perform()
            print("그룹 선택 Select_box_button을 클릭했습니다.")
            return group_box_btn_click
        except NoSuchElementException:
            print("그룹 선택 Select_box_button을 찾을 수 없습니다.")
            return None
         
    # 원격 협업 생성하기 모달창 > 새로 고침 존재 확인
    def collaborator_refresh(self):
        try:
            refresh_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_refresh)))
            if refresh_btn.is_displayed():
                print("새로 고침 버튼이 존재합니다.")
            else:
                print("새로 고침 버튼이 존재하지 않습니다.")
            return refresh_btn.is_displayed()
        except NoSuchElementException:
            print("새로 고침 버튼을 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성하기 모달창 > 새로 고침 버튼 클릭
    def click_collaborator_refresh(self):
        try:
            refresh_btn_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_refresh)))
            actions = ActionChains(self.driver)
            actions.move_to_element(refresh_btn_click)
            actions.click(refresh_btn_click)
            actions.perform()
            print("새로 고침 버튼을 클릭했습니다.")
            return refresh_btn_click
        except NoSuchElementException:
            print("새로 고침 버튼을 찾을 수 없습니다.")
            return None
            
    # 원격 협업 생성하기 모달창 > 멤버 리스트 > 마우스 아래 이동
    def scroll_down(self):
        try:
            vue_scrollbar = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.vue_scrollbar))
            self.driver.execute_script(
                "arguments[0].scrollTop += arguments[0].offsetHeight;", vue_scrollbar)
            print("멤버 리스트를 아래로 이동했습니다.")
            return vue_scrollbar
        except NoSuchElementException:
            print("멤버 리스트를 아래로 이동하지 못했습니다.")
            return None
        
    # 원격 협업 생성하기 모달창 > 멤버 리스트 > 마우스 위로 이동
    def scroll_up(self):
        try:
            vue_scrollbar = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(self.vue_scrollbar))
            self.driver.execute_script(
                "arguments[0].scrollTop -= arguments[0].offsetHeight;", vue_scrollbar)
            print("멤버 리스트를 위로 이동했습니다.")
            return vue_scrollbar
        except NoSuchElementException:
            print("멤버 리스트를 위로 이동하지 못했습니다.")
            return None
    
    # 원격 협업 생성하기 모달창 > 그룹 리스트 열기 및 닫기 클릭
    def group_user_list(self):
        try:
            for group_xpath in self.group_list_option:
                group_user_btn = WebDriverWait(self.driver, float(str(group_xpath["timeout"]))).until(
                    EC.presence_of_element_located((By.XPATH, str(group_xpath["xpath"]))))
                actions = ActionChains(self.driver)
                actions.move_to_element(group_user_btn)
                actions.click(group_user_btn)
                actions.perform()
            time.sleep(3)
        except NoSuchElementException:
            print("그룹 리스트 열기 및 닫기 버튼을 찾을 수 없습니다.")
            return None
        
    # 원격 협업 생성하기 모달창 > 협업 멤버 리스트 존재 확인
    def member_list_displayed(self):
        try:
            member_list = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collapsible_member)))
            if member_list.is_displayed():
                print("멤버 리스트가 존재합니다.")
            else:
                print("멤버 리스트가 존재하지 않습니다.")
            return member_list.is_displayed()
        except NoSuchElementException:
            print("멤버 리스트를 찾을 수 없습니다.")
            return False
    
    # 원격 협업 생성하기 모달창 > 선택 가능한 멤버 리스트에서 user2 멤버 선택하기
    def member_user2_list(self):
        try:
            for user_xpath in self.user_option:
                user_select = WebDriverWait(self.driver, float((str(user_xpath["timeout"])))).until(
                    EC.presence_of_element_located((By.XPATH, str(user_xpath["xpath"]))))
                actions = ActionChains(self.driver)
                actions.move_to_element(user_select)
                actions.click(user_select)
                actions.perform()
                print(user_xpath["message"])
                return user_select
        except NoSuchElementException:
            print("user2 멤버를 찾을 수 없습니다.")
            return None
        
    # 원격 협업 생성하기 모달창 > 선택한 멤버 확인
    def select_member(self):
        try:
            member_user2 = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.member_user2)))
            if member_user2.is_displayed():
                print("선택 가능한 멤버에 user2 멤버가 선택이 되었습니다.")
            else:
                print("선택 가능한 멤버에 user2 멤버가 선택되지 않았습니다.")
            return member_user2.is_displayed()
        except NoSuchElementException:
            print("선택 가능한 멤버를 찾을 수 없습니다.")
            return False
        
    # 원격 협업 생성하기 모달창 > 닫기 버튼 존재 확인
    def remote_modal_close(self):
        try:
            modal_close_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.modal_close_button)))
            if modal_close_btn.is_displayed():
                print("원격 협업 생성하기 모달창 닫기 버튼이 존재합니다.")
            else:
                print("원격 협업 생성하기 모달창 닫기 버튼이 존재하지 않습니다.")
            return modal_close_btn.is_displayed()
        except NoSuchElementException:
            print("원격 협업 생성하기 모달창 닫기 버튼을 찾을 수 없습니다.")
            return False
            
    # 원격 협업 생성하기 모달창 > 닫기 버튼 클릭
    def remote_modal_close_click(self):
        try:
            modal_close_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.modal_close_button)))
            actions = ActionChains(self.driver)
            actions.move_to_element(modal_close_click)
            actions.click(modal_close_click)
            actions.perform()
            print("원격 협업 생성하기 모달창 닫기 버튼을 클릭했습니다.")
        except NoSuchElementException:
            print("원격 협업 생성하기 모달창 닫기 버튼을 찾을 수 없습니다.")
            return None