# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 15:16:22 2020

@author: Mollasadra
"""

import glassdoor_scraper as gs
import pandas as pd
path = "C:/Users/Mollasadra/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15,False, path, 15)
df                 