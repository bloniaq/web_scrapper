from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

starter_url = 'http://185.40.115.250/'
req_line = 'A'

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.implicitly_wait(30)
driver.get(starter_url)
# go to schedules
driver.find_element_by_xpath('//*[@id="tab2Nav"]').click()
# pick a line
driver.find_element_by_xpath("//*[@id='dvTab2RoutesContent']/input" +
                             "[@type='button'][@routenum='" +
                             req_line + "']").click()
# expand directions menu
time.sleep(2)
driver.find_element_by_xpath('//*[@id="dvTab2Directions"]/table/tbody/' +
                             'tr/td[2]/div/button').click()
# wait
time.sleep(2)

line_dirs = []
# get directions names
line_dirs_names = driver.find_elements_by_xpath(
    '//*[@id="dvTab2Directions"]/table/tbody/tr/td[2]/div/div/ul/li/a/' +
    'span[@class="text"]')
# get childs text
line_dirs_from_to = driver.find_elements_by_xpath(
    '//*[@id="dvTab2Directions"]/table/tbody/tr/td[2]/div/div/ul/li/a/' +
    'span[@class="text"]/small/div')
# replace redunant text by ""
for i in range(len(line_dirs_names)):
    line_dirs.append(line_dirs_names[i].text.replace(
        "\n" + line_dirs_from_to[i].text, ""))

# fold directions menu
driver.find_element_by_xpath(
    '//*[@id="dvTab2Directions"]/table/tbody/tr/td[2]/div/button').click()
# loop thru directions
for direction in line_dirs:
    print("\n\nkierunek: <", direction, ">\n")
    time.sleep(2)
    # expand list of directions
    driver.find_element_by_xpath(
        '//*[@id="dvTab2Directions"]/table/tbody/tr/td[2]/div/button').click()
    # find direction name in list
    text_el = driver.find_element_by_xpath(
        '//span[contains(text(), "{0}")]'.format(direction))
    # click on grandparent
    text_el.find_element_by_xpath('../..').click()
    time.sleep(2)
    # make bus stops list
    stops_list = driver.find_elements_by_xpath(
        '//table[@class="route-track-table"]/tr/td[@class="td2"]')
    for i in stops_list:
        print(i.text)
    time.sleep(2)
driver.quit()
