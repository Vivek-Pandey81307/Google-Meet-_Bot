from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import schedule
import time
import datetime
import requests
from playsound import playsound

print("-----------------Script Started-------------------")

## To join class automatically 
def OnlineClassBot(links):
    email=" " # your mail ID
    password=" " # your mail password
    opt = Options()
    ## To load specific chrome profile 
    #profilePath="/home/manoj/Desktop/OnlineClass/selenium/"    ##paste the profile in directory so that you can keep your chrome tab of different profile running (avoid crash )   
    opt.add_argument("--user-data-dir=profilePath") 
    opt.add_argument("--disable-extensions")
    opt.add_argument('--profile-directory=Default')## G profile name
    ## Pass the argument 1 to allow and 2 to block
    ## allowing all the access (notifications,mic,camera)
    opt.add_experimental_option("prefs", { \
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 1 
    })
    ## seperating the window  to avoid immediate close after joining
    opt.add_experimental_option("detach",True)
    opt.add_argument("--disable-logging")
    opt.add_argument("--log-level=2")
    opt.add_argument("--disable-in-process-stack-traces")
    
    driver = webdriver.Chrome(options=opt,executable_path=r" ") # Enter the absolute path of the chrome driver
    time.sleep(2)
    #driver.get("https://meet.google.com/"+links)
    driver.get("https://accounts.google.com/ServiceLogin/identifier?ltmpl=meet&osid=1&continue=https%3A%2F%2Fmeet.google.com%2F" +links+ "%3Fhs%3D196&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
    time.sleep(2)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys(email)
    time.sleep(2)
    ## Next Button:
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/span").click()
    time.sleep(3)
    ##Password:
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)
    time.sleep(3)
    ##next button:
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()

    time.sleep(8)
    ##opening Meet:
    ##Mic
    mic=driver.find_element_by_xpath("/html//div[@id='yDmH0d']/c-wiz/div[@class='T4LgNb']//div[@class='KWIIWd']//div[@class='ZUpb4c']/div[1]//div[@class='ZB88ed']/div[@class='dP0OSd']/div[@class='GKGgdd']/div[@role='button']")
    mic.click()
    time.sleep(2)
    ##Camera
    camera=driver.find_element_by_xpath("/html//div[@id='yDmH0d']/c-wiz/div[@class='T4LgNb']/div[@class='kFwPee']//div[@class='KWIIWd']//div[@class='ZUpb4c']/div[1]//div[@class='GOH7Zb']/div[@class='GKGgdd']/div[@role='button']")
    camera.click()
    time.sleep(2)
    ##Join
    join=driver.find_element_by_xpath("/html//div[@id='yDmH0d']/c-wiz/div[@class='T4LgNb']/div[@class='kFwPee']//div[@class='KWIIWd']//div[@class='KieQAe']/div[2]//div[@class='jtn8y']/div[@class='XCoPyb']/div[1]")
    join.click()
   

