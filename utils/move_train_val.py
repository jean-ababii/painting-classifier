# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:13:15 2020

@author: jean_
"""

import os

PATH = "C:\\Users\\jean_\\Desktop\\projet-dl\\photos-appareil"

files = os.listdir(PATH)

for f in files:
    if os.path.isdir(os.path.join(PATH, f)) and f[-5:]== "train":  #if f is a train folder 
        folder = os.listdir(os.path.join(PATH, f))
        folder_number = f[:2]
        

        for pic in folder:
            if int(pic[pic.find("_")+1:pic.find(".")]) % 10 == 0:
                new_location = os.path.join(PATH, folder_number + "_val", pic)
                os.rename(os.path.join(PATH, f, pic), new_location)


