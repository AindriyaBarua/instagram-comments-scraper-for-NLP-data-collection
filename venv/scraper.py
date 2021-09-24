"""
Developed by Aindriya Barua.
Python Version : 3.8.1 64-bit.

This file makes the web driver, scraps comments from the given link
"""

from selenium import webdriver
import time
import sys
from selenium.common.exceptions import NoSuchElementException
import re

import constants
import output_writer

driver = None

def make_driver():
    global driver
    opt = webdriver.ChromeOptions()
    opt.add_argument(constants.CHROME_OPT_DISABLE_GPU)
    driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=opt)
    return driver


def scraper_main(link): 
    global driver
    scrap_link(link)
    comment_container_contents = get_container_contents()
    comments = get_comments(comment_container_contents)
    return comments


def manual_login():
    global driver
    driver.get(constants.INSTAGRAM_HOME)
    time.sleep(20)


def scrap_link(link):
    global driver
    driver.get(link)
    time.sleep(3)


def check_exists_by_xpath(xpath):
    global driver
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

def load_all_comments():
    global driver
    print("Loading all comments...")
    c= 0
    while check_exists_by_xpath(constants.LOAD_MORE_COMMENTS_XPATH):
        c = c+1
        load_more_comments_element = driver.find_element_by_xpath(constants.LOAD_MORE_COMMENTS_XPATH)
        load_more_comments_element.click()
        time.sleep(2)
    print("No of Load more clicks: ", c)
    time.sleep(2)

def get_container_contents():
        global driver
        load_all_comments()
        comment_container_contents = driver.find_elements_by_class_name(constants.COMMENT_CONT_CLASSNAME)
        return comment_container_contents

def get_comments(comment_container_contents):
    count = 0
    comments = []
    for c in comment_container_contents:
        comment = c.text.split('\n')[1:-1]
        whole_comment = ''
        if len(comment) > 1:
            for part in comment:
                whole_comment = whole_comment + ' ' + part
        else:
            whole_comment = comment[0]
        whole_comment = whole_comment.strip()
        whole_comment = re.sub(' +', ' ', whole_comment)
        # Remove identical comments
        if whole_comment not in comments:
            comments.append(whole_comment)
            count = count + 1
    print(count, " comments scrapped \n")
    # remove caption
    if len(comments) > 0:
        comments.pop(0)

    return comments


        

        