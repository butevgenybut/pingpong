# -*- coding: utf-8 -*-
"""
Created on Tue Aug 29 15:08:48 2023

@author: FutureCode
"""

import re
#email "^[a-zA-Z0-9_+-.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9]+$"
#дата "[0-9]+\.[0-9]+\.[0-9]"

textright = "Tue Aug 29 15:08:48 2023"
textwrong = "Tue Aug 29 15:08:48 q023"
regex = "[a-zA-Z]+ [a-zA-Z]+ [0-9]+ [0-9]+:[0-9]+:[0-9]+ [0-9]+"
print(re.match(regex,textright))
print(re.match(regex,textwrong))