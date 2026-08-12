# try and expect
#try → xato bo‘lishi mumkin bo‘lgan kod.
#except → xatoni ushlaydi.
#else → xato bo‘lmasa ishlaydi.
#finally → har doim ishlaydi.

# ============= b ===========
# try:
#     a = int(input("birinchi sonni kiritsin; "))
#     b = int(input("ikkinchi sonni kiritsin; "))
#     result = a / b
#     print(result)
# except:
#     print("Mos xatolik: ") 
# 

# ============= c ===========   

# li = ["maktab", "bog'cha", "university", "kollej", "litsey"]
# try:
#     a = int(input("nechinchi elementni kurmoqchisiz: "))
#     print(li[a])
# except:print("buday index mavjud emas: ")    

# ============= d ===========   

# raqamlar = [12, 'uch', 5.6, False, 10, '7', None]

# natija = []

# for i in raqamlar:
#     try:
#         qiymat = int(i)
#         natija.append(qiymat)
#     except:
#         print(f"Xatolik: {i} ni int ga ogirish imkonsiz: ")    


# ============= e ===========   

# fayl_nomi = input("Fayl nomini kiriting!")

# try:
#    with open(fayl_nomi, "r") as fayl:
#     print(fayl.read())
# except FileNotFoundError:
#     print("fail not found")     

# ============= f ===========   

# try:
#     son1 = float(input("1-sonni kiriting:"))
#     son2 = float(input("2-sonni kiriting:"))
#     son3 = float(input("3-sonni kiriting:"))

#     print("Kiritilgan raqamlar:", son1,son2,son3)
# except:
#     print("Faqat raqam kiriting! ")

# ============= g ===========   

# import math

# for i in range(5):
#     try:
#         son = float(input(f"{i+1}-sonni kiriting: "))
#         print("Ildizi:", math.sqrt(son))
#     except:
#         print("Manfiy sonni ildizi olinmadi")    

# ============= h ===========   

# lugat = {
#     "a": 1,
#     "b": 2,
#     "c": 3
# }

# try:
#     kalit = input("Kalitni kiriting: ")
#     print(lugat[kalit])
# except:
#     print("Bunday kalit yo'q")

# ============= i ===========   

# try:
#     yosh = int(input("Yoshingizni kiriting: "))
#     print("Tug'ilgan yilingiz:", 2025 - yosh)
# except:
#     print("Yoshni raqam ko'rinishida kiriting!")

# ============= j ===========   

# royxat = ["10", 5, "salom", 2.5, None]

# for element in royxat:
#     try:
#         print(element / 10)
#     except:
#         print(f"Bo'lib bo'lmadi: {element} — turi {type(element).__name__}")