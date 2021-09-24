"""
Developed by Aindriya Barua.
Python Version : 3.8.1 64-bit.

This is the starting point of the project which has to be run. It calls the file reader, scraper, output writer
"""


import sys
import mass_links_scraper
import pandas as pd
import re

import constants
import output_writer
import scraper

def mass_scraper_main(links_file):
    links = read_links_file(links_file)
    driver = scraper.make_driver()
    # If we are not logged in, we can't load more comments
    scraper.manual_login()
    comments = []
    for link in links:
        link = str(link).strip()
        if link is not None and '\n' != link:
            if(re.match(r'^' + constants.VALID_IG_LINK ,str(link))):
                print("Scraping... " + link)
                comments.append('\n')
                comments.append(link)
                comments.append('\n')
                link_comments = scraper.scraper_main(link)
                comments += link_comments
    
    driver.close()
    output_writer.write_output(comments)


def read_links_file(links_file):
    xl = pd.ExcelFile(links_file)
    df = xl.parse(constants.INPUT_SHEET_NAME, index=False)
    links = df[constants.LINKS_COLUMN_NAME].to_list()
    return links

if __name__ == '__main__':
    links_filepath = constants.INPUT_FILENAME
    mass_scraper_main(links_filepath)
    
