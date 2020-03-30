from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
import time
from time import sleep
import sys
from random import random
import threading


driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com/')

x=input("HIT ENTER AFTER SCANNING QR CODE.")

name = input("ENTER THE NAME OF GROUP/CONTACT :")
x=input("IS IT A PINNED CHAT ? (Y/N)")
if(x=='Y'):
	user = driver.find_element_by_xpath('//span/span[@title = "{}"]'.format(name))
	user.click()
else :
	user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
	user.click()
	
print("/////////////////////////////////////////////////////////////////////////////////////////////////////////")
print("WHAT DO YOU WANT TO SEND ?")
print("1.TEXT")
print("2.IMAGE/VIDEO")
print("3.DOCUMENT")
print("/////////////////////////////////////////////////////////////////////////////////////////////////////////")
choice=int(input("CHOICE :"))
count=int(input("ENTER THE NUMBER OF TIMES YOU WANT TO SEND THE MESSAGE :"))

def sendAText():
	msg=input("ENTER YOUR MESSAGE :")
	msg_box = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]')
	for i in range(count):
		msg_box.send_keys(msg)
		button = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button')
		driver.implicitly_wait(10)
		print("Count " , (i+1)) 
		actions = ActionChains(driver)
		actions.move_to_element(button)
		actions.click(button)
		actions.perform()


def sendMoreThanJustText(x,x1,x2,x3):
	attach_button=driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/div')
	attach_button.click()
	pth=input("ENTER PATH :")
	for i in range(count):
		iconb=driver.find_element_by_xpath(x1)
		iconb.click()
		inp = driver.find_element_by_xpath(x2)
		inp.send_keys(pth)
		sleep(2)
		send_button=driver.find_element_by_xpath(x3)
		send_button.click()
			
if(choice==1):
	sendAText()
	

elif(choice==2):			
	sendMoreThanJustText(choice,'/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button','/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[1]/button/input','/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div')	
			
elif(choice==3):
	sendMoreThanJustText(choice,'/html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button','html/body/div[1]/div/div/div[4]/div/header/div[3]/div/div[2]/span/div/div/ul/li[3]/button/input','/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div/span')
	
else:
	print("Wrong Choice.")
  

