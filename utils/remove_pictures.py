# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 16:25:04 2020

@author: jean_
"""

import os

PATH = "C:\\Users\\jean_\\Desktop\\projet-dl\\photos-appareil\\images"

files = os.listdir(PATH)

for f in files:
    folder = os.listdir(os.path.join(PATH, f))       

    for pic in folder:
        if int(pic[pic.find("_")+1:pic.find(".")]) % 2 != 1:  #we only leave 1 pic in 5 starting with the first one
            os.remove(os.path.join(PATH, f, pic))
        else:
            print(os.path.join(PATH, f, pic))



