# -*- coding: utf-8 -*-
"""
Created on Thu Aug 13 12:11:18 2020

@author: jean_
"""

import os

PATH = "C:\\Users\\jean_\\Desktop\\projet-dl\\photos-appareil\\test"

files = os.listdir(PATH)

for f in files:
    if os.path.isdir(os.path.join(PATH, f)):  #if the file is a folder
        os.rename(os.path.join(PATH, f), os.path.join(PATH, f[:2]))
