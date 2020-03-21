from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=r"C:\Users\spars\OneDrive\Desktop\chromedriver.exe")

#Login
br = driver.get('http://54.235.233.16/')
sr = driver.find_element_by_id('logemail')
sr.send_keys("amazonaniruddha123@gmail.com")
pk = driver.find_element_by_id('logpsk')
pk.send_keys("University@99")
driver.find_element_by_name('login').click()

#Register
#driver.find_element_by_id('signfirstname').send_keys("Sparsh")
#driver.find_element_by_id('signsurname').send_keys("Amit")
#driver.find_element_by_id('signemail').send_keys("sparshamit1227@gmail.com")
#driver.find_element_by_id('signpassword').send_keys("sparshbhai")
#driver.find_element_by_id('signday').send_keys("27")
#driver.find_element_by_id('signmonth').send_keys("Dec")
#driver.find_element_by_id('signyear').send_keys("1999")
#gen = "Male"
#if(gen=="Male"):
#    driver.find_element_by_id('signgender1').click()
#elif(gen=="Female"):
#    driver.find_element_by_id('signgender2').click()
#else:
#    driver.find_element_by_id('signgender3').click()
#driver.find_element_by_name('register').click()
