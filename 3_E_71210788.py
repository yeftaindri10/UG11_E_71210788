print("=======Program Manipulasi String=======")
print("Pilihan Menu :")
print("1. Hitung kata")
print("2. cek kata")
print("3. ubah kata")
pil = input("Pilihan anda : ")
kalimat = input("Masukkan sebuah kalimat/kata : ")
hasil = (kalimat.lower())

if pil == "1":
    masukkan1 = input("Masukkan kata yang ingin dihitung : ")
    tampilan = hasil.count(masukkan1)
    print("Terdapat sebanyak", tampilan, "kata", masukkan1, "di dalam string")

if pil == "2":
    masukkan2 = input("Masukkan kata yang ingin di cek : ")
    tampilan = masukkan2.upper()
    ubah = hasil.replace(masukkan2,tampilan)
    print("Kata", masukkan2, "terdapat di dalam string")
    print("String diubah menjadi :")
    print(ubah)

if pil == "3":
    masukkan3 = input("Masukkan kata yang ingin diubah : ")
    pengganti = input("Masukkan kata pengganti : ")
    print("Anda akan mengubah kata", masukkan3, "menjadi", pengganti, "sebanyak 1x")
    ubah = input("Apakah anda ingin mengubah jumlah total penggantian kata ? (yes/no) : ")

    if ubah == "yes":
        totalganti = int(input("Masukkan jumlah total penggantian : "))
        print("String berhasil diubah menjadi :")
        ganti = hasil.replace(masukkan3, pengganti, totalganti)
        print(ganti)
    elif ubah == "no":
        x = 1
        print("String berhasil diubah menjadi :")
        ganti = hasil.replace(masukkan3, pengganti, x)
        print(ganti)