import pickle
from time import sleep
import urllib.request

with open ('insta.pickle','rb') as f: #피클불러오기
    pickle_list =  pickle.load(f)




img_list=list(set(pickle_list))#중복제거
for img_src,num in zip(img_list,range(len(img_list))): #리스트에 받아둔 url로 다운
    try:
        urllib.request.urlretrieve(img_src,"G:/insta/"+str(num) + '.png')
    except:pass
    


            