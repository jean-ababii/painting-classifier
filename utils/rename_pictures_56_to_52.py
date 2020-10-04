# -*- coding: utf-8 -*-

"""
Created on Thu Jul 23 15:21:43 2020

@author: jean_
"""

import os

PATH = "C:\\Users\\jean_\\Desktop\\projet-dl\\photos-appareil\\images\\52"

folder = os.listdir(PATH)

for pic in folder:
    new_name = "52_"+pic[pic.find("_")+1:]
    os.rename(os.path.join(PATH, pic), os.path.join(PATH, new_name))


