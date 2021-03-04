#!/usr/bin/env python3
"""
    Part 1 of challenge
"""
import json
from selenium import webdriver


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
        elem = browser.find_element_by_css_selector('#searchFor')
        elem.send_keys(form)
        elem.send_keys(Keys.RETURN)

        #picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(2) > td.LeftCellSpacer
        selector = '#picklistContentPane > div.picklistTable > table > tbody > tr:nth-child(' + str(i) + ')'
        selected = find_element_by_css_selector(selector)
        for s in selected:
            print(s)
        '''
        while (1):
            try:
                browser.find_element_by_link_text('Next »').click()
                cells = browser.find_elements_by_css_selector("#ctl00_ContentPlaceHolder1_GridView1 > tbody > tr > td:nth-child(7)")
                [addresses.append(x.text) for x in cells if x.text != ' ']
            except:
                break

        d = dict()
        ret.append(d.update({'form_number': form, 'form_title': '', 'min_year': -1, 'max_year': -1}))
        '''

if __name__ == '__main__':
    form = 'Form W-2'
    information(form)