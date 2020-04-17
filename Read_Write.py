# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 15:51:09 2020

@author: Abhinav
"""

#-------------------------Reading & Writing data in Files----------------------
# Reading CSV Files with Pandas:
import pandas
df = pandas.read_csv('F:/pyWork/pyData/User_Data.csv')
print(df)

# Writing CSV Files with Pandas:
import pandas
df.to_csv('F:/pyWork/pyData/User_Data_1.csv')

# Reading Excel Files with Pandas
df = pandas.read_excel('F:/pyWork/pyData/User_Data.xlsx')
print(df)

# Writing Excel Files with Pandas 
df1 = pandas.DataFrame(df)
print (df1)
df1.to_excel('Bank1.xlsx')