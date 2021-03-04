#!/usr/bin/env python3
"""
    Part 2 of challenge
"""
import json
import os
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def download_forms(form, min_year, max_year):
    """
        Taking a tax form name (ex: "Form W-2") and a range of years (inclusive, 2018-2020
        should fetch three years), download all PDFs available within that range. The forms
        returned should be an exact match for the input (ex: "Form W-2" should not return "Form
        W-2 P", etc.) The downloaded PDFs should be downloaded to a subdirectory under your
        script's main directory with the name of the form, and the file name should be the "Form
        Name - Year" (ex: Form W-2/Form W-2 - 2020.pdf)
    """
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser = webdriver.Chrome(options=op)

    browser.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
    elem = browser.find_element_by_css_selector('#searchFor')
    elem.send_keys(form)
    elem.send_keys(Keys.RETURN)

    while (1):
        try:
            for i in range(2, 27):
                product = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(i) + ') > td.LeftCellSpacer'
                product = browser.find_element_by_css_selector(product)
                year = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(i) + ') > td.EndCellSpacer'
                year = int(browser.find_element_by_css_selector(year).text)

                link = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(i) + ') > td.LeftCellSpacer > a'
                link = browser.find_element_by_css_selector(link).get_attribute('href')
                if product.text == form:
                    if int(year) >= min_year and int(year) <= max_year:
                        r = requests.get(link, allow_redirects=True)
                        fn = form + ' - ' + str(year) + '.pdf'
                        dirname = './' + form
                        #dirname = dirname.replace(' ', '_')
                        if not os.path.exists(dirname):
                            print('MAKING DIRECTOREEEEE')
                            os.makedirs(dirname)
                        filename = dirname + '/' + fn
                        #filename = filename.replace(' ', '_')
                        print(filename)
                        open(filename, 'wb').write(r.content)

            browser.find_element_by_link_text('Next »').click()
        except Exception as e:
            #print("exception!!!, {}".format(e))
            break
    print("Script finished")

if __name__ == '__main__':
    form = 'Form W-2'
    min_year = 1990
    max_year = 2000
    download_forms(form, min_year, max_year)
