#NO.1
a = ["B 1 ADC", "ZX-10R", "1000CC", "black"]
#NO.2
a.append("Rp.492.000.000")
a.append("2 roda")
a.insert(2, "Kawasaki")
a.insert(3, "Motor")

print(a)
#NO.3
ket = '''Selamat datang di aplikasi menghitung masukan pilihan:
1. untuk menghitung luas persegi
2. untuk menghitung luas lingkaran
3. untuk menghitung luas segitiga
'''

pilihan = input (ket)

match pilihan:
    case "1":
        print ("kamu memilih 1 untuk menghitung luas persegi")
        sisi = int(input("masukan sisi ?"))
        luasP = sisi * sisi
        print ("luas persegi yang sisinya", sisi, "adalah", luasP)
    case "2":
        print ("kamu memilih 2 untuk menghitung luas lingkaran")
        jari2 = float(input("masukan jari2 ?"))
        luasL = 3.14 * jari2 * jari2
        print ("luas lingkaran yang jari2nya", jari2, "adalah", int(luasL))
    case "3":
        print ("kamu memilih 3 untuk menghitung luas segitiga")
        alas = int(input("masukan alas ?"))
        tinggi = int(input("masukan tinggi ?"))
        tinggi = 0.5 * alas * tinggi
        print ("luas segitiga yang alasnya", alas, "dan tingginya", tinggi, "adalah")
    case _:
        print("salah memilih pilihan")

