#!/usr/bin/env python3
"""
    Part 1 of challenge
"""
import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def information(forms):
    """
        Taking a list of tax form names (ex: "Form W-2", "Form 1095-C"), search the website
        and return some informational results. Specifically, you must return the "Product
        Number", the "Title", and the maximum and minimum years the form is available for
        download. The forms returned should be an exact match for the input (ex: "Form W-2"
        should not return "Form W-2 P", etc.) The results should be returned as json, in the
        format of the following example:

        [
            {
                "form_number": "Form W-2",
                "form_title": "Wage and Tax Statement (Info Copy Only)",
                "min_year": 1954,
                "max_year": 2021
            }
            ...
        ]
    """
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    browser = webdriver.Chrome(options=op)
    browser.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')

    ret = []
    for form in forms:
        browser.get('https://apps.irs.gov/app/picklist/list/priorFormPublication.html')
        elem = browser.find_element_by_css_selector('#searchFor')
        elem.send_keys(form)
        elem.send_keys(Keys.RETURN)

        d = dict()
        year_list = []
        print("Starting...")

        #selector = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(2) + ')'
        #selected = browser.find_element_by_css_selector(selector)
        #print(selected.text)
        #for s in selected:
        #    print(s)
        while (1):
            try:
                #picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(2) > td.LeftCellSpacer
                for i in range(2, 27):
                    product = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(i) + ') > td.LeftCellSpacer'
                    product = browser.find_element_by_css_selector(product)
                    #print("[{}]".format(product.text))
                    title = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(i) + ') > td.MiddleCellSpacer'
                    title = browser.find_element_by_css_selector(title)
                    #print("[{}]".format(title.text))
                    year = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(i) + ') > td.EndCellSpacer'
                    year = browser.find_element_by_css_selector(year)
                    #print("[{}]".format(year.text))
                    #print("form: [{}], product: [{}]\ntitle: [{}], year: [{}]".format(form, product.text, title.text, year.text))
                    if product.text == form:
                        #print("formy: {}".format(title.text))
                        d = dict()
                        #print(65)
                        year_list.append(int(year.text))
                        #print(67)
                        #print('yearlistnow {}'.format(year_list))
                        d.update({'form_number': form, 'form_title': title.text, 'min_year': year_list, 'max_year': -1})
                print("Next page...")
                browser.find_element_by_link_text('Next »').click()
            except Exception as e:
                print('If fail this error might be important: {}'.format(e))
                print("Wrapping up...")
                #d.update({'form_number': form, 'form_title': title.text, 'min_year': year_list, 'max_year': -1})
                if len(d) is not 0:
                    ret.append(d)
                break

    #print("ret is: {}".format(ret))
    for di in ret:
        year_l = di['min_year']
        di['min_year'] = min(year_l)
        di['max_year'] = max(year_l)
    return ret


if __name__ == '__main__':
    forms = ['Form W-2', 'Form W-2 P', 'Doesnt exist']
    filename = 'information.json'
    jayson = information(forms)
    print(jayson)
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(jayson, f)
