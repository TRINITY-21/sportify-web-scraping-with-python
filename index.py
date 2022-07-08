from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time, json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
driver = webdriver.Chrome(ChromeDriverManager().install())

# website to scrape
website = ("https://open.spotify.com/artist/2jzc5TC5TVFLXQlBNiIUzE")
path = 'C:/Users/User/Downloads/chromedriver/chromedriver'
# # driver = webdriver.Chrome(path)

driver.get(website)
see_more_class ="//div[@class='Type__TypeElement-goli3j-0 dhAODk']"

# see_more_element = driver.find_element(By.XPATH, "//div[@class='Type__TypeElement-goli3j-0 dhAODk']")
# print('seeee morreeee', see_more_element)

see_more_element = driver.execute_script("arguments[0].click();", WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='Type__TypeElement-goli3j-0 dhAODk']"))))

time.sleep(15)
body_html = driver.find_element(By.TAG_NAME, "html")
html = body_html.get_attribute('innerHTML')


soup=BeautifulSoup(html, 'html.parser')
print(soup.prettify())


with open('test.html', 'w') as a:
  json.dump(html, a)

# from selenium import webdriver

# options = webdriver.ChromeOptions()
# options.add_argument("start-maximized")
# options.add_argument("--auto-open-devtools-for-tabs")
# options.add_experimental_option("excludeSwitches", ["enable-automation"])
# options.add_experimental_option('useAutomationExtension', False)
# driver = webdriver.Chrome(options=options, executable_path=path)
# driver.get(website)

# time.sleep(10)

# body_html = driver.find_element(By.XPATH, "/html/body")
# # print (body_html.text)
# # print (body_html.get_attribute("innerHTML"))
# soup=BeautifulSoup(body_html.get_attribute("innerHTML"), 'html.parser')
# print(soup.prettify())

time.sleep(1500)
