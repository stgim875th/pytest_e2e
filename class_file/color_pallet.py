from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class ColorPallet:
    def __init__(self, driver):
        self.driver = driver
    
    # 색상 버튼 클릭
    def click_color_button(self):
        color_btn1 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='tooltip']/button[@class='tool']")
        color_btn1.click()
    
    # 색상 버튼 활성화
    def click_color_active(self):
        color_btn2 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='tooltip']/button[@class='tool active']")

# 색상 12종 클릭하기
    def click_color_2(self):
        color_click_btn_2 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[2][@class='picker--item']")
        color_click_btn_2.click()
        
    def click_color_3(self):
        color_click_btn_3 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[3][@class='picker--item']")
        color_click_btn_3.click()
        
    def click_color_4(self):
        color_click_btn_4 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[4][@class='picker--item']")
        color_click_btn_4.click()
        
    def click_color_5(self):
        color_click_btn_5 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[5][@class='picker--item']")
        color_click_btn_5.click()
        
    def click_color_6(self):
        color_click_btn_6 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[6][@class='picker--item']")
        color_click_btn_6.click()
        
    def click_color_7(self):
        color_click_btn_7 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[7][@class='picker--item']")
        color_click_btn_7.click()
        
    def click_color_8(self):
        color_click_btn_8 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[8][@class='picker--item']")
        color_click_btn_8.click()
        
    def click_color_9(self):
        color_click_btn_9 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[9][@class='picker--item']")
        color_click_btn_9.click()
        
    def click_color_10(self):
        color_click_btn_10 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[10][@class='picker--item']")
        color_click_btn_10.click()
        
    def click_color_11(self):
        color_click_btn_11 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[11][@class='picker--item']")
        color_click_btn_11.click()
        
    def click_color_12(self):
        color_click_btn_12 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[12][@class='picker--item']")
        color_click_btn_12.click()
        
    def click_color_1(self):
        color_click_btn_1 = self.driver.find_element(By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[1][@class='stream-tools tools']/div[2][@data-v-b85caa5a]/div[@class='picker--container']/div[@class='picker line_color']/ul[@class='picker--list']/li[1][@class='picker--item']")
        color_click_btn_1.click()
        
    # 포인팅 좌표 클릭
    def wait_for_participant_screen(self):
            return WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='main-video']/div[@class='main-video__box']/div[3][@class='main-video__pointing']")))

    def move_and_click_with_offset(self, pointing, x_offset, y_offset):
        actions = ActionChains(self.driver)
        actions.move_to_element(pointing)
        actions.click_and_hold(pointing)
        actions.drag_and_drop_by_offset(pointing, x_offset, y_offset)
        actions.click(pointing)
        actions.perform()
        
    def perform_pointing_actions(self):
        participant_screen = self.wait_for_participant_screen()
        self.move_and_click_with_offset(participant_screen,  0, 5)
        self.move_and_click_with_offset(participant_screen, 10, 15)
        self.move_and_click_with_offset(participant_screen, 0, -3)
        self.move_and_click_with_offset(participant_screen, -2, 5)
        self.move_and_click_with_offset(participant_screen, -3, 0)
    
    # 포인팅 좌표 클릭 (POD 적용 전 원본 코드)
    # participant_screen = WebDriverWait(driver, 5).until(
    #     EC.presence_of_element_located((By.XPATH, "//main[@class='main-wrapper']/div[@class='main-body stream']/div[@class='main-video']/div[@class='main-video__box']/div[3][@class='main-video__pointing']")))
    
    # actions = ActionChains(driver)\
    #     .move_to_element(participant_screen)\
    #     .click_and_hold(participant_screen)\
    #     .drag_and_drop_by_offset(participant_screen, 0, 5)\
    #     .click(participant_screen)\
    #     .drag_and_drop_by_offset(participant_screen, 10, 15)\
    #     .click(participant_screen)\
    #     .drag_and_drop_by_offset(participant_screen, 0, -3)\
    #     .click(participant_screen)\
    #     .drag_and_drop_by_offset(participant_screen, -2, 5)\
    #     .click(participant_screen)\
    #     .drag_and_drop_by_offset(participant_screen, -3, 0)\
    #     .click(participant_screen)\
    #     .perform()