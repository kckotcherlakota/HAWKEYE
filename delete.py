#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 02:44:09 2019

@author: krishna
"""
#
#import os
#os.remove("Don.xlsx")
##print("File Removed!")
# Python program to explain os.remove() method 

# importing os module 
import os 

# File name 
file = 'Don.xlsx'

# File location 
location = "/home/krishna/Desktop/hawkeye"

# Path 
path = os.path.join(location, file) 

# Remove the file 
# 'file.txt' 
os.remove(path) 
print("%s has been removed successfully" %file) 
