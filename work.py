from selenium import webdriver
import datetime
import time
from selenium.webdriver.common.action_chains import ActionChains
import json
import  os
import unittest
from selenium.webdriver.common.keys import Keys
import sys
import warnings
class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    FAIL = '\033[91m' #RED
    RESET = '\033[0m' #RESET COLOR
def hbjson(a,b):
    x={a:b}
    with open(r'json path', 'w') as file:
        json.dump(x, file)
    os.system(r'bot disocrd path')
hbjson("","")


driver = webdriver.Edge(executable_path=r' driver path ')

driver.get("website link")




search_btn = driver.find_element_by_class_name("authlink")
search_btn.click()



driver.get(" website planning link")


now = datetime.datetime.today()
d = now.isoweekday()
dmy= "{}".format(now.date())
dd =dmy[8:]
year=dmy[:4]
m=dmy[5:]
mm=m[:-3]
dmy="{}/{}/{}".format(dd,mm,year)


time.sleep(3)
q= 1 + d 
path = ('/html/body/div[1]/div/div[4]/table/tbody/tr[2]/td[{}]'.format(q)) 
all_elements = driver.find_elements_by_xpath(path)
print(all_elements)
dw={}
a=[]
bt=[]
ttt=[]
for element in all_elements: 
    all_texts = element.find_elements_by_class_name("wc-time")
    all_words = element.find_elements_by_class_name("get-syllabus")
    print('Schedules :')
    tt=0
    for text in all_texts :
        print(bcolors.OK+text.text+bcolors.RESET)
        ttt.append(text.text)
    for word in all_words :
        dw[ttt[tt]] = word.text
        print(bcolors.OK+word.text+bcolors.RESET)
        if "DS" in word.text :
         print("Schedule :",bcolors.WARNING+ttt[tt]+bcolors.RESET,"It's a",bcolors.WARNING+"DS"+bcolors.RESET)
        if "COLLES" in word.text :
         print("Schedule :",bcolors.WARNING+ttt[tt]+bcolors.RESET,"It's a",bcolors.FAIL+"COLLES"+bcolors.RESET)
        else:
            a.append(ttt[tt])
        tt +=1
driver.quit()

