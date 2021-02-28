from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys

inputusername= sys.argv[1]
inputPW= sys.argv[2]

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://moodle.iitd.ac.in/login/index.php')

username= driver.find_element_by_id('username')
username.send_keys(inputusername)
password= driver.find_element_by_id('password')
password.send_keys(inputPW)

text=driver.find_element_by_id('login').text
def numbers(str):
    return [int(s) for s in str.split() if s.isdigit()]

def check(text,s):
    if (text.find(s)==-1):
        return False
    else:
        return True

def solvecaptcha(text):
    answer=0
    if check(text,'add')==True:
        answer= numbers(text)[0]+numbers(text)[1]
    elif check(text,'subtract')==True:
        answer=numbers(text)[0]-numbers(text)[1]
    elif check(text,'first') == True:
        answer=numbers(text)[0]
    elif check(text,'second')==True:
        answer=numbers(text)[1]
    return answer

solution=driver.find_element_by_id('valuepkg3')
solution.send_keys(Keys.BACKSPACE)
solution.send_keys(solvecaptcha(text))

loginbutton=driver.find_element_by_id('loginbtn')
loginbutton.send_keys(Keys.RETURN)