from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


driver = webdriver.Chrome()

driver.get("https://www.google.com")

time = 2

sleep(time)

barraGoogle = driver.find_element(By.NAME, "q")
barraGoogle.send_keys("PontoJob")
barraGoogle.send_keys(Keys.RETURN)

sleep(time)

first_result = driver.find_element(By.XPATH, '//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/div/span/a')
first_result.click()

sleep(time)

userPontoJob = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[1]/div/input')
userPontoJob.send_keys("10528154990")
userPontoJob.send_keys(Keys.RETURN)

senhaPontoJob = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[2]/div/div[2]/div/input')
senhaPontoJob.send_keys("danimon159!")

clickAcessar = driver.find_element(By.XPATH, '//*[@id="root"]/div[1]/div/div/div/div/div/div/div/div/div[3]/button')
clickAcessar.click()

sleep(time)

driver.quit()
