# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 15:21:43 2020

@author: jean_
"""

import os

PATH = "C:\\Users\\jean_\\Desktop\\projet-dl\\photos-appareil"

files = os.listdir(PATH)

for f in files:
    if os.path.isdir(os.path.join(PATH, f)):  #if the file is a folder
        folder = os.listdir(os.path.join(PATH, f))

        for pic in folder:
            new_name = pic[:pic.find("(")]+"_"+pic[pic.find(" ")+1:]
            os.rename(os.path.join(PATH, f, pic), os.path.join(PATH, f, new_name))

