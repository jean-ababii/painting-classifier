# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 16:00:32 2020

@author: jean_
"""

import os

PATH = "C:\\Users\\jean_\\Desktop\\projet-dl\\photos-appareil"

for i in range(56):

    if i < 9 :  # to create "01_val" and not "1_val"
        name = "0" + str(i+1) + "_test"
    else :
        name = str(i+1) + "_test"
    os.mkdir(os.path.join(PATH, name))