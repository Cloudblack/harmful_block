from selenium import webdriver 
from selenium.webdriver.common.by import By
import base64#불러온 url계속 base64라서 시도해봤는데 뭔가이상하다
import time
import urllib.request
options = webdriver.ChromeOptions() # 크롬 옵션 객체 생성
options.add_argument('headless') # headless 모드 설정
options.add_argument("disable-gpu") 
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
# 속도 향상을 위한 옵션 해제
prefs = {'profile.default_content_setting_values': {'cookies' : 2, 'images': 2, 'plugins' : 2, 'popups': 2, 'geolocation': 2, 'notifications' : 2, 'auto_select_certificate': 2, 'fullscreen' : 2, 'mouselock' : 2, 'mixed_script': 2, 'media_stream' : 2, 'media_stream_mic' : 2, 'media_stream_camera': 2, 'protocol_handlers' : 2, 'ppapi_broker' : 2, 'automatic_downloads': 2, 'midi_sysex' : 2, 'push_messaging' : 2, 'ssl_cert_decisions': 2, 'metro_switch_to_desktop' : 2, 'protected_media_identifier': 2, 'app_banner': 2, 'site_engagement' : 2, 'durable_storage' : 2}}   
options.add_experimental_option('prefs', prefs)
#크롬 웹드라이브 속도옵션설정이라는데 음 잘모르겠다..


num = 0 # 파일번호가 될 예정


dr = webdriver.Chrome(options=options)  #크롬 웹드라이브
dr.implicitly_wait(10) #로딩이완료될때까지 기다림 ,하지만 10초지마녀 가동
dr.set_window_size(414, 900) #브라우저 크기를 414*900으로 설정 
dr.get('https://www.pornhub.com/video?o=mv&t=a&cc=kr') #주소로 웹 오픈 
time.sleep(2) #로딩 대기


pagedowns = 1 #정확히는 페이지 번호
while pagedowns < 2273: #마지막페이지가 2273이라서..
    try:
         
        #img = dr.find_element(By.XPATH,'/html/body/div[3]/div/div[5]/div/div/ul/li[5]/div/div[1]/a/img')     
        img = dr.find_elements(By.CSS_SELECTOR,'li > div > div.phimage > a > img') #웹에서 요소를 찾을떄 쓴다 (요소 copy )      
        
        for i in img:             
            img_src = str(i.get_attribute('src'))#불러온 elements에서 src를 빼옴
            if 'data' not in img_src: #data들어간건 전부 base64파일이라 그냥 포기했음
            # if 'data' in img_src:
            #     img_src = img_src +'=' * (4-len(img_src) % 4)
            #     img_src = base64.b64decode(img_src)
                urllib.request.urlretrieve(img_src,"G:/porn/"+str(num) + '.png') #url주소를 저장한다 (저장할팔일,경로)
                num+=1  #하나끝날때마다 번호+1
            else:pass
        pagedowns += 1 #한페이지 끝날때마다 번호+1
        dr.get(f'https://www.pornhub.com/video?o=mv&t=a&cc=kr&page={pagedowns}')
        print(pagedowns)
        time.sleep(5)
    except:
        pagedowns += 1
        print('something wrong')
        time.sleep(60) #뭔가오류(보통 오래쓰면 한번씩 튕구더라..)나면 잠시 쉬었다가 진행
        continue

print('finish')


