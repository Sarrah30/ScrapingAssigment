from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import sys

contestnumber= sys.argv[1]

PATH = 'C:\Program Files (x86)\chromedriver.exe'
driver = webdriver.Chrome(PATH)
driver.get('https://codeforces.com/problemset')

text=driver.find_element_by_class_name('problems').text
def textlist(text):
    return [str(s) for s in text.split() if s.isalnum()==True and s.isalpha()==False]

def check(text,s):
    if (text.find(s)==-1):
        return False
    else:
        return True

def problemslist(text,contestnumber):
    A= textlist(text)
    B=[]
    for i in range(len(A)):
        if check(A[i],contestnumber)==True and A[i].isdigit()==False:
            B.append(A[i])
    return B


def convert(s):
    str1 = ""
    return (str1.join(s))

def problemlabel(l):
    for i in range(len(l)):
        a=list(l[i])
        j=0
        while j<len(a):
            if a[j].isdigit()==False:
                a=a[j:]
                j=len(a)+1
            else:
                j+=1
            l[i]= convert(a)
    return l

problemlabellist=problemlabel(problemslist(text,contestnumber))
problemurls=['https://codeforces.com/problemset/problem/{}/{}'.format(contestnumber,problemlabellist[i]) for i in range(len(problemlabellist))]

def navigatetopage(problemlabellist):
    driver2=webdriver.Chrome(PATH)
    i=0
    while i < len(problemlabellist):
        os.makedirs('./{}/{}'.format(contestnumber,problemlabellist[i]))
        driver2.get(problemurls[i])
        driver2.save_screenshot('./{}/{}/problem.png'.format(contestnumber,problemlabellist[i]))
        inputinfo=driver2.find_element_by_class_name('input')
        inputtext= inputinfo.find_element_by_xpath('.//pre').text
        with open('./{}/{}/input1.txt'.format(contestnumber,problemlabellist[i]),'w') as f:
            f.write(inputtext)
        outputinfo=driver2.find_element_by_class_name('output')
        outputtext=outputinfo.find_element_by_xpath('.//pre').text
        with open('./{}/{}/output1.txt'.format(contestnumber,problemlabellist[i]),'w') as g:
            g.write(outputtext)
        i+=1

navigatetopage(problemlabellist)
