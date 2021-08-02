"""
A Marvel új web alapú rajongó oldalt készít az X-man képregény adaptációkból.
Itt találod a webes applikáció prototípusát:(https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html)

Teszteld le, hogy a különböző szűrőfeltételek alapján megfelelő karaktereket mutatja az oldal.

Tehát mondjuk `iceman` pontosan az `original` és a `factor` csapatban van benne és a `hellfire` illetve a `force`
csapatokban nincs benne.
(Figyelem: ne engedd, hogy az oldal dinamikus működése elvonja a figyelmed a célról!
A karaktereket csoporthoz tartozását nem feltétlenül a felület változásával tudod ellenőrizni.)
Al alkalmazás helyesen mutatja a felületen a csoporthoz tartozást. Nincs külön tesztadat leírás ehhez a feladathoz,
tehát a látottak alapáj kell a tesztadatot összeállítanod.
"""
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

options = Options()
options.headless = False

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)

try:
    driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/mutant_teams.html")
    time.sleep(2)

    def locators_by_xpath(xp):
        elements = driver.find_elements_by_xpath(xp)
        return elements

    def locator_by_xpath(xp):
        element = driver.find_element_by_xpath(xp)
        return element


    # fields, test_data
    original_x_man_label_xp = '//label[@for="original"]'
    x_force_label_xp = '//label[@for="force"]'
    x_factor_label_xp = '//label[@for="factor"]'
    hellfire_club_label_xp = '//label[@for="hellfire"]'
    all_characters_xp = '//ul//h2'
    expected_original_xman_group = ['Angel', 'Beast', 'Cyclops', 'Iceman', 'Jean Grey', 'Professor X']
    expected_x_force_group = ['Angel', 'Cyclops', 'Nightcrawler', 'Psylocke', 'Rictor', 'Storm', 'Sunspot', 'Wolverine']
    expected_x_factor_group = ['Angel', 'Beast', 'Cyclops', 'Iceman', 'Jean Grey', 'Quicksilver', 'Rictor']
    expected_hellfire_club_group = ['Angel', 'Emma Frost', 'Magneto', 'Psylocke', 'Storm', 'Sunspot', 'Tithe']


    def characters_of_group(my_list):
        all_char = locators_by_xpath(all_characters_xp)
        for _ in range(len(all_char)):
            if all_char[_].text == "":
                continue
            else:
                my_list.append(all_char[_].text)


    locator_by_xpath(original_x_man_label_xp).click()
    original_x_man_group = []
    characters_of_group(original_x_man_group)
    assert original_x_man_group == expected_original_xman_group
    time.sleep(1)

    locator_by_xpath(x_force_label_xp).click()
    x_force_group = []
    characters_of_group(x_force_group)
    assert x_force_group == expected_x_force_group
    time.sleep(1)

    locator_by_xpath(x_factor_label_xp).click()
    x_factor_group = []
    characters_of_group(x_factor_group)
    assert x_factor_group == expected_x_factor_group
    time.sleep(1)

    locator_by_xpath(hellfire_club_label_xp).click()
    hellfire_club_group = []
    characters_of_group(hellfire_club_group)
    assert hellfire_club_group == expected_hellfire_club_group
finally:
    pass
    # driver.close()
