from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

import time

# Remote header 클래스 생성
class HeaderArea:
    def __init__(self, driver):
        self.driver = driver
        
        # 워크스페이스 메뉴 xpath
        self.work_space_options = [
            {
                "xpath": "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']/button[@class='header-workspace-selector']",
                "message": "워크스페이스 메뉴를 클릭했습니다.",
                "timeout": 5
                },
            {
                "xpath": "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']/button[@class='header-workspace-selector selected']",
                "message": "워크스페이스 메뉴를 닫았습니다.",
                "timeout": 5
            }
        ]
        
    # 워크스페이스 메뉴 존재 확인
    def work_space_displayed(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located
                ((By.XPATH, "//section[@class='remote-layout']/header[@class='header workspace-selected']/div[@class='header-workspace']/nav[@class='header-workspace-lnb']/span[@class='popover--wrapper']")))
        except NoSuchElementException:
            return False
        
    # 워크스페이스 메뉴 클릭하기
    def click_workspace_menu(self):
        for option in self.work_space_options:
            work_space_btn = WebDriverWait(self.driver, option["timeout"]).until(
                EC.presence_of_element_located((By.XPATH, option["xpath"])))
            actions = ActionChains(self.driver)
            actions.move_to_element(work_space_btn)
            actions.click(work_space_btn)
            actions.perform()
            print(option["message"])
            time.sleep(3)
    
    # 영상 on/off 메뉴 존재 확인
    def display_menu(self):
        try:
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//div[@class='header-workspace']/ul[@class='header-workspace-tools']/div[1][@class='tooltip']")))
        except NoSuchElementException:
            return False