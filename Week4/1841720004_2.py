# -*- coding: utf-8 -*-
"""1841720004_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1G0ckKi2zbP1sR-IO5o1cR1J_OkK7xm6M
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

## ------ import data example-2 ------ ##
#  import data from a csv formatted file
#  and save it into a pandas dataframe object name df

# because I use google Collab, so the file I upload to google drive

df = pd.read_csv("/content/drive/MyDrive/Teknologi Data/fifa.csv")
df.info()