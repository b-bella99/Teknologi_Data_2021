# -*- coding: utf-8 -*-
"""1841720004_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13Q9dWvB6m1TsawfgxOfNlGksvNdhMhqu
"""

from google.colab import drive
drive.mount('/content/drive')

import pandas as pd

## ------ import data example-1 ------ ##
#  import data from ms.excell file
#  and save it into a pandas dataframe object name df

# because I use google Collab, so the file I upload to google drive

df = pd.read_excel("/content/drive/MyDrive/Teknologi Data/OnlineRetail.xlsx")
df.info()