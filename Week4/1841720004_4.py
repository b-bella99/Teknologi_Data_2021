# -*- coding: utf-8 -*-
"""1841720004_4.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yb-TkNheunYkX0BzteLd5SCgQGGIzBq-
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

## ------ import data example-4 ------ ##
#  import data from a csv formatted file
#  and set a column as an index using set_index() function

# because I use google Collab, so the file I upload to google drive

df = pd.read_csv("/content/drive/MyDrive/Teknologi Data/fifa.csv")
df.info()

df.set_index('Date', inplace = True)
df.info()

print(df.head())  # if we are using VS Code, otherwise, df.head() for google Colab