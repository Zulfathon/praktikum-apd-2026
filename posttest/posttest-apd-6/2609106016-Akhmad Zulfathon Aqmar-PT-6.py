import os
daftarKamar = {}

while True:
    os.system('cls')
    print("===================")
    print("SILAHKAN PILIH MENU")
    print("===================")
    print("1. Menambahkan Kamar")
    print("2. Daftar Kamar")
    print("3. Mengubah Status Kamar")
    print("4. Menghapus Kamar")
    print("5. Keluar")
    pilihanUtama = (input("Masukkan Pilihan (1-5): "))

    if pilihanUtama == "1":
        while True:
            os.system('cls')
            print("=================")
            print("Menambahkan Kamar")
            print("=================")
            print("1. Tambah Kamar")
            print("2. Kembali")
            pilihan1 = (input("Masukkan Pilihan (1/2): "))

            if pilihan1 == "2":
                break
            elif pilihan1 == "1":
                while True: 
                    noKamar = int(input("Masukkan Nomor Kamar: "))
                    if noKamar in daftarKamar:
                        print("Gagal!, Kamar No", noKamar, "Telah Terdaftar")
                        print()
                        input("Tekan Enter Untuk Melanjutkan")
                        break
                    else:
                        while True:
                            print("==========================")
                            print("Silahkan Pilih Jenis Kamar")
                            print("==========================")
                            print("1. Besar")
                            print("2. Kecil")
                            pilihanJenis = input("Masukkan Pilihan (1/2): ")


                            if pilihanJenis == "1":
                                jenisKamar = "Besar"
                                hargaKamar = 850000
                                break
                            elif pilihanJenis == "2":
                                jenisKamar = "Kecil"
                                hargaKamar = 750000
                                break
                            else:
                                print("Pilihan tidak valid!")
                                print()
                                input("Tekan Enter Untuk Melanjutkan")
                                continue

                        kamarbaru = {
                            'Jenis Kamar'  : jenisKamar,
                            'Harga Kamar'  : hargaKamar,
                            'Status Kamar' : "Kosong",
                            'Nama Penghuni': "-",
                            'Nomor Kontak' : "-"
                            }
                        daftarKamar[noKamar] = kamarbaru
                        print("Berhasil!, Kamar No", noKamar, "Telah Berhasil Ditambahkan")
                        print()
                        input("Tekan Enter Untuk Melanjutkan")
                    break
            else:
                print("Pilihan tidak valid!")
                print()
                input("Tekan Enter Untuk Melanjutkan")

    elif pilihanUtama == "2":
        os.system('cls')
        print("====================")
        print("DAFTAR SELURUH KAMAR")
        print("====================")

        if len(daftarKamar) == 0:
            print("Belum Ada Data Kamar Di Dalam Daftar")
            print()
        else:
            for noKamar, dataKamar in daftarKamar.items():
                print('Nomor Kamar   : ', noKamar)
                print('Jenis Kamar   : ', dataKamar['Jenis Kamar']) 
                print('Harga Kamar   : ', dataKamar['Harga Kamar']) 
                print('Status Kamar  : ', dataKamar['Status Kamar'])
                print('Nama Penghuni : ', dataKamar['Nama Penghuni'])
                print('Nomor Kontak  : ', dataKamar['Nomor Kontak'])
                print("-" * 30)
        
        print()
        input("Tekan Enter Untuk Kembali Ke Menu Utama")

    elif pilihanUtama == "3":
        if len(daftarKamar) == 0:
            os.system('cls')
            print("=====================")
            print("MENGUBAH STATUS KAMAR")
            print("=====================")
            print("Belum Ada Data Kamar Di Dalam Daftar")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu utama")

        else:
            while True:
                os.system('cls')
                print("=====================")
                print("MENGUBAH STATUS KAMAR")
                print("=====================")
                print("1. Ubah Status Kamar")
                print("2. Kembali")
                pilihan3 = input("Masukkan Pilihan (1/2): ")

                if pilihan3 == "2":
                    break
                elif pilihan3 == "1":
                    while True:
                        noTujuan = int(input("Masukkan Nomor Kamar Yang Ingin Diubah: "))
                        if noTujuan in daftarKamar:
                            kamar = daftarKamar[noTujuan]
                        
                            if kamar['Status Kamar'] == "Kosong":
                                print("Kamar Nomor", noTujuan, "Saat Ini Kosong")
                                namaPenghuni = input("Masukkan Nama Penghuni: ")
                                noKontak = input("Masukkan Nomor Kontak: ")
                        
                                kamar['Status Kamar'] = "Terisi"
                                kamar['Nama Penghuni'] = namaPenghuni
                                kamar['Nomor Kontak'] = noKontak
                                print("Berhasil!, Kamar No", noTujuan, "Telah Terisi Oleh", namaPenghuni)
                                print()
                                input("Tekan Enter Untuk Melanjutkan")
                                break
                            else:
                                while True:
                                    print("Kamar No", noTujuan, "Telah Terisi oleh", kamar['Nama Penghuni'])
                                    print("1. Kosongkan Kamar")
                                    print("2. Batalkan Perubahan")
                                    pilihanStatus = input("Masukkan Pilihan (1/2): ")
                        
                                    if pilihanStatus == "1":
                                        kamar['Status Kamar'] = "Kosong"
                                        kamar['Nama Penghuni'] = "-"
                                        kamar['Nomor Kontak'] = "-"
                                        print("Berhasil!, Kamar No", noTujuan, "Telah Dikosongkan")
                                        print()
                                        input("Tekan Enter Untuk Melanjutkan")
                                        break
                                    elif pilihanStatus == "2":
                                        break
                                    else:
                                        print("Pilihan Tidak Valid!")
                                        print()
                                        input("Tekan Enter Untuk Melanjutkan")
                                        break    
                        else:
                            print("Gagal!, Kamar No", noTujuan, "Tidak Ditemukan Di Dalam Daftar")
                            print()
                            input("Tekan Enter Untuk Melanjutkan")
                            break
                        break
                else:
                    print("Pilihan Tidak Valid!")  
                    print()
                    input("Tekan Enter Untuk Melanjutkan")  

    elif pilihanUtama == "4":
        if len(daftarKamar) == 0:
            os.system('cls')
            print("===============")
            print("MENGHAPUS KAMAR")
            print("===============")
            print("Belum Ada Data Kamar Di Dalam Daftar")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu Utama")
        else:
            while True:
                os.system('cls')
                print("===============")
                print("MENGHAPUS KAMAR")
                print("===============")
                print("1. Hapus Kamar")
                print("2. Kembali")
                pilihan4 = input("Masukkan Pilihan(1/2): ")

                if pilihan4 == "2":
                   break
                elif pilihan4 == "1":
                   noHapus = int(input("Masukkan Nomor Kamar Yang Ingin Dihapus: "))
                   if noHapus in daftarKamar:
                       kamar = daftarKamar[noHapus]
                       if kamar['Status Kamar'] == "Terisi":
                           print("Gagal!, Kamar No", noHapus, "Sedang Diisi Oleh", kamar['Nama Penghuni'])
                           print("Harap Dikosongkan Terlebih Dahulu")
                           print()
                           input("Tekan Enter Untuk Melanjutkan")
                       else:
                           del daftarKamar[noHapus]
                           print("Berhasil!, Kamar No", noHapus, "Telah Dihapus")
                           print()
                           input("Tekan Enter Untuk Melanjutkan")
                   else:
                       print("Gagal!, Kamar No", noHapus, "Tidak Ditemukan Di Dalam Daftar Kamar")
                       print()
                       input("Tekan Enter Untuk Melanjutkan")
                   
                else:
                    print("Pilihan Tidak Valid!")
                    print()
                    input("Tekan Enter Untuk Melanjutkan")

    elif pilihanUtama == "5":
        os.system('cls')
        print("===================")
        print("KELUAR DARI PROGRAM")
        print("===================")
        exit()

    else:
        print("Pilihan Tidak Valid!")
        print()
        input("Tekan Enter Untuk Melanjutkan")



       
        