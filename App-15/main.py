from selenium import webdriver
from dotenv import load_dotenv
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

load_dotenv()
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

chrome_options = Options()
chrome_options.add_argument("--disable-search-engine-choice-screen")

prefs = {'download.default_directory': os.getcwd()}
chrome_options.add_experimental_option("prefs", prefs)

service = Service("chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(options=chrome_options, service=service)
driver.get("https://demoqa.com/login")
username_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'userName')))
password_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'password')))

username_field.send_keys(username)
password_field.send_keys(password)

login_button = driver.find_element(By.ID, 'login')
driver.execute_script("arguments[0].click();", login_button)

elements = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div/div[1]/div/div/div[1]/span/div')))
elements.click()

textbox = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="item-0"]')))
textbox.click()

fullname_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'userName')))
email_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'userEmail')))
curr_addr_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'currentAddress')))
perm_addr_field = WebDriverWait(driver, 3).until(EC.visibility_of_element_located((By.ID, 'permanentAddress')))

#Fill in the details
fullname_field.send_keys("Sampreeth")
email_field.send_keys("twst@domain.ext")
curr_addr_field.send_keys("Bangalore")
perm_addr_field.send_keys("Chintamani")

submit_button = driver.find_element(By.ID, 'submit')
driver.execute_script("arguments[0].click();", submit_button)

#Downloads
download = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'item-7')))
download.click()

download_button = driver.find_element(By.ID, 'downloadButton')
driver.execute_script("arguments[0].click();", download_button)


input("Press enter to close")
driver.quit()