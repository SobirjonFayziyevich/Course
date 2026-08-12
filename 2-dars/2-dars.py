# Murakkab data turlar
# list, dict, set,  tuple

# ====== Pythonda  listlar ---> [] qavs bilan keladi ========
# li = [1, 2, 3]
# li = [1., 2., 3.3, -23.0]
# li = ["1.", "2"]
# li = ["1.", 2, True, 2.3]
# li = ["1.", 2, True, 2.3, [1, 2]]
# print(type(li))
# print(li)
# ====== Indexsing ========
# print(li[1:4])
# print(li[1:])

# ======= range syntaksisi 3 tagacha argumet qabul qila oladi. =======
# === range(start, stop, step)
# → start dan boshlanadi
# → step bilan oshadi
# → stop ga yetganda (yoki oshib ketsa) to‘xtaydi (stop kirmaydi)

# for i in range(3):
#     print(i)

# for i in range(3, 13, 5): # buyerda 13 soni eksklyuzif bulgani uchun kirmaydi
    # print(i)

# for i in range(3, 12, 1): #bu yerda sonimiz 1gacha qiymatini oshirib beoradi lekin 12 chiqmaydi
#    print(i)

# for i in range(3, 13, 5): #bu yerda sonimiz 1gacha qiymatini oshirib beoradi lekin 12 chiqmaydi
#    print(i)

# for raqam in [3, 13, 5]: #bu yerda for har bir raqamni uqib chiqadi listda qiymat berilsa.
#     print(raqam)

# li = []
# print(li)
# for raqam in range(2, 21, 2):
#     li.append(raqam)   #har bir aylanishda for ichida .raqam qiuymti ruyxatga qushiladi.
# print(li)

# ======= list comprehension === 
# yuqorida kodni bitta qilib yozish logikasi
# li = [i for i in range(2, 21, 2)]
# print(li)

# append()== Bitta elementni list oxiriga qo‘shadi
# Agar list qo‘shsang, uni ichki list sifatida qo‘shadi

# li = [1, 2, 3]
# li.append([4, 5])
# print(li)

# extend() == Boshqa listni ichidagi elementlari bilan qo‘shadi
# Har bir elementni alohida qo‘shadi
# li = [1, 2, 3]
# li.extend([4, 5])
# print(li)

# dictionary -> {}; har bir element bu juft bo'lib kelishi shart: key and value (kalit va qiymat)
# di = {
#     "nomi": "O'zbekiston",
#     "aholi": 36000000,
#     "hududi": 447.4,
#     "Osiyoda": True 
#     } 
# print(type(di))
# print(di)
# print(di["nomi"])
# # print(di["hududi"])
# print(list(di.values())[2])

# for kalit, qiymat in di.items(): # items 2 ta o'zgaruvchi qaytadi: (kalit, qiymat)
#  print(kalit, qiymat)

# di["poytaxt"] = "Toshkent"
# print(di)
# di["poytaxt"] = "Samarqand"
# print(di)


# === tuple -> (); listlarni o'zgartirish mumkin, tuple ni o'zgaritrish imkoni yo'q;
# tu = (2, 3, 4)
# tu[1]  # tuple berilgan qiymatni uzgarieib bulmaydi
# print(tu[1])

# === set {} ichida uniqe valularni saqlab qoladi.====
# li = [2, "2", True, 2, "3", 3.4, "3"]
# ss = {2, "2", True, 2, "3", 3.4, "3"}
# print(set(li))
# #print(ss)

# import numpy as np  # numerical python;
# print(np.unique(li))

# break, continue
# li = [i for i in range(5)]
# a = 0
# for i in li: # [0~9]
#     #if i == 2: break #for loopni uzib quyadi
#     # if (i == 1) or (i == 3): continue 
#     #or
#     if i in [1, 3]: continue # yuqoridagi qatorni qisqartmasi.
#     print(i)


# li = ["olma", "anor", "xurmo"]

# for i, meva in enumerate(li): # enumerate o'zidan 2 ta o'zgaruvchi qaytaradi.
#     # if i == 1: break
#     if i == 1: continue
#     #  1) iterativning indeksi; 2) iterativedagi element 
#     print(f'{i +1} 1- mevaning nomi -> {meva}')


# ===  zip U bir nechta ro‘yxat (yoki boshqa iterable'lar) elementlarini indekslari bo‘yicha juftlab beradi. =====

# viloyatlar = ["Surxandaryo", "Farg'ona", "Namangan", "Sirdaryo"]
# viloyat_markazlari = ["Termiz", "Farg'ona", "Namangan", "Guliston"] 
# viloyat_markazlari2 = ["Termiz", "Farg'ona", "Namangan", "Guliston"] 

# for viloyat, shahar, shahar2 in zip(viloyatlar, viloyat_markazlari, viloyat_markazlari2):
#     print(f"{viloyat} viloyatininf markazi -> {shahar} shahri {shahar2}.")

# for indeks, (viloyat, shahar) in enumerate(zip(viloyatlar, viloyat_markazlari)):
#     print(f"{indeks + 1}-indeksdagi {viloyat} viloyatining markazi -> {shahar} shahri.")

# ismlar = ["Ali", "Vali", "Sami"]
# yoshlar = [20, 25, 30]

# natija = zip(ismlar, yoshlar)
# print(list(natija))

# ismlar = ["Ali", "Vali", "Sami"]
# yoshlar = [20, 25, 30]

# for ism, yosh in zip(ismlar, yoshlar):
#     print(f"{ism} {yosh} yoshda")


# try-except

# li = [i for i in range(10)]

# for i in range(5, 15): # 5 dan boshlab 9 gacha qiymat olib beradi sababi range(10 ga teng qiymati)
#     try: li[i]
#     except: print(f"{i}-indeksda xatolik bor")
#     # print(li[i])



# Object-oriented programming: functions and classes
# def salomlashish(ism = "Ali", familiya = "Valiyev"): print(f"Salom, {ism}, {familiya}!")
# salomlashish(familiya="Olimov ", ism="Vali") # call