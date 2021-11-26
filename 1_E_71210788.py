def pangkatAngka():
    var = float(input("Masukkan angka yang ingin dipangkatkan\nAngka : "))
    print("Ingin memodifikasi pangkat? (yes/no)")
    data = input(": ")
    Data = data.capitalize()
    if Data == "Yes":
        var1 = float(input("Masukkan nilai pangkat : "))
        results = var ** var1
        print("Hasil dari", var, "^", var1, "=", results)
        return(results)
    elif Data == "No":
        results = var ** 2
        print("Hasil dari", var, "^ 2 = ", results)
        return(results)

def akarBilangan():
    print("Masukkan angka yang ingin diakarkan")
    var = float(input("Angka : "))
    print("Ingin memodifikasi akar? (yes/no)")
    data = input(": ")
    Data = data.capitalize()
    if Data == "Yes":
        var1 = float(input("Masukkan bilangan 2: "))
        results = float(var ** (1/var1))
        Results = "{:.2f}".format(results)
        print("Hasil akar pangkat", var1, "dari", var, "=", results)
        return Results
    elif Data == "No":
        results = float(var ** 1/2)
        Results = "{:.2f}".format(results)
        print("Hasil akar pangkat 2 dari", var, "=", results)
        return Results

print("Menu Program Yang Tersedia\n1. pangkatkan angka\n2. akarkan angka")
a = int(input("Masukkan pilihan yang diinginkan: "))
if a == 1 :
    print(pangkatAngka())
elif a == 2:
    print(akarBilangan())