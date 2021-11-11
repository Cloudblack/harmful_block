from selenium import webdriver 
from selenium.webdriver import ActionChains 
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import urllib.request
import pickle

# usb 가져오지 못한다는 에러 자꾸 떠서 추가함
options = webdriver.ChromeOptions()
#options.add_argument('headless') # headless 모드 설정
#options.add_argument("window-size=1920x1080") # 화면크기(전체화면)
options.add_argument("disable-gpu") 





img_list=[]
num = 0

dr = webdriver.Chrome(options=options) 
dr.implicitly_wait(10)
dr.set_window_size(414, 900) #브라우저 크기를 414*900으로 설정 
dr.get('https://www.instagram.com/') #인스타그램 웹 오픈 
time.sleep(2) 

#로그인을 위해 아이디 패스워드 로그인버튼 위치를 따둔다
id_box = dr.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(1) > div > label > input") 
password_box = dr.find_element(By.CSS_SELECTOR,"#loginForm > div > div:nth-child(2) > div > label > input") 
login_button = dr.find_element(By.CSS_SELECTOR,'#loginForm > div > div:nth-child(3) > button')

act = ActionChains(dr) #액션체인을 몬듬
act.send_keys_to_element(id_box,'elije456@gmail.com').send_keys_to_element(password_box,'1346asddff').click(login_button).perform() 
#act.send_keys_to_element(id_box,'hahakim77@naver.com').send_keys_to_element(password_box,'1346asddff').click(login_button).perform() 
#키입력을 보낸다 (보낼위치,값) perform()은 모르겠다
time.sleep(3)


first_popup=dr.find_element(By.CSS_SELECTOR,'#react-root > section > main > div > div > div > div > button')
first_popup.click()#첫번째 팝업을 끔
time.sleep(2)

second_popup=dr.find_element(By.CSS_SELECTOR,'body > div.RnEpo.Yx5HN > div > div > div > div.mt3GC > button.aOOlW.HoLwm')
second_popup.click()#두번째팝업을 끔
time.sleep(2)

dr.get("https://www.instagram.com/explore/tags/selfie/") #태그에 셀카가있는 파일들
time.sleep(3)

elem = dr.find_element(By.TAG_NAME,"body") #아래로 내릴때 page down키를 쓰는데 바디를 누른상태로(?)눌러야된다
time.sleep(2)


pagedowns = 1
while pagedowns < 1000:
    
    try:        
        elem.send_keys(Keys.PAGE_DOWN) #Key가 진짜 키보드의 key였다 
        time.sleep(5)#요소를 부르거나 html변화가 생기는 작업에선 sleep을안주면 오류를 뱉는다(너무빠르다고..)      
        img = dr.find_elements(By.CSS_SELECTOR,'div.KL4Bh > img')
        time.sleep(2)
        
        for i in img: 
            time.sleep(0.5)
            img_src = str(i.get_attribute('src')) 
            img_list.append(img_src) #url 리스트에추가
            num+=1             
        time.sleep(10)      
        pagedowns += 1
        print(pagedowns)
        with open('insta.pickle', 'wb') as f:#혹시나 오류나서 날라갈까봐 무서워서 피클에 저장
            pickle.dump(img_list,f)
            
    except:  
        dr.get("https://www.instagram.com/explore/tags/selfie/")#무슨오륜지모르니까 페이지 다시불러옴
        time.sleep(5)        
        elem = dr.find_element(By.TAG_NAME,"body")
        time.sleep(5)
        pagedowns += 1
        print(pagedowns)
        print('something wrong')
        time.sleep(30)#뭔가오류(보통 오래쓰면 한번씩 튕구더라..)나면 잠시 쉬었다가 진행
        for x in range(pagedowns):            
            elem.send_keys(Keys.PAGE_DOWN)
            time.sleep(0.3)
        pass
       

img_list=list(set(img_list))#중복제거
for img_src,num in zip(img_list,range(len(img_list))): #리스트에 받아둔 url로 다운
    urllib.request.urlretrieve(img_src,"G:/insta/"+str(num) + '.png')
print('finish')

# 피클 다시불러오기
# with open ('insta.pickle','rb') as f:
# #     pickle_list =  pickle.load(f)



