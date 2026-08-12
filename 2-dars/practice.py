# List, Tuple, Dictionary

# ======== b =========

# narxlar = [12000, 18000, 10900, 22000]
# narxlar[0] = 13000
# narxlar[2] = 11000
# narxlar[3] = 2000
# print(narxlar)


# ======== c =========

# mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik"]
# yangi_mevalar = ["olcha", "xurmo", "gilos", "nok"]
# for i in yangi_mevalar:
#     mevalar.append(i)
#     print(mevalar)

# ======== d =========

# mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik"]
# mevalar.remove("o'rik")
# mevalar.remove("shaftoli")
# print(mevalar)

# ======== e =========


# mevalar = ["olma", "anor", "anjir", "shaftoli"]
# narxlar = [12000, 18000, 10900, 22000]
# for meva, narx in zip(mevalar, narxlar):
#     print(f"{meva}ning naxi-> {narx}")

# ======== f =========

# avtomobil = ["bmw", "mercedes", "volvo", "general motors", "tesla", "audi"]
# print(sorted(avtomobil))

# ======== g =========

# avtomobil = ["bmw", "mercedes", "volvo", "general motors", "tesla", "audi"]
# print(avtomobil[-3:])

# ======== h =========

# list bu [] ichida xar qanday malumotlarni saqlaydi va malumot qoshish, o'zgartirish, remove qilish mumkin
# tuple () ichida malumot saqlaydi va uni o'zgartirib va saqlab bo'lmaydi.
# set bu {} - tartibsiz va takrorlanmaydigan elementlardan iborat malumotdr.

# ======== i =========

# x = ('olma', 'banan', 'olcha')
# new_list = list(x)
# new_list[1] = 'kivi'
# x = tuple(new_list)
# print(x)

# ======== j =========

# A = ("a", "b", "c")
# B = (1, 2, 3)
# print(A + B)


# ======== k =========

# malumotlar = {
#     "yosh": 20,          # int
#     "bo'y": 1.75,        # float
#     "ism": "Ali"         # string
# }

# print(malumotlar)

# ======== l =========

# car = {
#     "lacceti": "oq",
#     "damas": "qizil",
#     "kia": "qora",
#     "bmw": "kulrang"
# }

# # 4 ta yangi mashina qo‘shamiz
# car["toyota"] = "oq"
# car["mersedes"] = "qora"
# car["audi"] = "qizil"
# car["hyundai"] = "ko'k"

# print(car)

# ======== m =========

# car = {
#     "lacceti": "oq",
#     "damas": "qizil",
#     "kia": "qora",
#     "bmw": "kulrang"
# }

# # Ranglarni o'zgartirish
# car["lacceti"] = "ko'k"
# car["damas"] = "oq"
# car["kia"] = "qizil"
# car["bmw"] = "qora"

# print(car)


# ======== n =========

# car = {
#     "lacceti": "ko'k",
#     "damas": "oq",
#     "kia": "qizil",
#     "bmw": "qora"
# }

# for mashina, rang in car.items():
#     print(mashina, "-", rang)

# ======== o =========

# car = {
#     "lacetti": "oq", 
#     "damas": "qizil",
#       "kia": "qora"
#       }
# for key in car:
#     if len(key) == 3:
#         print(key.upper())
#     else:
#         print(key.capitalize())

# ======== p =========

# davlatlar = {
#     "Uzbekistan": "Toshkent",
#     "Korea": "Seul",
#     "Japan": "Tokio",
#     "France": "Parij",
#     "Germany": "Berlin"
# }

# # 1. Davlatlarni alifbo bo'yicha chiqarish
# print("Davlatlar:")
# for davlat in sorted(davlatlar.keys()):
#     print(davlat)

# print("\nPoytaxtlar:")
# # 2. Poytaxtlarni alifbo bo'yicha chiqarish
# for poytaxt in sorted(davlatlar.values()):
#     print(poytaxt)

# ======== q =========

# otam = {
#     "ism": "Fayzullo",
#     "tugilgan_yil": 1943, 
#     "shahar": "Navoiy",
#     "manzil": "Xatirchi tumani"
# }

# print(f"Otamning ismi {otam['ism']}.")
# print(f"U {otam['tugilgan_yil']}-yilda tug'ilgan.")
# print(f"Toshkent shahrida, {otam['manzil']}da yashaydi.")

# ======== r =========

# otam = {
#     "ism": "Fayzulla",
#     "tug'ilgan_yili": 1943,
#     "viloyat": "Navoiy"
# }

# print(f"Otamning ismi {otam['ism']}, {otam["tug'ilgan_yili"]}-yilda {otam['viloyat']} viloyatida tug'ilgan. ")
