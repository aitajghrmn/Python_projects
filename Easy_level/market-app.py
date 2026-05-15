mehsullar = {
    "alma" : 1.50 ,
    "armud" : 2.00 ,
    "banan" : 3.20 ,
    "sud" : 2.50 ,
    "corek" : 0.80

}

print("Market sistemine xosh gelmisiniz !")

ad = input("Mehsulun adini daxil edin: ")

if ad in mehsullar :
    print(ad, "qiymeti: " , mehsullar[ad], "AZN")
else :
    print("Bu mehsul tapilmadi")

en_bahali = max(mehsullar, key=mehsullar.get)
en_ucuz = min(mehsullar, key=mehsullar.get)
ortalama = sum(mehsullar.values()) / len(mehsullar)

print("Ən bahalı məhsul:", en_bahali, "-", mehsullar[en_bahali], "AZN")
print("Ən ucuz məhsul:", en_ucuz, "-", mehsullar[en_ucuz], "AZN")
print("Qiymətlərin ortalaması:", round(ortalama, 2), "AZN")
