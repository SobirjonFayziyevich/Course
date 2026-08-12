# print("Hello!")

# print("Assalomu alaykum!") Ctrl + / Cmd + /
# print("Assalomu alaykum!") Shift + 3
# print("Assalomu alaykum!") Shift + 3
# print("Assalomu alaykum!") Shift + 3
# print("Assalomu alaykum!") Shift + 3
# print("Assalomu alaykum!") Shift + 3

# print("Assalomu alaykum!") Shift + 3

# Python eng sodda data turlari: 
# 1) integer - raqam (0~9); butun sonlar; 
# 2) float
# 3) boolean
# 4) string

# ============ integer ============
# raqam = -20
# print(raqam)
# print(type(raqam)) # reserved word

# ======== float ==============
# qoldiqli_son = -2.1
# print(qoldiqli_son)
# print(type(qoldiqli_son)) # reserved word

# ======== boolean faqatgina 2 ta qiymat qabul bo'ladi ==============
# boolean = True
# print(boolean)
# print(type(boolean)) # reserved word
# print(boolean == 1)

# print(10 > 9)   : True
# print(10 == 9)  : False
# print(10 < 9)   : False

# string harflar (raqamlar, qoldiqli sonlar...) (character)dan tashkil topgan data turi
# integer = 33
# print(type(integer))
# print(integer)
# string = '33' # integer
# print(string)
# print(type(string))


# salom = "Assalomu alaykum! 222 2.3"
# print(type(salom))

# ========== f-string ==========

# print(f"2 + 3 = {2 + 3}")

# yosh = 20
# print(f"Keyingi yil {yosh + 1} yosh bo'lasiz")

# ism = "ali"
# print(f"{ism.upper()}")

# ========== Agar figurniy qavsning o‘zini chiqarish kerak bo‘lsa, uni ikki marta yoziladi: ========

# print(f"{{salom}}")

# shahar  = "Toshkent" # string
# harorat = 21 # integer
# bulutli = True # boolean
# namlik  = 22.2 # float

# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")
# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")
# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")
# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")
# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")
# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")
# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")
# print("Seoulda bugun harorat 16 daraja issiq va bulutli hamda namlik 10.2 bo'ldi")

# # f-string doim curly brackets (figurniy qavslar) bilan ishlatiladi va ular doim o'zgaruvchini anglatadi
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")
# print(f"{shahar}da bugun harorat {harorat} daraja issiq va {bulutli} hamda namlik {namlik} bo'ldi")

# print(f"{shahar} shahrida bugungi harorat {harorat} daraja issiq va namlik {namlik} dajarada bo'ldi {bulutli}")

# ======= indexing -> pythonda [] square bracketsga raqam kiritiladi. pythonda indexing doimo 0 dan boshladi =========

# string = "Python va java"
# print(len(string))
# print(len(string[6]))
# print(string[7:]) 
# print(string[-4:])
# ism1 = "Ali"
# ism2 = "Vali"
# print(f"{ism1} {string[-4:]}ni yaxshi ko'radi")
# print(f"{ism2} {string[:6]}ni yaxshi ko'radi")

# print(string.upper())
# print(string.lower())
# print(string.replace("java script", "c++"))
# print(string.capitalize())
# print(string.count("a"))

# while har doim to'g'ri bo'lgan holatda cheksiz davom (loop) etadi.
# while ning shartini buzadigan mantiqni yaratishim kerak;

# i = 1
# while i < 6:
#   print(i)
#   i += 1


# raqam = 5
# while raqam > 0: # ctrl + c ; control + c
#     # print(raqam)
#     raqam = raqam - 1 # 2; 3; 4;
#     raqam -= 1

# bolinuvchi = 10
# boluvchi = 4
# bolinma = bolinuvchi / boluvchi
# print(bolinma)

# print((bolinuvchi % boluvchi) == 2) 

# shartli operatorlar if - elif - else
# harorat = 15

# if harorat < 10: # shartlar qanoatlantirilishi tekshiradi
#     print("Sovuq")
# elif harorat < 15 or harorat > 10:  # har bir shart bajarilishi kerak; har bir shartdan True qayitishi kk 
#     print("Iliq")
# elif harorat < 20:
#     print("Issiq")
# else: print("Qaynoq")

# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# username = "John"

# if len(username) > 0:
#   print(f"Welcome, {username}!")
# else:
#   print("Error: Username cannot be empty")