from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get(" https://witty-hill-0acfceb03.azurestaticapps.net/periodic_table.html")
    time.sleep(2)

    def locator_by_xpath(xp):
        element = driver.find_element_by_xpath(xp)
        return element

    with open("data.txt", "r", encoding="utf-8") as file:
        result = file.read()

    print(result)

    elements = driver.find_elements_by_xpath('//ul//li')
    elements_text = driver.find_elements_by_xpath('//ul//li//span')
    elements_num = []
    for _ in range(len(elements)):
        if elements[_].get_attribute("class") == "empty":
            continue
        else:
            elements_num.append(elements[_].get_attribute("data-pos"))

    elements_name = []
    for _ in elements_text:
        elements_name.append(_.text)

    full_list = []
    for _ in range(len(elements_name)):
        full_list.append(elements_num[_] + ", " + elements_name[_])
finally:
    driver.close()