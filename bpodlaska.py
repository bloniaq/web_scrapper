import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

starter_url = 'http://185.40.115.250/'
req_line = 'E'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get(starter_url)
# przejdz do rozkładów jazdy
driver.find_element_by_xpath('//*[@id="tab2Nav"]').click()
# wybierz linię
driver.find_element_by_xpath("//*[@id='dvTab2RoutesContent']/input[@type='button'][@routenum='" + req_line + "']").click()
# rozwin menu kierunki
time.sleep(2)
driver.find_element_by_xpath('//*[@id="dvTab2Directions"]/table/tbody/tr/td[2]/div/button').click()
# odczekaj
time.sleep(2)
# zapisz dostępne kierunki HTML
line_directions_code = driver.find_element_by_xpath('//*[@id="dvTab2Directions"]/table/tbody/tr/td[2]/div/div').get_attribute("innerHTML")
# utworz obiekt bs4
soup = BeautifulSoup(line_directions_code, 'lxml')
# pokaz kod html
print(soup.prettify())
# przeszukaj kod html 
line_directions = soup.findAll("span", {"class": 'text'})
# utwórz pustą listę
line_dirs = []
# petla przez znalezione spany
for i in line_directions:
    print(i)
    print(type(i))
    line_dirs.append(i.contents[0])
print(line_dirs)
driver.close()
