from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
import re
import requests
try:
	def likho(kya):
		a = open('links.txt', 'a')
		a.write(kya)
		a.close()
	def doubleclick(browser,element):
		action = ActionChains(browser) 
		action.double_click(on_element = element) 
		action.perform()
	def getthelinks(browser):
		li=[]
		titles=[]
		try:
			titlescount=len(browser.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div/div'))
			for i in range(titlescount):
				element=browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div/div/div['+str(i+1)+']/div/div/h4')
				titles.append(element.get_attribute('innerHTML'))
		except Exception as e:
			print(e)
		finally:
			pass
		#print(titles)
		t=browser.page_source
		t=str(t)
		check="https://player.vimeo.com/video/"
		
		res = [i for i in range(len(t)) if t.startswith(check, i)]
		#print(res)
		for i in range(len(res)):
			li.append(check+t[res[i]+31:res[i]+40])
		print(li)
		for i in range(len(li)):
			likho(titles[i]+"\t"+li[i]+"\n")
			
			
			
	def scroll_shim(browser,element):
		x =element.location['x']
		y =element.location['y']
		scroll_by_coord = 'window.scrollTo(%s,%s);' % (x,y)
		scroll_nav_out_of_way = 'window.scrollBy(0, -120);'
		browser.execute_script(scroll_by_coord)
		browser.execute_script(scroll_nav_out_of_way)

	browser = webdriver.Firefox()
	browser.get('http://www.pesuacademy.com')
	input('Press enter after website loads')
	elem = browser.find_element_by_name('j_username')
	elem.send_keys(input('Enter your Username :\n'))
	elem = browser.find_element_by_name('j_password')
	elem.send_keys(input('Enter your Password :\n'))
	sleep(1)  
	element = browser.find_element_by_id('postloginform#/Academy/j_spring_security_check')
	doubleclick(browser,element)
	input("Press Enter after logging in")
	element = browser.find_element_by_xpath('/html/body/div[3]/div[1]/ul/li[2]/a/span[2]')
	doubleclick(browser,element)
	input("Press Enter after my courses appear")
	for i in range(len(browser.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/tr') )):
		ele=browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/tr['+str(i+1)+']/td[2]')
		print(i+1,".",ele.get_attribute("innerHTML"))
	arr1=list(map(int,input("Enter the topic numbers (sep by \" \")\n").split()))
	for i in arr1:
		ele=browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div/div[2]/div/div[3]/div/table/tbody/tr['+str(i)+']/td[2]')
		print("Opening the course",ele.get_attribute("innerHTML"))
		scroll_shim(browser,ele)
		doubleclick(browser,ele)
		input("Press Enter after the page loads")
		print("Opening all links under unit 1(one after the other)")
		arr2=list(range(len(browser.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div'))))
		for j in arr2:
			ele1 = browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[2]/div[2]/div[1]/div/div/div/div['+str(j+1)+']')
			scroll_shim(browser,ele1)
			doubleclick(browser,ele1)
			input("Press Enter after the page loads")
			getthelinks(browser)
			input("Links retrived, press Enter to continue")
			browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/a[2]').click()
			input("Press Enter after the page loads")
		input(arr2)
		browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/div[1]/a[1]').click()
		input("Press Enter after the page loads")
		
except Exception as e:
	print(e)
input("Press Enter to log out")
browser.find_element_by_xpath('/html/body/nav/div/header/div/div[2]/ul/li/a/span[2]').click()
sleep(5)
browser.find_element_by_xpath('/html/body/nav/div/header/div/div[2]/ul/li/ul/li[3]/a').click()
input("Press Enter to after logging out")
print("Exiting") 
browser.quit() 
print("Finished")

#browser.quit()

