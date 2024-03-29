#!/usr/bin/env python3
#encoding=utf-8
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options
import pandas as pd
import sys
import os


def submit(username, password):
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--blink-settings=imagesEnabled=false')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    browser = webdriver.Chrome(options=chrome_options)
    browser.implicitly_wait(10)
    browser.get("http://yqtb.nwpu.edu.cn/wx/xg/yz-mobile/index.jsp")
    browser.find_element_by_id("username").send_keys(username)
    browser.find_element_by_id("password").send_keys(password)
    browser.find_element_by_name("submit").click()
    sleep(3)
    file_object = open("login.html", "w")
    html = browser.page_source
    file_object.write(html)
    file_object.close()
    browser.find_element_by_xpath('//a[@href="/wx/ry/jrsb_js.jsp"]').click()
    submitted_title = browser.find_element_by_class_name('page__title')
    browser.find_element_by_link_text('提交填报信息').click()
    checkbox = browser.find_element_by_xpath('//input[@type="checkbox"]')
    checkbox = browser.find_element_by_class_name('weui-check')
    checkbox = browser.find_element_by_class_name('weui-cells_checkbox')
    checkbox.click()
    browser.find_element_by_id('save_div').click()
    print('提交成功')


def main():
    # df = pd.read_csv(os.getcwd()+"/namelist.csv")
    # for idx, row in df.iterrows():
    #     print(row['ID'], row['password'])
    #     submit(row['ID'], row['password'])
    submit("2018300410", "q1w2e3r4314159")
if __name__ == "__main__":
    main()

