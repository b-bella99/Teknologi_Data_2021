import pandas as pd
import os

class PandasDemos:

    def __init__(self):
        self.data = None

    def tampilkan_pilihan(self):
        print('Pandas Demos')
        print('-------------')
        print('Menu:')
        print('(1) Load dataset')
        print('(2) Priview the top and bottom 5 data rows')
        print('(3) Show the data of intelligence system group research')
        print('(4) Show authors and their proposal titles')
        print('(0) Quit')
        pilihan = input('What is your choice? ')
        if pilihan == '1':
            self.load_dataset()
            return True
        elif pilihan == '2':
            self.tampilkan_5_baris_awal_akhir()
            return True
        elif pilihan == '3':
            self.tampilkan_data_sistem_cerdas()
            return True
        elif pilihan == '4':
            self.tampilkan_pengusul_dan_judul()
            return True
        else:
            return False

    def load_dataset(self):
        # print("Path at terminal when executing this file")
        # print(os.getcwd() + "\n")

        # print("this file path, relative to os.getcwd()")
        # print(__file__ + "\n")

        #print("This file full path (following symlinks)")
        full_path = os.path.realpath(__file__)
        # print(full_path + "\n")

        # print("This file directory and name")
        path, filename = os.path.split(full_path)
        # print(path '-->' + filename + "\n")
        path_parent = os.path.dirname(path)
        # print('path_parent: ', path_parent + "\files\rekap_prposal.csv")

        # print("this file directory only")
        #print(os.path.dirname(full_path))

        print('Load dataset...')
        # # Hasil import sebagai DataFrame
        # # https://stackoverflow.com/questions/18039057/python-pandas-error-tokenizing-data
        # # https://www.shanelynn.ie/pandas-csv-error-error-tokenizing-data-c-error-eof-inside-string-starting-at-line/
        self.data = pd.read_csv(
        #     'files/rekap_proposal.csv',
            path_parent + "\\files\\rekap_proposal.csv",
            sep=';',                      # Separator
            error_bad_lines=False,        # Skip baris yang error
            engine='python'               # Mengganti Parser engine dari C ke Python
        )
        # # Set kolom 'id' sebagai index
        self.data.set_index('id')
        # # Cetak di console
        print(self.data.to_string())

    def tampilkan_pengusul_dan_judul(self):
        print('Memilih kolom tertentu..')
        # # Mengambil berdasarkan nama kolom
        nama = self.data['nama_pengusul']
        # # Bisa juga dengan cara seperti ini
        judul = self.data.judul_proposal
        # # Menggabungkan 2 DataFrame
        # # A. Digabungkan barisnya (Ditumpuk)
        gabung_baris = pd.concat([nama, judul], axis=0)
        print(gabung_baris.to_string())
        # # B. Digabungkan kolomnya (Digandeng)
        gabung_kolom = pd.concat([nama, judul], axis=1)
        print(gabung_kolom.to_string())

    def tampilkan_5_baris_awal_akhir(self):
        print('Menyeleksi beberapa baris di awal dan akhir..')
        # # Mengambil N-baris teratas
        awal5 = self.data.head(5)
        print(awal5.to_string())
        # # Mengambil N-baris terakhir
        akhir5 = self.data.tail(5)
        print(akhir5.to_string())

    def tampilkan_data_sistem_cerdas(self):
        print('Seleksi baris dengan WHERE')
        # # Membuat filter untuk WHERE
        filter = self.data['grup_riset'] == 'SISTEM CERDAS'
        # # Seleksi data
        data_si = self.data.where(filter)
        print(data_si)
