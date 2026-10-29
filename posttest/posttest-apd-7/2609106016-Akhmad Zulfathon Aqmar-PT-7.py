import os
daftarKamar = {}
waktuBertamu = "07:00 - 21-00"
info = "Maksimal Berkunjung 3 Jam Sehari"

def tampilanStatistik():
    jumlahTerdaftar = len(daftarKamar) 
    hitungTerisi = 0
    jumlahBesar = 0
    jumlahKecil = 0
    for data in daftarKamar.values():
        if data.get('Status Kamar') == "Terisi":
            hitungTerisi += 1

        if data.get ('Jenis Kamar') == "Besar":
            jumlahBesar += 1
        elif data.get ('Jenis Kamar') == "Kecil":
            jumlahKecil += 1
    jumlahTerisi = hitungTerisi        
    jumlahKosong = jumlahTerdaftar - jumlahTerisi  
    print("===================================================")
    print("               STATISTIK DAN INFO KOS              ")
    print("===================================================")
    print("Total Terdaftar      : ", jumlahTerdaftar)
    print("Kamar Terisi         : ", jumlahTerisi)
    print("Kamar Kosong         : ", jumlahKosong)
    print("Kamar Besar          : ", jumlahBesar)
    print("Kamar Kecil          : ", jumlahKecil)
    print("===================================================")

def tampilanAngka():
    return "Info: Wajib Berupa Angka Bilangan Bulat!"

def tampilanInfo():
    return "Info: Wajib Memilih Sesuai Pilihan Yang Tersedia!"

def hargaBayar(jenis):
    if jenis == "1" or jenis == "Besar":
        return 850000
    else:
        return 750000

def periksaNama(penghuni):
    if len(penghuni.strip()) > 0:
        return True
    else:
        return False

def tekanEnter():
    input("Tekan Enter Untuk Melanjutkan")

def tampilanKeluar():
    print("===================================================")
    print("                KELUAR DARI PROGRAM                ")
    print("===================================================")
