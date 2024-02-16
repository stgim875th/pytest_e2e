import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

# 협업 예약 생성 클래스 생성
class CollaboSchedule:
    def __init__(self, driver):
        self.driver = driver
        
        # 협업 예약 메뉴
        self.collabo_schedule = (By.XPATH, "//button[@class='btn workspace-welcome__reservation' and contains(text(), '협업 예약')]")
        
        # 협업 예약 모달창
        self.collaborte_schedule_modal = (By.XPATH, "//div[@class='vue-scrollbar__area vue-scrollbar-transition']/section[@class='createreservation-info-section']")
        
        # 협업 이름
        self.collaborate_name = (By.XPATH, "//section[@class='createreservation-info-section']/div[1][@class='createreservation-info-section__row']/figure[@class='inputrow']/input[@type='text']")
        
        # 협업 설명
        self.collaborate_description = (By.XPATH, "//section[@class='createreservation-info-section']/div[2][@class='createreservation-info-section__row']/figure[@class='inputrow']/textarea[@type='text']")
        
        # 표준 시간대
        self.time_zone = (By.XPATH, "//section[@class='createreservation-info-section']/div[4][@class='createreservation-info-section__row']/div[@class='createreservation-info-section__label']/p/span[@class='required' and contains(text(), '표준 시간대')]")
        
        # 표준 시간대 > 표준 시간대 메뉴 버튼
        self.time_zone_btn_open = (By.XPATH, "//section[@class='createreservation-info-section']/div[4][@class='createreservation-info-section__row']/div[@class='createreservation-info-section__data']/span[@class='popover--wrapper createreservation-info__selector']/button[@class='select-label']")
        
        # 표준 시간대 > 표준 시간대 메뉴 닫기
        self.time_zone_btn_close = (By.XPATH, "//section[@class='createreservation-info-section']/div[4][@class='createreservation-info-section__row']/div[@class='createreservation-info-section__data']/span[@class='popover--wrapper createreservation-info__selector']/button[@class='select-label active']")
        
        # 표준 시간대 > 표준 시간대 드롭다운 박스
        self.time_zone_dropdown = (By.XPATH, "//div[@class='modal reservation-modal']/div[@role='tooltip' and @class='popover select-options']")
        
        # 표준 시간대 > 표준 시간대 드롭다운 박스 > Time zone 선택
        self.time_zone_options = [
            ('(GMT-11:00) 미드웨이 제도, 사모아', '(GMT-11:00) 미드웨이 제도, 사모아를 선택했습니다.'),
            ('(GMT-11:00) 파고파고', '(GMT-11:00) 파고파고를 선택했습니다.'),
            ('(GMT-10:00) 하와이', '(GMT-10:00) 하와이를 선택했습니다.'),
            ('(GMT-8:00) 알래스카', '(GMT-8:00) 알래스카를 선택했습니다.'),
            ('(GMT-8:00) 주노', '(GMT-8:00) 주노를 선택했습니다.'),
            ('(GMT-7:00) 밴쿠버', '(GMT-7:00) 밴쿠버를 선택했습니다.'),
            ('(GMT-7:00) 태평양 표준시(미국 및 캐나다)', '(GMT-7:00) 태평양 표준시(미국 및 캐나다)를 선택했습니다.'),
            ('(GMT-7:00) 티후아나', '(GMT-7:00) 티후아나를 선택했습니다.'),
            ('(GMT-7:00) 애리조나', '(GMT-7:00) 애리조나를 선택했습니다.'),
            ('(GMT-7:00) 마사틀란', '(GMT-7:00) 마사틀란를 선택했습니다.'),
            ('(GMT-7:00) 유콘', '(GMT-7:00) 유콘를 선택했습니다.'),
            ('(GMT-6:00) 에드먼턴', '(GMT-6:00) 에드먼턴를 선택했습니다.'),
            ('(GMT-6:00) 산지 표준시(미국 및 캐나다)', '(GMT-6:00) 산지 표준시(미국 및 캐나다)를 선택했습니다.'),
            ('(GMT-6:00) 서스캐처원', '(GMT-6:00) 서스캐처원를 선택했습니다.'),
            ('(GMT-6:00) 멕시코 시티', '(GMT-6:00) 멕시코 시티를 선택했습니다.'),
            ('(GMT-6:00) 과테말라', '(GMT-6:00) 과테말라를 선택했습니다.'),
            ('(GMT-6:00) 엘살바도르', '(GMT-6:00) 엘살바도르를 선택했습니다.'),
            ('(GMT-6:00) 마나과', '(GMT-6:00) 마나과를 선택했습니다.'),
            ('(GMT-6:00) 코스타리카', '(GMT-6:00) 코스타리카를 선택했습니다.'),
            ('(GMT-6:00) 테구시갈파', '(GMT-6:00) 테구시갈파를 선택했습니다.'),
            ('(GMT-6:00) 치와와', '(GMT-6:00) 치와와를 선택했습니다.'),
            ('(GMT-6:00) 몬테레이', '(GMT-6:00) 몬테레이를 선택했습니다.'),
            ('(GMT-5:00) 위니펙', '(GMT-5:00) 위니펙을 선택했습니다.'),
            ('(GMT-5:00) 중부 표준시(미국 및 캐나다)', '(GMT-5:00) 중부 표준시(미국 및 캐나다)를 선택했습니다.'),
            ('(GMT-5:00) 파나마', '(GMT-5:00) 파나마를 선택했습니다.'),
            ('(GMT-5:00) 보고타', '(GMT-5:00) 보고타를 선택했습니다.'),
            ('(GMT-5:00) 리마', '(GMT-5:00) 리마를 선택했습니다.'),
            ('(GMT-5:00) 에이커', '(GMT-5:00) 에이커를 선택했습니다.'),
            ('(GMT-4:00) 몬트리올', '(GMT-4:00) 몬트리올을 선택했습니다.'),
            ('(GMT-4:00) 동부 표준시(미국 및 캐나다)', '(GMT-4:00) 동부 표준시(미국 및 캐나다)를 선택했습니다.'),
            ('(GMT-4:00) 인디애나(동부)', '(GMT-4:00) 인디애나(동부)를 선택했습니다.'),
            ('(GMT-4:00) 푸에르토리코', '(GMT-4:00) 푸에르토리코를 선택했습니다.'),
            ('(GMT-4:00) 카라카스', '(GMT-4:00) 카라카스를 선택했습니다.'),
            ('(GMT-4:00) 라파스', '(GMT-4:00) 라파스를 선택했습니다.'),
            ('(GMT-4:00) 가이아나', '(GMT-4:00) 가이아나를 선택했습니다.'),
            ('(GMT-3:00) 핼리팩스', '(GMT-3:00) 핼리팩스를 선택했습니다.'),
            ('(GMT-3:00) 산티아고', '(GMT-3:00) 산티아고를 선택했습니다.'),
            ('(GMT-3:00) 몬테비디오', '(GMT-3:00) 몬테비디오를 선택했습니다.'),
            ('(GMT-3:00) 레시페', '(GMT-3:00) 레시페를 선택했습니다.'),
            ('(GMT-3:00) 부에노스아이레스, 조지타운', '(GMT-3:00) 부에노스아이레스, 조지타운을 선택했습니다.'),
            ('(GMT-3:00) 상파울루', '(GMT-3:00) 상파울루를 선택했습니다.'),
            ('(GMT-3:00) 대서양 표준시(캐나다)', '(GMT-3:00) 대서양 표준시(캐나다)를 선택했습니다.'),
            ('(GMT-2:30) 뉴펀들랜드 및 래브라도', '(GMT-2:30) 뉴펀들랜드 및 래브라도를 선택했습니다.'),
            ('(GMT-2:00) 그린란드', '(GMT-2:00) 그린란드를 선택했습니다.'),
            ('(GMT-2:00) 페르난두 지 노로냐', '(GMT-2:00) 페르난두 지 노로냐를 선택했습니다.'),
            ('(GMT-1:00) 카보베르데 제도', '(GMT-1:00) 카보베르데 제도를 선택했습니다.'),
            ('(GMT+0:00) 아조레스', '(GMT+0:00) 아조레스를 선택했습니다.'),
            ('(GMT+0:00) 세계 표준시 UTC', '(GMT+0:00) 세계 표준시 UTC를 선택했습니다.'),
            ('(GMT+0:00) 그리니치 표준시', '(GMT+0:00) 그리니치 표준시를 선택했습니다.'),
            ('(GMT+0:00) 레이캬비크', '(GMT+0:00) 레이캬비크를 선택했습니다.'),
            ('(GMT+0:00) 누악쇼트', '(GMT+0:00) 누악쇼트를 선택했습니다.'),
            ('(GMT+1:00) 더블린', '(GMT+1:00) 더블린을 선택했습니다.'),
            ('(GMT+1:00) 런던', '(GMT+1:00) 런던을 선택했습니다.'),
            ('(GMT+1:00) 리스본', '(GMT+1:00) 리스본을 선택했습니다.'),
            ('(GMT+1:00) 카사블랑카', '(GMT+1:00) 카사블랑카를 선택했습니다.'),
            ('(GMT+1:00) 서중앙 아프리카', '(GMT+1:00) 서중앙 아프리카를 선택했습니다.'),
            ('(GMT+1:00) 알제', '(GMT+1:00) 알제를 선택했습니다.'),
            ('(GMT+1:00) 튀니스', '(GMT+1:00) 튀니스를 선택했습니다.'),
            ('(GMT+2:00) 베오그라드, 브라티슬라바, 류블랴나', '(GMT+2:00) 베오그라드, 브라티슬라바, 류블랴나를 선택했습니다.'),
            ('(GMT+2:00) 사라예보, 스코페, 자그레브', '(GMT+2:00) 사라예보, 스코페, 자그레브를 선택했습니다.'),
            ('(GMT+2:00) 오슬로', '(GMT+2:00) 오슬로를 선택했습니다.'),
            ('(GMT+2:00) 코펜하겐', '(GMT+2:00) 코펜하겐을 선택했습니다.'),
            ('(GMT+2:00) 브뤼셀', '(GMT+2:00) 브뤼셀을 선택했습니다.'),
            ('(GMT+2:00) 암스테르담, 베를린, 로마, 스톡홀름, 비엔나', '(GMT+2:00) 암스테르담, 베를린, 로마, 스톡홀름, 비엔나를 선택했습니다.'),
            ('(GMT+2:00) 암스테르담', '(GMT+2:00) 암스테르담을 선택했습니다.'),
            ('(GMT+2:00) 로마', '(GMT+2:00) 로마를 선택했습니다.'),
            ('(GMT+2:00) 스톡홀름', '(GMT+2:00) 스톡홀름을 선택했습니다.'),
            ('(GMT+2:00) 비엔나', '(GMT+2:00) 비엔나를 선택했습니다.'),
            ('(GMT+2:00) 룩셈부르크', '(GMT+2:00) 룩셈부르크를 선택했습니다.'),
            ('(GMT+2:00) 파리', '(GMT+2:00) 파리를 선택했습니다.'),
            ('(GMT+2:00) 취리히', '(GMT+2:00) 취리히를 선택했습니다.'),
            ('(GMT+2:00) 마드리드', '(GMT+2:00) 마드리드를 선택했습니다.'),
            ('(GMT+2:00) 하라레, 프리토리아', '(GMT+2:00) 하라레, 프리토리아를 선택했습니다.'),
            ('(GMT+2:00) 바르샤바', '(GMT+2:00) 바르샤바를 선택했습니다.'),
            ('(GMT+2:00) 프라하 브라티슬라바', '(GMT+2:00) 프라하 브라티슬라바를 선택했습니다.'),
            ('(GMT+2:00) 부다페스트', '(GMT+2:00) 부다페스트를 선택했습니다.'),
            ('(GMT+2:00) 트리폴리', '(GMT+2:00) 트리폴리를 선택했습니다.'),
            ('(GMT+2:00) 요하네스버그', '(GMT+2:00) 요하네스버그를 선택했습니다. '),
            ('(GMT+2:00) 카르툼', '(GMT+2:00) 카르툼을 선택했습니다.'),
            ('(GMT+3:00) 헬싱키', '(GMT+3:00) 헬싱키를 선택했습니다.'),
            ('(GMT+3:00) 나이로비', '(GMT+3:00) 나이로비를 선택했습니다.'),
            ('(GMT+3:00) 소피아', '(GMT+3:00) 소피아를 선택했습니다.'),
            ('(GMT+3:00) 이스탄불', '(GMT+3:00) 이스탄불을 선택했습니다.'),
            ('(GMT+3:00) 아테네', '(GMT+3:00) 아테네를 선택했습니다.'),
            ('(GMT+3:00) 부카레스트', '(GMT+3:00) 부카레스트를 선택했습니다.'),
            ('(GMT+3:00) 니코시아', '(GMT+3:00) 니코시아를 선택했습니다.'),
            ('(GMT+3:00) 베이루트', '(GMT+3:00) 베이루트를 선택했습니다.'),
            ('(GMT+3:00) 다마스쿠스', '(GMT+3:00) 다마스쿠스를 선택했습니다.'),
            ('(GMT+3:00) 예루살렘', '(GMT+3:00) 예루살렘을 선택했습니다.'),
            ('(GMT+3:00) 암만', '(GMT+3:00) 암만을 선택했습니다.'),
            ('(GMT+3:00) 카이로', '(GMT+3:00) 카이로를 선택했습니다.'),
            ('(GMT+3:00) 모스크바', '(GMT+3:00) 모스크바를 선택했습니다.'),
            ('(GMT+3:00) 바그다드', '(GMT+3:00) 바그다드를 선택했습니다.'),
            ('(GMT+3:00) 쿠웨이트', '(GMT+3:00) 쿠웨이트를 선택했습니다.'),
            ('(GMT+3:00) 리야드', '(GMT+3:00) 리야드를 선택했습니다.'),
            ('(GMT+3:00) 바레인', '(GMT+3:00) 바레인을 선택했습니다.'),
            ('(GMT+3:00) 카타르', '(GMT+3:00) 카타르를 선택했습니다.'),
            ('(GMT+3:00) 아덴', '(GMT+3:00) 아덴을 선택했습니다.'),
            ('(GMT+3:00) 지부티', '(GMT+3:00) 지부티를 선택했습니다.'),
            ('(GMT+3:00) 모가디슈', '(GMT+3:00) 모가디슈를 선택했습니다.'),
            ('(GMT+3:00) 키예프', '(GMT+3:00) 키예프를 선택했습니다.'),
            ('(GMT+3:00) 민스크', '(GMT+3:00) 민스크를 선택했습니다.'),
            ('(GMT+3:00) 키시네프', '(GMT+3:00) 키시네프를 선택했습니다.'),
            ('(GMT+3:30) 테헤란', '(GMT+3:30) 테헤란을 선택했습니다.'),
            ('(GMT+4:00) 두바이', '(GMT+4:00) 두바이를 선택했습니다.'),
            ('(GMT+4:00) 무스카트', '(GMT+4:00) 무스카트를 선택했습니다.'),
            ('(GMT+4:00) 바쿠, 트빌리시, 예레반', '(GMT+4:00) 바쿠, 트빌리시, 예레반을 선택했습니다.'),
            ('(GMT+4:30) 카불', '(GMT+4:30) 카불을 선택했습니다.'),
            ('(GMT+5:00) 예카테린부르크', '(GMT+5:00) 예카테린부르크를 선택했습니다.'),
            ('(GMT+5:00) 이슬라마바드, 카라치, 타슈켄트', '(GMT+5:00) 이슬라마바드, 카라치, 타슈켄트를 선택했습니다.'),
            ('(GMT+5:30) 인도', '(GMT+5:30) 인도를 선택했습니다.'),
            ('(GMT+5:30) 뭄바이, 콜카타, 뉴델리', '(GMT+5:30) 뭄바이, 콜카타, 뉴델리를 선택했습니다.'),
            ('(GMT+5:30) 콜롬보', '(GMT+5:30) 콜롬보를 선택했습니다.'),
            ('(GMT+5:45) 카트만두', '(GMT+5:45) 카트만두를 선택했습니다.'),
            ('(GMT+6:00) 알마티', '(GMT+6:00) 알마티를 선택했습니다.'),
            ('(GMT+6:00) 다카', '(GMT+6:00) 다카를 선택했습니다.'),
            ('(GMT+6:00) 아스타나, 다카', '(GMT+6:00) 아스타나, 다카를 선택했습니다.'),
            ('(GMT+6:30) 랑군', '(GMT+6:30) 랑군을 선택했습니다.'),
            ('(GMT+7:00) 노보시비르스크', '(GMT+7:00) 노보시비르스크를 진행하겠습니다.'),
            ('(GMT+7:00) 크라스노야르스크', '(GMT+7:00) 크라스노야르스크를 선택했습니다.'),
            ('(GMT+7:00) 방콕', '(GMT+7:00) 방콕을 선택했습니다.'),
            ('(GMT+7:00) 베트남', '(GMT+7:00) 베트남을 선택했습니다.'),
            ('(GMT+7:00) 자카르타', '(GMT+7:00) 자카르타를 선택했습니다.'),
            ('(GMT+8:00) 이르쿠츠크, 울란바토르', '(GMT+8:00) 이르쿠츠크, 울란바토르를 선택했습니다.'),
            ('(GMT+8:00) 베이징, 상하이', '(GMT+8:00) 베이징, 상하이를 선택했습니다.'),
            ('(GMT+8:00) 홍콩 특별 행정구', '(GMT+8:00) 홍콩 특별 행정구를 선택했습니다.'),
            ('(GMT+8:00) 타이페이', '(GMT+8:00) 타이페이를 선택했습니다.'),
            ('(GMT+8:00) 쿠알라룸푸르', '(GMT+8:00) 쿠알라룸푸르를 선택했습니다.'),
            ('(GMT+8:00) 싱가포르', '(GMT+8:00) 싱가포르를 선택했습니다.'),
            ('(GMT+8:00) 퍼스', '(GMT+8:00) 퍼스를 선택했습니다.'),
            ('(GMT+9:00) 야쿠츠크', '(GMT+9:00) 야쿠츠크를 선택했습니다.'),
            ('(GMT+9:00) 서울', '(GMT+9:00) 서울을 선택했습니다.'),
            ('(GMT+9:00) 오사카, 삿포로, 도쿄', '(GMT+9:00) 오사카, 삿포로, 도쿄를 선택했습니다.'),
            ('(GMT+9:30) 다윈', '(GMT+9:30) 다윈을 선택했습니다.'),
            ('(GMT+10:00) 블라디보스토크', '(GMT+10:00) 블라디보스토크를 선택했습니다.'),
            ('(GMT+10:00) 괌, 포트모르즈비', '(GMT+10:00) 괌, 포트모르즈비를 선택했습니다.'),
            ('(GMT+10:00) 브리즈번', '(GMT+10:00) 브리즈번을 선택했습니다.'),
            ('(GMT+10:30) 애들레이드', '(GMT+10:30) 애들레이드를 선택했습니다.'),
            ('(GMT+11:00) 캔버라, 멜버른, 시드니', '(GMT+11:00) 캔버라, 멜버른, 시드니를 선택했습니다.'),
            ('(GMT+11:00) 호바트', '(GMT+11:00) 호바트를 선택했습니다.'),
            ('(GMT+11:00) 마가단', '(GMT+11:00) 마가단을 선택했습니다.'),
            ('(GMT+11:00) 솔로몬 제도', '(GMT+11:00) 솔로몬 제도를 선택했습니다.'),
            ('(GMT+11:00) 뉴칼레도니아', '(GMT+11:00) 뉴칼레도니아를 선택했습니다.'),
            ('(GMT+11:00) 로드하우 섬', '(GMT+11:00) 로드하우 섬을 선택했습니다.'),
            ('(GMT+12:00) 캄차카', '(GMT+12:00) 캄차카를 선택했습니다.'),
            ('(GMT+12:00) 피지 제도, 마샬 제도', '(GMT+12:00) 피지 제도, 마샬 제도를 선택했습니다.'),
            ('(GMT+13:00) 오클랜드, 웰링턴', '(GMT+13:00) 오클랜드, 웰링턴을 선택했습니다.'),
            ('(GMT+13:00) 사모아 독립국', '(GMT+13:00) 사모아 독립국을 선택했습니다.'),
            ('(GMT+9:00) 서울', '(GMT+9:00) 서울을 선택했습니다.')
            ]
    
    # 시작 일시 메뉴 > 달력 메뉴
    
    # 시작 일시 메뉴 > 달력 메뉴 선택
    
    # 시작 일시 메
    
    
    
    
    
    
    
    
    
    
    # 협업 예약 메뉴 존재 확인
    def collabo_schedule_displayed(self):
        try:
            collabo_schedule = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collabo_schedule)))
            if collabo_schedule.is_displayed():
                print("협업 예약 메뉴가 존재합니다.")
            else:
                print("협업 예약 메뉴가 존재하지 않습니다.")
            return collabo_schedule.is_displayed()
        except NoSuchElementException:
            print("협업 예약 메뉴를 찾을 수 없습니다.")
            return False
    
    # 협업 예약 메뉴 클릭
    def click_collabo_schedule(self):
        try:
            collabo_schedule_click = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collabo_schedule)))
            actions = ActionChains(self.driver)
            actions.move_to_element(collabo_schedule_click)
            actions.click(collabo_schedule_click)
            actions.perform()
            print("협업 예약 메뉴를 클릭했습니다.")
            return collabo_schedule_click
        except NoSuchElementException:
            print("협업 예약 메뉴를 클릭하지 못했습니다.")
            return None
    
    # 협업 예약 메뉴 > 협업 예약 메뉴 클릭 > 협업 예약 모달창 존재 확인
    def schedule_modal_displayed(self):
        try:
            schedule_modal = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborte_schedule_modal)))
            if schedule_modal.is_displayed():
                print("협업 예약 모달창이 존재합니다.")
            else:
                print("협업 예약 모달창이 존재하지 않습니다.")
            return schedule_modal.is_displayed()
        except NoSuchElementException:
            print("협업 예약 모달창을 찾을 수 없습니다.")
            return False
    
    # 협업 예약 모달창 > 협업 이름 메뉴 존재 확인
    def collaborate_name_displayed(self):
        try:
            collabo_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_name)))
            if collabo_name.is_displayed():
                print("협업 이름 메뉴가 존재합니다.")
            else:
                print("협업 이름 메뉴가 존재하지 않습니다.")
            return collabo_name.is_displayed()
        except NoSuchElementException:
            print("협업 이름 메뉴를 찾을 수 없습니다.")
            return False
            
    # 협업 예약 모달창 > Defalut 협업 이름 지우기
    def delete_collaborate_name(self):
        try:
            delete_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_name)))
            delete_name.clear()
            print("Defalut 협업 이름을 지웠습니다.")
            return delete_name
        except NoSuchElementException:
            print("Defalut 협업 이름을 지우지 못했습니다.")
            return None
        
    # 협업 예약 모달창 > new 협업 이름 입력하기
    def new_collaborate_name(self, newname):
        try:
            new_name = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_name)))
            new_name.send_keys(newname)
            print(f"협업 이름 {newname}가 정상적으로 입력되었습니다.")
            return new_name
        except NoSuchElementException:
            print(f"협업 이름 {newname}가 입력되지 않았습니다.")
            return None
        
    # 협업 예약 모달창 > 협업 설명 입력 메뉴 존재 확인
    def collaborate_description_displayed(self):
        try:
            description_displayed = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_description)))
            if description_displayed.is_displayed():
                print("협업 설명 입력 메뉴가 존재합니다.")
                return description_displayed.is_displayed()
            else:
                print("협업 설명 입력 메뉴가 존재하지 않습니다.")
        except NoSuchElementException:
            print("협업 설명 입력창을 찾을 수 없습니다.")
            return False
        
    # 협업 예약 모달창 > 협업 설명 입력창 > 협업 설명 입력하기
    def input_collaborate_description(self, newdescription):
        try:
            input_description = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.collaborate_description)))
            input_description.send_keys(newdescription)
            print(f"협업 설명 {newdescription} 내용을 입력했습니다.")
            return input_description
        except NoSuchElementException:
            print(f"협업 설명 {newdescription} 내용을 입력하지 못했습니다.")
            return None
        
    # 협업 모달창 > 표준 시간대 메뉴 존재 확인
    def time_zone_displayed(self):
        try:
            time_zone_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.time_zone)))
            if time_zone_menu.is_displayed():
                print("표준 시간대 메뉴가 존재합니다.")
            else:
                print("표준 시간대 메뉴가 존재하지 않습니다.")
            return time_zone_menu.is_displayed()
        except NoSuchElementException:
            print("표준 시간대 메뉴을 찾을 수 없습니다.")
            return False

    # 협업 예약 모달창 > 표준 시간대 > 표준 시간대 메뉴 버튼 존재 확인
    def time_zone_menu_button(self):
        try:
            time_zone_btn = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.time_zone_btn_open)))
            if time_zone_btn.is_displayed():
                print("표준 시간대 메뉴 버튼이 존재합니다.")
            else:
                print("표준 시간대 메뉴 버튼이 존재하지 않습니다.")
            return time_zone_btn.is_displayed()
        except NoSuchElementException:
            print("표준 시간대 메뉴 버튼을 찾을 수 없습니다.")
        
    # 협업 모달창 > 표준 시간대 메뉴 버튼 클릭
    def time_zone_menu_click(self):
        try:
            click_time_zone = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.time_zone_btn_open)))
            actions = ActionChains(self.driver)
            actions.move_to_element(click_time_zone)
            actions.click(click_time_zone)
            actions.perform()
            print("표준 시간대 메뉴를 클릭했습니다.")
            return click_time_zone
        except NoSuchElementException:
            print("표준 시간대 메뉴를 클릭하지 못했습니다.")
            
    # 협업 모달창 > 표준 시간대 메뉴 클릭 > 표준 시간대 드롭다운 박스 존재 확인
    def time_zone_optionbox_displayed(self):
        try:
            time_zone_optionbox = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.time_zone_dropdown)))
            if time_zone_optionbox.value_of_css_property('display') != 'none':
                print("협업 예약 : 표준 시간대 옵션 박스 메뉴가 존재합니다.")
            else:
                print("협업 예약 : 표준 시간대 옵션 박스 메뉴가 존재하지 않습니다.")
        except NoSuchElementException:
            print("협업 예약 : 표준 시간대 옵션 박스 메뉴를 찾을 수 없습니다.")
    
    # 협업 모달창 > 표준 시간대 메뉴 클릭 > 표준 시간대 재클릭 > 표준 시간대 메뉴 닫기
    def time_zone_menu_close(self):
        try:
            close_time_zone = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.time_zone_btn_close)))
            actions = ActionChains(self.driver)
            actions.move_to_element(close_time_zone)
            actions.click(close_time_zone)
            actions.perform()
            print("표준 시간대 메뉴를 닫았습니다.")
            return close_time_zone
        except NoSuchElementException:
            print("표준 시간대 메뉴를 닫지 못했습니다.")
            return None
        
    # 표준 시간대 > 표준 시간대 드롭다운 박스 > 각 Time zone들을 순차적으로 클릭
    def perform_time_zone_steps(self):
        for time_zone_click, time_zone_message in self.time_zone_options:
            self.click_time_zone_menu(time_zone_click)
            self.select_time_zone(time_zone_click, time_zone_message)
    
    # 표준 시간대 메뉴 버튼 선택
    def click_time_zone_menu(self, time_zone):
        try:
            time_zone_menu = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((self.time_zone_btn_open)))
            actions = ActionChains(self.driver)
            actions.move_to_element(time_zone_menu)
            actions.click(time_zone_menu)
            actions.perform()
            print(f"표준 시간대 :> {time_zone} 클릭했습니다.")
            time.sleep(3)
            return time_zone_menu
        except NoSuchElementException:
            print(f"표준 시간대 :> {time_zone} 클릭하지 못했습니다.")
            return False
        
    # 표준 시간대 > 표준 시간대 드롭다운 박스 > Time zone 선택
    def select_time_zone(self, time_zone_click, time_zone_message):
        try:
            time_zone_selection = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located(((By.XPATH, f"//div[@class='modal reservation-modal']/div[@role='tooltip' and @class='popover select-options']/div[@class='popover--body']/div[@class='select-optionbox']/button[@class='select-option' and contains(text(), '{time_zone_click}')]"))))
            actions = ActionChains(self.driver)
            actions.move_to_element(time_zone_selection)
            actions.click(time_zone_selection)
            actions.perform()
            print(time_zone_message)
            time.sleep(3)
            return time_zone_selection
        except NoSuchElementException:
            print("Time zone을 선택하지 못했습니다.")
            return False