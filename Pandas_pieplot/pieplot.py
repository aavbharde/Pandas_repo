# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 22:28:19 2019
Title: Plotting pie chart using pandas and matplotlib
Author: Aakanksha Vijay Bharde
"""
import pandas as pd
import matplotlib.pyplot as plt
file = pd.read_csv('C:/Users/aakan/Desktop/Stevens/Semester 2/Self_Study/Python/Pandas/Pandas_pieplot/Timecards.csv',skiprows=2)
#print(file)
dept = file.Department
print(dept)
tc = file['Number of Timecards']
explode = (0,0,0,0,0.1,0,0,0)
plt.pie(tc, labels=dept, autopct = '%.1f%%',shadow = False, startangle = 90, explode = explode)
plt.title("Timecards submitted by different departments in the month of July")
plt.axis('equal')
plt.show()