while True:
    os.system('cls')
    print("===================================================")
    print("                SILAHKAN PILIH MENU                ")
    print("===================================================")
    print("Waktu Bertamu : ", waktuBertamu)
    print(info)
    print("---------------------------------------------------")
    print(tampilanInfo())
    print("1. Menambahkan Kamar")
    print("2. Daftar Kamar")
    print("3. Mengubah Status Kamar")
    print("4. Menghapus Kamar")
    print("5. Keluar")

    pilihanUtama = (input("Masukkan Pilihan (1-5): "))

    if pilihanUtama == "1":
        while True:
            os.system('cls')
            print("===================================================")
            print("                 MENAMBAHKAN KAMAR                 ")
            print("===================================================")
            print(tampilanInfo())
            print("1. Tambah Kamar")
            print("2. Kembali")
            pilihan1 = (input("Masukkan Pilihan (1/2): "))

            if pilihan1 == "2":
                break
            elif pilihan1 == "1":
                while True:
                    print(tampilanAngka())
                    try: 
                        noKamar = int(input("Masukkan Nomor Kamar: "))
                    except ValueError:
                        print("Gagal!, Wajib Memasukkan Angka Bilangan Bulat")
                        print()
                        tekanEnter()
                        break
                    if noKamar in daftarKamar:
                        print("Gagal!, Kamar No", noKamar, "Telah Terdaftar")
                        print()
                        tekanEnter()
                        break
                    else:
                        while True:
                            print("===================================================")
                            print("             SILAHKAN PILIH JENIS KAMAR            ")
                            print("===================================================")
                            print(tampilanInfo())
                            print("1. Besar")
                            print("2. Kecil")
                            pilihanJenis = input("Masukkan Pilihan (1/2): ")


                            if pilihanJenis == "1":
                                jenisKamar = "Besar"
                                hargaKamar = hargaBayar("Besar")
                                break
                            elif pilihanJenis == "2":
                                jenisKamar = "Kecil"
                                hargaKamar = hargaBayar("Kecil")
                                break
                            else:
                                print("Pilihan tidak valid!")
                                print()
                                tekanEnter()
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
                        tekanEnter()
                    break
            else:
                print("Pilihan tidak valid!")
                print()
                tekanEnter()

    elif pilihanUtama == "2":
        os.system('cls')
        print("===================================================")
        print("               DAFTAR SELURUH KAMAR                ")
        print("===================================================")

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
            print("===================================================")
            print("              MENGUBAH STATUS KAMAR                ")
            print("===================================================")
            
            print("Belum Ada Data Kamar Di Dalam Daftar")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu utama")

        else:
            while True:
                os.system('cls')
                print("===================================================")
                print("              MENGUBAH STATUS KAMAR                ")
                print("===================================================")
                print(tampilanInfo())
                print("1. Ubah Status Kamar")
                print("2. Kembali")
                pilihan3 = input("Masukkan Pilihan (1/2): ")

                if pilihan3 == "2":
                    break
                elif pilihan3 == "1":
                    while True:
                        print(tampilanAngka())
                        try:
                            noTujuan = int(input("Masukkan Nomor Kamar Yang Ingin Diubah: "))
                        except ValueError:
                            print("Gagal!, Wajib Memasukkan Angka Bilangan Bulat")
                            print()
                            tekanEnter()
                            break
                        if noTujuan in daftarKamar:
                            kamar = daftarKamar[noTujuan]
                        
                            if kamar['Status Kamar'] == "Kosong":
                                print("Kamar Nomor", noTujuan, "Saat Ini Kosong")
                                while True:
                                    namaPenghuni = input("Masukkan Nama Penghuni: ")
                                    if periksaNama(namaPenghuni):
                                        break
                                    else:
                                        print("Gagal!, Nama Penghuni Tidak Boleh Kosong")
                                        print()
                                noKontak = input("Masukkan Nomor Kontak: ")
                        
                                kamar['Status Kamar'] = "Terisi"
                                kamar['Nama Penghuni'] = namaPenghuni
                                kamar['Nomor Kontak'] = noKontak
                                print("Berhasil!, Kamar No", noTujuan, "Telah Terisi Oleh", namaPenghuni)
                                print()
                                tekanEnter()
                                break
                            else:
                                while True:
                                    print("Kamar No", noTujuan, "Telah Terisi oleh", kamar['Nama Penghuni'])
                                    print(tampilanInfo())
                                    print("1. Kosongkan Kamar")
                                    print("2. Batalkan Perubahan")
                                    pilihanStatus = input("Masukkan Pilihan (1/2): ")
                        
                                    if pilihanStatus == "1":
                                        kamar['Status Kamar'] = "Kosong"
                                        kamar['Nama Penghuni'] = "-"
                                        kamar['Nomor Kontak'] = "-"
                                        print("Berhasil!, Kamar No", noTujuan, "Telah Dikosongkan")
                                        print()
                                        tekanEnter()
                                        break
                                    elif pilihanStatus == "2":
                                        break
                                    else:
                                        print("Pilihan Tidak Valid!")
                                        print()
                                        tekanEnter()
                                        break    
                        else:
                            print("Gagal!, Kamar No", noTujuan, "Tidak Ditemukan Di Dalam Daftar")
                            print()
                            tekanEnter()
                            break
                        break
                else:
                    print("Pilihan Tidak Valid!")  
                    print()
                    tekanEnter()

    elif pilihanUtama == "4":
        if len(daftarKamar) == 0:
            os.system('cls')
            print("===================================================")
            print("                  MENGHAPUS KAMAR                  ")
            print("===================================================")
            print("Belum Ada Data Kamar Di Dalam Daftar")
            print()
            input("Tekan Enter Untuk Kembali Ke Menu Utama")
        else:
            while True:
                os.system('cls')
                print("===================================================")
                print("                 MENGHAPUS KAMAR                   ")
                print("===================================================")
                print(tampilanInfo())
                print("1. Hapus Kamar")
                print("2. Kembali")
                pilihan4 = input("Masukkan Pilihan(1/2): ")

                if pilihan4 == "2":
                   break
                elif pilihan4 == "1":
                   print(tampilanAngka())
                   try:
                       noHapus = int(input("Masukkan Nomor Kamar Yang Ingin Dihapus: "))
                   except ValueError:
                       print("Gagal!, Wajib Masukkan Angka Bilangan Bulat")
                       print()
                       tekanEnter()
                       continue
                   if noHapus in daftarKamar:
                       kamar = daftarKamar[noHapus]
                       if kamar['Status Kamar'] == "Terisi":
                           print("Gagal!, Kamar No", noHapus, "Sedang Diisi Oleh", kamar['Nama Penghuni'])
                           print("Harap Dikosongkan Terlebih Dahulu")
                           print()
                           tekanEnter()
                       else:
                           del daftarKamar[noHapus]
                           print("Berhasil!, Kamar No", noHapus, "Telah Dihapus")
                           print()
                           tekanEnter()
                   else:
                       print("Gagal!, Kamar No", noHapus, "Tidak Ditemukan Di Dalam Daftar Kamar")
                       print()
                       tekanEnter()
                   
                else:
                    print("Pilihan Tidak Valid!")
                    print()
                    tekanEnter()

    elif pilihanUtama == "5":
        os.system('cls')
        tampilanStatistik()
        tampilanKeluar()
        exit()

    else:
        print("Pilihan Tidak Valid!")
        print()
        tekanEnter()



       
        