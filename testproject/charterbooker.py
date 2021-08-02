"""
A program töltse be a charterbooker app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html
oldalról.

Feladatod, hogy automatizáld selenium webdriverrel a charterbooker app tesztelését.

Az ellenőrzésekhez NEM kell teszt keretrendszert használnod (mint pl a pytest).
Egyszerűen használj elágazásokat vagy assert összehasonlításokat.

Teszteld le a többoldalas formanyomtatvány működését.
Ellenőrizd a helyes kitöltésre adott választ: "Your message was sent successfully.
Thanks! We'll be in touch as soon as we can, which is usually like lightning (Unless we're sailing or eating tacos!)."
Készíts tesztesetet az e-mail cím validációjára.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.support.ui import Select
from datetime import datetime

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/charterbooker.html")
    time.sleep(2)

    def locator_by_xpath(xp):
        element = driver.find_element_by_xpath(xp)
        return element

    def clear_n_fill_input_field(xp, test_data):
        locator_by_xpath(xp).clear()
        locator_by_xpath(xp).send_keys(test_data)


    # fields
    select_xp = '//select[@name="bf_totalGuests"]'
    next_btn_xp = '//button[@class="next-btn next-btn1"]'
    next_btn2_xp = '//button[@class="next-btn next-btn2"]'
    date_xp = '//input[@class="datepicker"]'
    select2_xp = '//select[@name="bf_time"]'
    select3_xp = '//select[@name="bf_hours"]'
    full_name_xp = '//input[@name="bf_fullname"]'
    email_xp = '//input[@name="bf_email"]'
    submit_xp = '//button[@class="submit-btn"]'
    msg = "Your message was sent successfully. Thanks! We'll be in touch as soon as we can, which is usually like " \
          "lightning (Unless we're sailing or eating tacos!)."

    date = datetime(2021, 8, 12, 12, 45)

    select = Select(driver.find_element_by_xpath(select_xp))
    option = select.select_by_value('7')
    driver.find_element_by_xpath(next_btn_xp).click()
    time.sleep(3)
    driver.find_element_by_xpath(date_xp).send_keys(date.strftime('%Y-%m-%d-%I:%M'))
    select2 = Select(driver.find_element_by_xpath(select2_xp))
    option2 = select2.select_by_value('Morning')
    select3 = Select(driver.find_element_by_xpath(select3_xp))
    option3 = select3.select_by_value('4')
    driver.find_element_by_xpath(next_btn2_xp).click()
    time.sleep(3)
    driver.find_element_by_xpath(full_name_xp).send_keys('József Attila')
    driver.find_element_by_xpath(email_xp).send_keys('jozsef@gmail.com')
    driver.find_element_by_xpath(submit_xp).click()
    time.sleep(3)
    assert driver.find_element_by_tag_name('h2').text == msg
finally:
    driver.close()
