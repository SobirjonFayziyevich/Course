# ==== b ======================
# i = 1

# while True:
#     a = input("Davom etsin, To'xtatish uchun 'yakun' de chiqsin: ")
#     if a == "yakun":
#      break
#     print(i)
# i += 1   

# for i in range(10):
#    print(i)
# ===== c =======================
# x = 1
# while x <= 50:
#     if (x ** 0.5) % 1 == 0:
#         print(x)
#     x += 1x

# ===== d ======================

# num = 0
# num2 = 0

# while True:
#     num = int(input("Son kiriting (to'xtatish uchun!): "))
#     if num == 0:
#         break
#     num += num2
#     num2 += 1

# if num2 > 0:
#     urtacha_son = num / num2
#     print("O'rtacha:", urtacha_son)
# else:
#     print("Hech qanday son kiritilmadi.")    

# ===== e ===================

# juft_son = []
# toq_son = []

# son = 1
# while son <= 10:
#     if son % 2 == 0:
#         juft_son.append(son)
#     else:
#         toq_son.append(son)
#     son += 1
# print("Juft sonlae:", juft_son)
# print("Toq sonlar:", toq_son)


# ===== f ===================

# ismlar = []

# while True:
#     ism = input("Ism kiriting ('yakun' deb yozilganda tugaydi):")

#     if ism.lower() == 'yakun':
#         break

#     ismlar.append(ism)

# print("Kiritilgan ismlar:")
# print(ismlar)

# ===== g ===================

# num = 10

# while num >= 1:
#     print(num)
#     num -= 1 

# ===== h ===================

# num = 1

# while num <= 100:
#     if num % 5 == 0:
#         print(num)
#     num += 1    

# ===== i ===================

# sonlar = [10, 20, 30, 40, 50]

# a = len(sonlar) - 1

# while a >= 0:
#     print(sonlar[a])
#     a -= 1

# ===== j ===================

# suzlar = ["olma", "banana", "shaftoli", "anor", "tarvuz", "gilos"]

# i = 0

# while i < len(suzlar):
#     if len(suzlar[i]) > 5:
#         print(suzlar[i])

#     i += 1


# ===== k ===================

# parol = "john1234"
# while True:
#     kiritilgan_parol = input("Input Password: ")

#     if kiritilgan_parol == parol:
#         print("Welcome! ")
#         break
#     else:
#         print("Mistake Password, Please Again! ")

# ===== l ===================

# num = 1
# har_tortinchi = []

# while num <= 50:
#     print(num)

#     if num % 4 == 0:
#         har_tortinchi.append(num)

#     num += 1
#     print("Har 4-sonlar ruyxati:")
#     print(har_tortinchi)   
# 
# ===== m =================== 

# mevalar = ["olma", "anor","banan"]
# narxlar = [10000, 12000, 15000]

# for meva, narx in zip(mevalar, narxlar):
#     print(meva, "-", narx)


# ===== n =================== 

# import random
# sonlar = []
# i = 0
# while i < 10:
#     son = random.randint(0, 100)
#     sonlar.append(son)
#     i += 1
#     print("Numbers:", sonlar)
#     print("Min number:", min(sonlar))
#     print("Max number:", max(sonlar))
#     print("Average number:", sum(sonlar) / (len(sonlar)))



# ===== o =================== 

# li = ["Assalom Alaykum", "uzbekistan", "Python,"]
# i = 0
# uzun_suz = ""

# while i < len(li):
#     if len (li[i]) > len(uzun_suz):
#         uzun_suz = li[i]
#     i += 1

# print(f"Eng uzun so'z -> {uzun_suz}")