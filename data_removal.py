# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:07:51 2021

@author: Divy
"""

from random import sample
import os
folder_path = '/Users/rusha/Downloads/Dataset/melanoma/'
files = os.listdir(folder_path)
path, dirs, files = next(os.walk(folder_path))
file_count = len(files)
total_files_req = 500 
num_rem = file_count - total_files_req
for file in sample(files,num_rem):
    os.remove(folder_path+file)
    