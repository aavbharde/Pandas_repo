# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 15:04:05 2019

@author: aakan
"""

import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv('C:/Users/aakan/Desktop/Stevens/Semester 2/Self_Study/Python/Pandas/Pandas_barplot/Sub_Division_IMD_2017.csv')
print(file)
obj = file[(file.SUBDIVISION == 'Madhya Maharashtra') & (file.YEAR >= 2000)].plot(kind='bar',y='ANNUAL',x='YEAR',figsize=(15,5),color = 'purple',title='ANNUAL RAINFALL IN MADHYA MAHARASHTRA')
obj.set_ylabel('Rainfall in mms')
