
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
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