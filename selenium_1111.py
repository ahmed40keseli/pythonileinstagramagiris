from instagramuserInfo import username,password
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

class insatgram:
    def __init__(self,username,password):
         self.browser=webdriver.Chrome()
         self.username=username
         self.password=password
    
    def signIn(self):       
         self.browser.get("https://www.instagram.com/accounts/login/")
         time.sleep(4)
        
         usernameinput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
         passwordinput=self.browser.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")    

         usernameinput.send_keys(self.username)
         passwordinput.send_keys(self.password)
         passwordinput.send_keys(Keys.ENTER)
         time.sleep(3)


instgrm = insatgram(username,password)
instgrm.signIn()


