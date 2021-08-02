"""
A program töltse be a sales Film register app-ot az https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html
oldalról.
Feladatod, hogy automatizáld az alkalmazás két funkciójának a tesztelését
Teszteld le, hogy betöltés után megjelennek filmek az alkalmazásban, méghozzá 24 db.
Teszteld le, hogy fel lehet-e venni az alábbi adatokkal egy új filmet:
Film title: Black widow
Release year: 2021
Chronological year of events: 2020
Trailer url: https://www.youtube.com/watch?v=Fp9pNPdNwjI
Image url: https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg
Film summary: https://www.imdb.com/title/tt3480822/
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/film_register.html")
    time.sleep(6)

    def locator_by_xpath(xp):
        element = driver.find_element_by_xpath(xp)
        return element

    def locators_by_xpath(xp):
        elements = driver.find_elements_by_xpath(xp)
        return elements

    def all_movies_list(my_list):
        all_movies = locators_by_xpath(all_movies_xp)
        for _ in range(len(all_movies)):
            my_list.append(all_movies[_].get_attribute("src"))

    # fields
    all_movies_xp = '//a//div//img'

    # TC01 - betöltés után megjelennek filmek az alkalmazásban, 24 db
    locators_by_xpath(all_movies_xp)
    movies = []
    all_movies_list(movies)
    assert len(movies) == 24

    # TC02 - új film felvitele
    # test data
    test_data = ["Black widow", "2021", "2020", "https://www.youtube.com/watch?v=Fp9pNPdNwjI",
                 "https://m.media-amazon.com/images/I/914MHuDfMSL._AC_UY327_FMwebp_QL65_.jpg",
                 "https://www.imdb.com/title/tt3480822/"]

    driver.find_element_by_tag_name('button').click()
    time.sleep(5)
    input_fields = driver.find_elements_by_tag_name('input')
    save_btn_xp = '//button[contains(text(),"Save")]'

    for _ in range(len(test_data)):
        input_fields[_].send_keys(test_data[_])
    locator_by_xpath(save_btn_xp).click()

    time.sleep(5)
    movies = []
    all_movies_list(movies)
    assert len(movies) == 25
finally:
    driver.close()
