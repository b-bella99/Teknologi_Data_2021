# -*- coding: utf-8 -*-
"""1841720004_7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uL2dVV2jGmFGOLu0Wl_H8N9986gDP3-k
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

## ------ data cleaning example-1 ------ ##

# import data from a *.xlsx retail transaction dataset

# because I use google Collab, so the file I upload to google drive

df = pd.read_excel("/content/drive/MyDrive/Teknologi Data/OnlineRetail.xlsx")
df.info()
print(df.isnull().any())
print(df.isnull().sum())
print(df[df['Description'].isnull()].head())
print(df[df['CustomerID'].isnull()].head())

#drop all rows with missing data
dfcleaned = df.dropna(axis=0)

#check number of rows deleted
print('df: ' , len(df), ' | ', 'dfcleaned: ', len(dfcleaned))
print('df - dfcleaned = ' , len(df) - len(dfcleaned))

#try to check & find another missing / incomplete / invalid data
#for example : check unit Price that has negative or zero value
print((dfcleaned['UnitPrice'] <= 0.0).sum())

print(dfcleaned[dfcleaned['UnitPrice'] <= 0.0].head())