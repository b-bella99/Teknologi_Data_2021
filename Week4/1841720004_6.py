# -*- coding: utf-8 -*-
"""1841720004_6.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Xq1PwUh5ovVbw0o3DnVadFQch4n1aGSk
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

## ------ data overview example-2 ------ ##

# because I use google Collab, so the file I upload to google drive

df = pd.read_excel("/content/drive/MyDrive/Teknologi Data/OnlineRetail.xlsx")
df.info()
print(df.isnull().any())
print(df.isnull().sum())
print(df[df['Description'].isnull()].head())