"""
Developed by Aindriya Barua.
Python Version : 3.8.1 64-bit.

This file writes the output comments into an excel file
"""

import pandas as pd
from pandas import ExcelWriter
import os.path

import constants

def write_output(comments):
    fname = constants.OUTPUT_FILENAME
    temp = {}
    temp_comments = []
    if os.path.isfile(fname):
        saved = pd.read_excel(fname)
        #temp_names.extend(saved['name'])
        temp_comments.extend(saved[constants.OUTPUT_COLUMN_NAME])
    #temp_names.extend(names)
    temp_comments.extend(comments)
    temp.update({constants.OUTPUT_COLUMN_NAME: temp_comments})
    df = pd.DataFrame(temp)
    
    writer = ExcelWriter(fname)
    df.to_excel(writer, constants.OUTPUT_COLUMN_NAME, index=False)
    writer.save()
    writer.close()
