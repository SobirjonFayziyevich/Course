# enumerate and zip

# =========== b =========

# num = list(range(100))

# for index, qiymat in enumerate(num):
#     if index in [20, 40, 60, 80]:
#         print(f"Index: {index}, Qiymat: {qiymat}")

# =========== c ==========

# sonlar = [2, 7, 9, 11, 10, 16, 20]

# for son in sonlar:
#     if son % 2 != 0:
#         continue
#     print(son)

# =========== d ==========

# sonlar = [1, 3, 5, 4, 20, 15,]

# for son in sonlar:
#     if son % 5 == 0:
#         print("Topild:", son)
#         break
#     print(son)

# =========== e ==========

# cars = [
#     "chevrolet",
#     'bmw',
#     'tayota',
#     'nissan',
#     'cobalt',
#     'sonata',
#     'tesla',
#     'ford',
#     'kia',
#     'Mercedes'
#     ]
# for tartib, nom in enumerate(cars, start=1):
#     print(tartib, '-', nom)

# =========== f ==========

# ismlar = ["Ali", "Vali", "Hasan", "Husan", "Madina"]
# ballar = [85, 55, 80, 90, 100]

# for ism, ball in zip(ismlar, ballar):
#     print(ism, '-', ball)

# =========== g ==========

# names = ['ali', 'vali', 'hasan', 'husan', 'madina']
# balls = [85, 55, 80, 90, 100]

# for name, ball in zip(names, balls):
#     if ball > 60:
#         holat = "O'tdi"
#     else:
#         holat = "O'tmadi"
# print(f"{name}: {ball}, holati: {holat} ")            

# =========== i  ===========

# uquvchilar = {
#     "Ali": {"Adabiyot": 80, "Fizika": 70, "Ingliz tili": 90},
#     "Vali": {"Adabiyot": 85, "Fizika": 75, "Ingliz tili": 60},
#     "Hasan": {"Adabiyot": 70, "Fizika": 65, "Ingliz tili": 85},

# }

# for ism, fanlar in uquvchilar.items():
#     print(f"{ism} fanlar buyicha baholari: ")

#     for fan, baho in fanlar.items():
#         print(f"{fan}: {baho}")

# =========== l  ===========

# sonlar = list(range(1, 101))

# for indeks, son in enumerate(sonlar):
#     if indeks % 3 == 0:
#         print(f"Indeks: {indeks}, Son:{son}")