# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt

#############################################################
#Beef consumption over the years

food_file = pd.read_csv('C:/Users/aakan/Desktop/Stevens/Semester 2/Self_Study/Python/Pandas/Project_Food_1/food.csv')
print(food_file)
obj = food_file[food_file.FOOD == 'BEEF'].plot(x='YEAR',y='CONSUMPTION',kind='line',title = 'BEEF CONSUMPTION OVER THE YEARS',color = 'Red')#The df.plot() function returns a matplotlib.axes.AxesSubplot object
obj.set_ylabel("BEEF CONSUMPTION")

#######################################################
# Fish versus Meat Consumption










