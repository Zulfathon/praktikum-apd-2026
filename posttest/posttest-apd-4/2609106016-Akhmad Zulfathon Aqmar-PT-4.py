username = "Fathon"
password = "016"
pin = "016016"
saldo = 5000000

for i in range(3):
    inputUsername = input("Masukkan username: ")
    inputPassword = input("Masukkan password: ")
    if inputUsername == username and inputPassword == password:
        print("login berhasil")
        break
    elif inputUsername != username and inputPassword != password:
        print("Username dan password salah")
    elif inputUsername != username:
        print("Username salah")
    elif inputPassword != password:
        print("Password salah")
else:
    print("Akun anda terblokir")
    exit()
print()
print("== SILAHKAN PILIH MENU ==")
print("1. Transfer uang")
print("2. Log out")

menu = input("Masukkan pilihan (1/2): ")
if menu == "1":
    transfer = True
    while transfer:
        namaPenerima = input("Masukkan nama penerima: ")
        nominalTransfer = int(input("Masukkan nominal transfer: "))
        if nominalTransfer < 50000:
            print("Transfer minimal 50000")
        elif nominalTransfer > saldo:
            print("Saldo anda tidak cukup")
        elif nominalTransfer > 1000000:
            print("Transfer maksimal 1000000")
        else:
            pin = (input("Masukkkan PIN: "))
            if pin == "016016":
                sisaSaldo = saldo - nominalTransfer
                print("Transfer berhasil, sisa saldo anda: ", sisaSaldo)
                print()
                print("==  Struk bukti transfer ==")
                print("Nama pengirim: ",username)
                print("Nama penerima: ",namaPenerima)
                print("Nominal Transfer: ",nominalTransfer)
                saldo = sisaSaldo
                kembali = input("Apakah pengguna ingin melakukan transfer lagi (iya/tidak)? ")
                if kembali == "tidak":
                    transfer = False   
elif menu == "2":
    exit()
else:
    print("Pilihan tidak valid")