nb= len(a)
nc = nb - 1
dhh={"08:00 - 08:30" :(8,0),"08:30 - 09:00": (8,30),"09:30 - 10:00":(9,30),"10:30 - 11:00":(10,30),"11:30 - 12:00":(11,30),"12:30 - 13:00":(12, 30),"13:30 - 14:00":(13, 30),"14:30 - 15:00": (14, 30),"15:30 - 16:00": (15, 30),"16:30 - 17:00": (16, 30),"17:30 - 18:00": (17, 30),"18:30 - 19:00": (18, 30),"19:30 - 20:00": (19, 30),"09:00 - 09:30": (9,00),"10:00 - 10:30": (10, 00),"11:00 - 11:30": (11, 00),"12:00 - 12:30": ( 12, 00),"13:00 - 13:30": (13, 00),"14:00 - 14:30": (14, 00),"15:00 - 15:30": (15, 00),"16:00 - 16:30": ( 16, 00),"17:00 - 18:30": (17, 00),"18:30 - 19:00": (18, 00),"19:00 - 19:30": (19, 00),"20:00 – 20:30": (20, 00),"08:00 - 09 :00": (8,00),"08:30 - 09:30": (8,30),"09:00 - 10:00": (9,00),"09:30 - 10:30": (9,30),"10:00 - 11:00": (10,00),"10:30 - 11:30": (10,30),"11:00 - 12:00": (11,00),"11:30 - 12:30": (11,30),"12:00 - 13:00": (12,00),"12:30 - 13:30": (12,30),"13:00 - 14:00": (13,00),"13:30 - 14:30": (13,30),"14:00 - 15:00": (14,00),"14:30 - 15:30": (14,30),"15:00 - 16:00": (15,00),"15:30 - 16:30": (15,30),"16:00 - 17:00": (16,00),"16:30 - 17:30": (16,30),"17:00 - 18:00": (17,00),"17:30 - 18:30": (17,30),"18:00 - 19:00": (18,00),"18:30 - 19:30": (18,30),"19:00 - 20:00": (19,00),"19:30 - 20:30": (19,30),"08:00 - 09:30": (8,00),"08:30 - 10:00": (8,30),"09:00 - 10:30": (9, 00),"09:30 - 11:00": (9, 30),"10:00 - 11:30": (10, 00),"10:30 - 12:00": (10, 30),"11:00 - 12:30": (11, 00),"11:00 - 13:00": (11, 30),"12:00 - 13:30": (12, 00),"12:30 - 14:00": (12, 30),"13:00 - 14:30": (13, 00),"14:00 - 15:30": (13, 30),"14:30 - 16:00": (14, 00),"15:00 - 16:30": (14, 30),"15:30 - 17:00": (15, 00) ,"16:00 - 17:30": (15, 30),"16:00 - 18:00": (16, 00),"17:00 - 18:30": (16, 30),"17:30 - 19:00": (17, 00),"18:00 - 19:30": (17, 30),"18:30 - 20:00": (18, 00),"19:30 - 20:30": (18, 30),"08:00 - 10:00": (8,00),"08:30 - 10:30": (8,30),"09:00 - 11:00": (9,00),"09:30 - 11:30": (9,30),"10:00 - 12:00": (10,00),"10:30 - 12:30": (10,30),"11:00 - 13:00": (11,00),"11:30 - 13:30": (11,30),"12:00 - 14:00": (12,00),"12:30 - 14:30": (12,30),"13:00 - 15:00": (13,00),"13:30 - 15:30": (13,30),"14:00 - 16:00": (14,00),"14:30 - 16:30": (14,30),"15:00 - 17:00": (15,00),"15:30 - 17:30": (15,30), "16:00 - 18:00": (16,00),"16:30 - 18:30": (16,30),"17:00 - 19:00": (17,00),"17:30 - 19:30": (17,30),"18:00 - 20:00": (18,00),"18:30 - 20:30": (18,30),"08:00 - 10:30": (8,00),"08:30 - 11:00": (8, 30),"09:00 - 11:30": (9, 00),"09:30 - 12:00": (9, 30),"10:00 - 12:30": (10, 00),"10:30 - 13:00": (10, 30),"11:00 - 13:30": (11, 00),"11:30 - 14:00": (11, 30),"12:00 - 14:30": (12, 00),"12:30 - 15:00": (12, 30),"13:00 - 15:30": (13, 00),"13:30 - 16:00": (13, 30),"14:00 - 16:30": (14, 00),"14:30 - 17:00": (14, 30),"15:00 - 17:30": (15, 00),"15:30 - 18:00": (15, 30),"16:00 - 18:30": (16, 00),"16:30 - 19:00": (16, 30),"17:00 - 19:30": (17, 00),"17:30 - 20:00": (17, 30),"18:00 - 20:30": (18, 00),"08:00 - 11:00": (8,00),"08:30 - 11:30": (8,30),"09:00 - 12:00": (9,00),"09:30 - 12:30": (9,30),"10:00 - 13:00": (10,00),"10:30 - 13:30": (10,30),"11:00 - 14:00": (11,00),"11:30 - 14:30": (11,30),"12:00 - 15:00": (12,00),"12:30 - 15:30": (12,30),"13:00 - 16:00": (13,00),"13:30 - 16:30": (13,30),"14:00 - 17:00": (14,00),"14:30 - 17:30": (14,30),"15:00 - 18:00": (15,00),"15:30 - 18:30": (15,30),"16:00 - 19:00": (16,00),"16:30 - 19:30": (16,30),"17:00 - 20:00": (17,00),"17:30 - 20:30": (17,30),"08:00 - 11:30": (8,00),"08:30 - 12:00":(8,30),"09:00 - 12:30":(9, 00),"09:30 - 13:00":(9, 30),"10:00 - 13:30":(10, 00),"10:30 - 14:00":(10, 30),"11:00 - 14:30":(11, 00),"11:30 - 15:00":(11, 30),"12:00 - 15:30":(12, 00),"12:30 - 16:00":(12, 30),"13:00 - 16:30":(13, 00),"13:30 - 17:00":(13, 30),"14:00 - 17:30":(14, 00),"14:30 - 18:00":(14, 30),"15:00 - 18:30":(15,0),"15:30 - 19:00":(15, 30),"16:00 - 19:30":(16, 00),"16:30 - 20:00":(16, 30),"17:00 - 20:30":(17, 00),"08:00 - 12:00": (8,00),"08:30 - 12:30": (8,30),"09:00 - 13:00": (9,00),"09:30 - 13:30": (9,30),"10:00 - 14:00": (10,00),"10:30 - 14:30": (10,30),"11:00 - 15:00": (11,00),"11:30 - 15:30": (11,30),"12:00 - 16:00": (12,00),"12:30 - 16:30": (12,30),"13:00 - 17:00": (13,00),"13:30 - 17:30": (13,30),"14:00 - 18:00": (14,00),"14:30 - 18:30": (14,30),"15:00 - 19:00": (15,00),"15:30 - 19:30": (15,30),"16:00 - 20:00": (16,00),"16:30 - 20:30":(16,30)}
dh=list(dhh.keys())
n = len(dhh)
cpt=0
hmarge = []
while cpt < n :
    apt=0
    while apt < nb :
        if dh[cpt] in a[apt] :
            hmarge.append(dh[cpt])
            
        apt = apt +1
    cpt = cpt + 1
