from kegiatan import Kegiatan

class Keuangan(Kegiatan):
    def __init__(self):
        super().__init__()
        self.jenis = 'kredit'
        self.nominal = 0

    def tampilkan_form(self):
        super().tampilkan_form()
        str_jenis = input('Masukkan Jenis: ')
        str_nominal = input('Masukkan Nominal: ')
        self.jenis = str_jenis
        self.nominal = float(str_nominal)

    def simpan(self):
        data = {
            'tanggal' : self.tanggal,
            'nama' : self.nama,
            'jenis' : self.jenis,
            'nominal' : self.nominal
        }
        self.tersimpan.append(data)

    def tampilkan_tersimpan(self):
        i = 0
        while i < len(self.tersimpan):
            baris = self.tersimpan[i]
            print('{}. [{}] {} | {} | Rp. {}'.format((i+1),
                                                     baris['tanggal'],
                                                     baris['nama'],
                                                     baris['jenis'],
                                                     baris['nominal']))
            i = (i + 1)