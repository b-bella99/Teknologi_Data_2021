from kegiatan import Kegiatan
from keuangan import Keuangan
from pandasdemos.pandasdemos import PandasDemos

class App:
    def __init__(self):
        self.kegiatan = Keuangan()

    def jalankan(self):
        print('---------------------------------')
        print('Welcome to NoteApp!')
        print('---------------------------------')
        print('Menu:')
        print('(1) Input a new Note')
        print('(2) Look at Existing Notes')
        print('(3) Pandas Demos')
        print('(0) Quit')
        pilihan = input('What is your choice? ')
        print('Your choice is ', pilihan)
        selesai = False
        if pilihan == '0':
            selesai = True
        else:
            if pilihan == '1':
                #print('Choice #1')
                self.kegiatan.tampilkan_form()
                self.kegiatan.simpan()
            elif pilihan == '2':
                #print('Choice #2')
                self.kegiatan.tampilkan_tersimpan()
            elif pilihan == '3':
                print('Membuka program latihan Pandas')
                pd = PandasDemos()
                lanjut = True
                while lanjut:
                    lanjut = pd.tampilkan_pilihan()
            else:
                print('[Error] Youre choice is not valid!')
                selesai = False
        return selesai