def check_h(): 
    if cpt == 166 and apt == nb:
        print("check is done : ",bcolors.OK + "True" + bcolors.RESET)
    else:
        print("check is done : ",bcolors.FAIL+"error fail schedule"+bcolors.RESET)
check_h()
hmarge=sorted(hmarge)
nh= len(hmarge)
i=0
def regjson():
    x={dw[hmarge[i]]:hmarge[i]}
    with open(r'json path', 'w') as file:
        json.dump(x, file)
    os.system(r'python bot disocrd path')

def emarge():
    driver = webdriver.Edge(executable_path=r"driver path")
    driver.get("action path")  
    time.sleep(1)
    search_btn = driver.find_element_by_class_name("authlink")
    search_btn.click()
    time.sleep(2)
    driver.get("action path") 
    time.sleep(3)
    path2 = ("//*[text()='{}']".format(dw[hmarge[i]]))
    path4=("/html/body/div[6]/div[1]/div[2]/div[2]/div[1]/div/table/tbody/tr[1]/td[1]/span[1]")
    all_cars=driver.find_elements_by_xpath(path2)
    for car in all_cars :
        car.click()
        time.sleep(1)
        check=driver.find_element_by_xpath(path4).text
        print(type(check),type(dmy), check,dmy)
        if check == dmy:
            print("sign")
            canvas = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[2]/div[2]/div[1]/div/table/tbody/tr[1]/td[2]/div/div/canvas')
            drawing = ActionChains(driver)
            drawing.move_to_element(canvas).click().perform()
            driver.find_element_by_xpath('//*[@id="cboxLoadedContent"]/div/div/button[1]').click()
            regjson()
    driver.quit()


while i< nh :
    tho=dhh[hmarge[i]]
    th=tho[0]
    tm=tho[1]
    rh=now.hour
    rm=now.minute
    rs=now.second
    #print(th,tm,rh,rm,rs)
    wh=th-rh
    wm=tm-rm
    #print(wm,wh)
    if wm<0 :
        wh=wh-1
        wm=60+wm
    #print(wm,wh)
    wt=(wh*3600)+(wm*60)-rs
    wt=wt-3*60
    #print(wt)
    if wt<0: 
        print("Schedule exceeded:",bcolors.FAIL+hmarge[i]+bcolors.RESET,"n'est pas pris en compte")  

    else :
        print("Schedule register on:", bcolors.OK + hmarge[i] + bcolors.RESET)
        print("We wait:",bcolors.OK+str(wt)+bcolors.RESET,'secondes')
        time.sleep(wt)
        emarge()
    i=i+1
hbjson("","")

exit()
