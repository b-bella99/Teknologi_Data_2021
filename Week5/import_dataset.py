import inline as inline
import matplotlib
import numpy as np  # linear algebra
import pandas as pd # data processing, CSV file I?O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns # data vizualisation

#to set backend of matplotlib to iniline view visual:
#%matplotlib inline

#using PyCharm
plt.show()

df = pd.read_csv('BreadBasket_DMS.csv')

#Get Distinct/Unique Value
print('Distinct/Unique Value: ', df.Item.unique())

#Displaying Unique Item by Removing Duplicates Data in a Column
