daftarKamar = []

while True:
    print("===========================")
    print("SISTEM MANAJEMEN KAMAR KOST")
    print("===========================")
    print("1. Tambah Kamar")
    print("2. Tampilkan Seluruh Kamar")
    print("3. Ubah Status Kamar")
    print("4. Hapus Kamar")
    print("5. Keluar")
    print("===========================")
    print()
    pilihan = input("Masukkan pilihan (1-5): ")
    if pilihan == "1":
        while True: 
            print("=================")
            print("TAMBAH KAMAR BARU")
            print("=================")
            nomorKamar = int(input("Masukkan Nomor Kamar (Angka): "))
            kamarKembar = False
            for kamar in daftarKamar:
                if kamar['Nomor'] == nomorKamar:
                    kamarKembar = True
            if kamarKembar == True:
                print("Gagal, Kamar Nomor:", nomorKamar, "Telah Terdaftar di List")
            else:
                while True:
                    print("=================")
                    print("Pilih Jenis Kamar")
                    print("=================")
                    print("1. Besar")
                    print("2. Kecil")
                    pilihJenis = input("Masukkan Jenis kamar (1/2): ")
                    if pilihJenis == "1":
                        jenisPilihan = "Besar"
                        hargaKamar = 850000
                        break
                    elif pilihJenis == "2":
                        jenisPilihan = "Kecil"
                        hargaKamar = 750000
                        break
                    else:
                        print()
                        print("Pilihan tidak valid!")

                kamarbaru = {
                    'Nomor': nomorKamar,
                    'Jenis': jenisPilihan,
                    'Harga': hargaKamar,
                    'Status': 'Kosong',
                    'Penghuni': '-',
                    'No. Hp': '-'
                    }
                daftarKamar.append(kamarbaru)
                print("Berhasil!, Kamar No", nomorKamar, "Berhasil Ditambahkan")
                break

    elif pilihan == "2":
        print("======================")
        print("DAFTAR INFORMASI KAMAR")
        print("======================")

        if len(daftarKamar) == 0:
            print("Belum Ada Data Kamar Di Dalam Daftar")
        else:
            for kamar in daftarKamar:
                print("Nomor Kamar    :", kamar['Nomor'])
                print("Jenis Kamar    :", kamar['Jenis'])
                print("Harga Kamar    :", kamar['Harga'])
                print("Status Kamar   :", kamar['Status'])
                print("Nama Penghuni  :", kamar['Penghuni'])
                print("Nomor Kontak   :", kamar['No. Hp'])

                print("-" * 36)

    elif pilihan == "3":
        print("=================")
        print("UBAH STATUS KAMAR")
        print("=================")

        if len(daftarKamar) == 0:
            print("Belum Ada Data Kamar Di Dalam Daftar")
        else:
            while True:
                noKamar = (int(input("Masukkan Nomor Kamar Yang Ingin Diubah: ")))
                kamarTujuan = False
                for kamar in daftarKamar:
                    if kamar['Nomor'] == noKamar:
                        kamarTujuan = True
                        if kamar['Status'] == "Kosong":
                            print("Kamar Nomor", noKamar, "Saat Ini Kosong")
                            print("Silahkan Lengkapi Data Diri")
                            namaPenghuni = input("Masukkan Nama: ")
                            noPenghuni = input("Masukkan Nomor Hp: ")
                    

                            kamar['Status'] = "Terisi"
                            kamar['Penghuni'] = namaPenghuni
                            kamar['No. Hp'] = noPenghuni
                            print("Berhasil!, Kamar No", noKamar, "Telah Terisi Oleh:", namaPenghuni)
                        else:
                            print("Kamar No", noKamar, "Saat Ini Telah Terisi Oleh", kamar['Penghuni'])
                            print("Silahkan Pilih")
                            print("1. Kosongkan Kamar")
                            print("2. Batalkan Perubahan")
                            pilihanStatus = input("Masukkan Pilihan (1/2): ")

                            if pilihanStatus == "1":
                                kamar['Status'] = "Kosong"
                                kamar['Penghuni'] = "-"
                                kamar['No. Hp'] = "-"
                                print("Berhasil!, Kamar No", noKamar, "Telah Dikosongkan")
                            else:
                                print("Perubahan Status Dibatalkan")
                break
            if kamarTujuan == False:
                print("Gagal!, Kamar No", noKamar, "Tidak Ditemukan Di Dalam Daftar")
    elif pilihan == "4":
        print("================")
        print("HAPUS DATA KAMAR")
        print("================")

        if len(daftarKamar) == 0:
            print("Belum Ada Data Kamar Di Dalam Daftar")
        else:
            while True:
                noHapus = int(input("Masukkan No Kamar Yang Ingin Dihapus: "))
                kamarDitemukan = False
                kamarTerisi = False

                for kamar in daftarKamar:
                    if kamar['Nomor'] == noHapus:
                        kamarDitemukan = True

                        if kamar['Status'] == "Terisi":
                            kamarTerisi = True
                        else: 
                            daftarKamar.remove(kamar)
                        break
                if kamarDitemukan == True:
                    if kamarTerisi == True:
                        print("Gagal!, Kamar No", noHapus, "Tidak Dapat Dihapus Karena Masih Ada Penghuninya")
                        print("Silahkan Kosongkan Kamar Terlebih Dahulu")
                    else:
                        print("Berhasil!, Kamar No", noHapus, "Telah Dihapus Dari Daftar")
                    break
                else:
                    print("Gagal!, Kamar No", noHapus, "Tidak Ditemukan Dari Dalam Daftar")
                    break
    elif pilihan == "5":
        print("===================")
        print("KELUAR DARI PROGRAM")
        print("===================")
        break
    else:
        print("Pilihan Tidak Valid!")



            
                

