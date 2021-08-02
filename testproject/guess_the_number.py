"""
A program töltse be a Guess the number app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html
 oldalról.

Feladatod, hogy automatizáld selenium webdriverrel az app funkcionalitását tesztelését.

Egy tesztet kell írnod ami addig találgat a megadott intervallumon belül amíg ki nem találja a helyes számot.
Nem jár plusz pont azért ha úgy automatizálsz, hogy minnél optimálisabban és gyosabban találja ki a helyes számot
a program

Amikor megvan a helyes szám, ellenőrizd le, hogy a szükséges lépések száma mit az aplikáció kijelez egyezik-e a saját
belső számlálóddal.

Teszteld le, hogy az applikáció helyesen kezeli az intervallumon kívüli találgatásokat. Az applikéció -19 vagy 255
értéknél nem szabad, hogy összeomoljon. Azt kell kiírnia, hogy alá vagy fölé találtál-e.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/guess_the_number.html")
    time.sleep(2)

    def locator_by_xpath(xp):
        element = driver.find_element_by_xpath(xp)
        return element

    def clear_n_fill_input_field(xp, test_data):
        locator_by_xpath(xp).clear()
        locator_by_xpath(xp).send_keys(test_data)


    # fields
    guess_btn = driver.find_element_by_xpath('//button[contains(text(), "Guess")]')
    restart_btn = driver.find_element_by_xpath('//button[contains(text(), "Restart")]')
    ok_message = driver.find_element_by_xpath('//p[contains(text(), "Yes! That is it.")]')
    alert_message_higher = driver.find_element_by_xpath('//p[contains(text(), "Guess higher.")]')
    alert_message_lower = driver.find_element_by_xpath('//p[contains(text(), "Guess lower.")]')
    number_of_guesses = driver.find_element_by_xpath('//p[@class="text-info"]//span')

    # TC01
    index = 0
    for index, value in enumerate(range(1, 101)):
        driver.find_element_by_tag_name('input').send_keys(value)
        guess_btn.click()
        driver.find_element_by_tag_name('input').clear()
        index += 1
        if ok_message.is_displayed():
            guesses_num = number_of_guesses.text
            assert index == int(guesses_num)
            break

    time.sleep(2)

    # TC02
    # test data
    a = -19
    b = 255
    expected_text_higher = 'Guess higher.'
    expected_text_lower = 'Guess lower.'

    def fill_n_assert(num, alert, exp):
        restart_btn.click()
        time.sleep(2)
        driver.find_element_by_tag_name('input').send_keys(num)
        guess_btn.click()
        assert alert.text == exp
        time.sleep(2)


    fill_n_assert(a, alert_message_higher, expected_text_higher)
    fill_n_assert(b, alert_message_lower, expected_text_lower)
finally:
    driver.close()
