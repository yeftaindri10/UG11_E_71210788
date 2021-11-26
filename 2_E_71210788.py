def hurufTengah(a):
    jumlah = len(a)
    if jumlah % 2 == 1:
        if jumlah >= 5:
            y = int((jumlah - 1) / 2)
            return a[y - 1] + a[y] + a[y + 1]
        elif jumlah < 5:
            y = int((jumlah - 1) / 2)
            return a[y]
    elif jumlah % 2 == 0:
        if jumlah < 8:
            y = int(jumlah / 2)
            return a[y - 1] + a[y]
        else:
            y = int(jumlah / 2)
            return a[y - 2] + a[y - 1] + a[y] + a[y + 1]


a = input("Masukkan kata: ")
print("Huruf tengah pada kata", a, "adalah", hurufTengah(a))