def getTodayClass():
    TodayTime = datetime.datetime.now()
    Current_Day=TodayTime.strftime("%A")
    CurrentTime=float(TodayTime.strftime("%H.%M"))
    ##Class Time Table
    Days={
    "Monday":   {09.13:"PANLAB", 10.13:"PANLAB", 11.13:"SLS", 12.13:"JTS", 13.53:"PAN", 14.43:"VNT",15.33:"JTS"},
    "Tuesday":  {09.13:"VNT",    10.13:"JTS",    11.13:"PHK", 12.13:"PRP", 13.53:"FLV", 14.43:"PAN",15.33:"PGA"},
    "Wednesday":{09.13:"VNT",    10.13:"VNT",    11.13:"PHK", 12.13:"PRP", 13.53:"FLV", 14.43:"JYS",15.33:"SLS"},
    "Thursday": {09.13:"MTK",    10.13:"MTK",    11.13:"PAN", 12.13:"PHK", 13.53:"VNT", 14.43:"RJR",15.33:"RJR"},
    "Friday":   {09.13:"PAN",    10.13:"JTS",    11.13:"PGA", 12.13:"PRP", 13.53:"FLV", 14.43:"JTS",15.33:"JTS"}
    }
    ##Teacher's Name, Subject Name And Meeting links
    teachersNameAndSubject={
    "JTS":["Jeetu Singh","Artificial intelligence","kgi-djtq-xhy"],
    "JYS":["Jaya Sharma","Comprehension","vnt-xkyy-mps"],
    "MTK":["Muthumum M","MOOC-II","nkr-yibe-hrh"],
    "PAN":["Pramod Nagar","Compiler Design","xhm-nzjw-ocv"],
    "PANLAB":["Pramod Nagar","Compiler Design-Lab","daa-mwys-pei"],
    "PGA":["Parag Assht","Employability Skills & Practices","hnj-vpqu-drm"],
    "PHK":["Piyush Kaala","Energy Conservation","hsw-qoqq-unn"],
    "RJR":["Rajesh Rathnam","Competitive Professional Skills-III","rae-dspp-wft"],
    "SLS":["Shalini Sharma","Indian Art Form","qum-sgyp-art"],
    "FLV":["Franklin Vinod","Network Security","dcx-pcry-mso"],
    "PRP":["Pritee Parwekar","Wireless Sensor Networks","qaw-jnph-qis"],
    "VNT":["Vinam Tomar","Database Management System","pzg-edui-wti"]
    }
    
    if Current_Day=="Sunday" or Current_Day=="Saturday":
        return "No Class Today"
        
    else:
        print(CurrentTime)
        Todayclass=Days[Current_Day].get(CurrentTime) ## getting current class teacher name  
        Name=teachersNameAndSubject[Todayclass][0].upper() ## getting teacherfull name 
        Subject=teachersNameAndSubject[Todayclass][1].upper()##getting Subject name
        links=teachersNameAndSubject[Todayclass][2]  ## getting current class meeting link
        print(Subject)
        print(Name)
        print("https://meet.google.com/"+links)
        playsound(" ") # Enter the absolute path of the audio file
        print("-------------------Joining Class-------------------")
        OnlineClassBot(links)
        time.sleep(60)
        CheckTime = CurrentTime
        ##  prevent to open multiple Browser window
        while (CurrentTime == CheckTime):
            AltTime = datetime.datetime.now()
            CheckTime=float(AltTime.strftime("%H.%M"))
            time.sleep(20)
        classScheduler()       


scheduler1 = schedule.Scheduler()
scheduler2 = schedule.Scheduler()
scheduler3 = schedule.Scheduler()
scheduler4 = schedule.Scheduler()
scheduler5 = schedule.Scheduler()
scheduler6 = schedule.Scheduler()
scheduler7 = schedule.Scheduler()

def classScheduler():
    while True:
        AltTime = datetime.datetime.now()
        CheckTime=float(AltTime.strftime("%H.%M"))
        ## condition to prevent to open same links multiple time
        if CheckTime<=09.13:
            scheduler1.run_pending()
        elif CheckTime<=10.13:    
            scheduler2.run_pending()
        elif CheckTime<=11.13:
            scheduler3.run_pending()
        elif CheckTime<=12.13:
            scheduler4.run_pending()
        elif CheckTime<=13.53:
            scheduler5.run_pending()
        elif CheckTime<=14.43:
            scheduler6.run_pending()
        elif CheckTime<=15.33:
            scheduler7.run_pending()
        time.sleep(1)

scheduler1.every().day.at("09:13").do(getTodayClass)
scheduler2.every().day.at("10:13").do(getTodayClass)
scheduler3.every().day.at("11:13").do(getTodayClass)
scheduler4.every().day.at("12:13").do(getTodayClass)
scheduler5.every().day.at("13:53").do(getTodayClass)
scheduler6.every().day.at("14:43").do(getTodayClass)
scheduler7.every().day.at("15:33").do(getTodayClass)

classScheduler()

