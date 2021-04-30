import pandas as pd
import numpy as np
import os

full_path = os.path.realpath(__file__)
path, filename = os.path.split(full_path)

Cryotherapy = pd.read_excel(path + "\\files\Cryotherapy.xlsx")

print(Cryotherapy.head())

print(Cryotherapy.info())

print(Cryotherapy.empty)

print(Cryotherapy.size)

#Variabel independen
x = Cryotherapy.drop(["Result_of_Treatment"], axis=1)
print(x.head())

# Variabel dependen
y = Cryotherapy["Result_of_Treatment"]
print(y.head())

# Import train_test_split function
from sklearn.model_selection import train_test_split
x_train , x_test, y_train, y_test = train_test_split(x, y, test_size = 0.2, random_state = 123)

# Import Gaussian Naive Bayes Model
from sklearn.naive_bayes import GaussianNB
# Mengaktifkan / memanggil/ membuat fungsi klasifikasi Naive Bayes
modelnb = GaussianNB()
# Memasukkan data training pada fungsi klasifikasi naive bayes
nbtrain = modelnb.fit(x_train, y_train)
print(nbtrain.class_count_)

# Menentukan hasil prediksi dari x_test
y_pred = nbtrain.predict(x_test)
print(y_pred)

# Menentukan probalitias hasil prediksi
print(nbtrain.predict_proba(x_test))

# Import confussion_matrix mmodel
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y_test, y_pred))

# Menerapkan hasil confussion matrix
y_actual1 = pd.Series([1,0,1,0,1,0,1,0,1,0,0,1,1,0,1,1,0,0], name="actual")
y_pred1 = pd.Series([1,1,1,0,1,0,1,0,1,0,0,1,1,0,1,0,0,1], name="prediction")
df_confusion = pd.crosstab(y_actual1, y_pred1)
print(df_confusion)

# Menghilangkan nilai akurasi dari klasifikasi naive bayes
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))