#!/bin/python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('http://www.sistemas.pucminas.br/sgaaluno3/SilverStream/Pages/pgAln_LoginSSL.html')
login_sga = driver.find_element_by_name('S33_')
passwd_sga = driver.find_element_by_name('S35_')
orig_sga = driver.find_element_by_name('S39_')

login_sga.send_keys('xxxx')
passwd_sga.send_keys('xxxxx')
orig_sga.send_keys('xxxxx')
driver.find_element_by_name('S55_').click()