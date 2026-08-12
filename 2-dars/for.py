# ====== b ===========

# kv = []

# for i in range(1, 11):
#     kv.append(i ** 2)

# print(kv)

# ====== c ===========

# kub = []
# yigindi = 0

# for i in range(1, 11):
#     kub.append(i ** 3)
#     print(f" Yig'indi:", yigindi)
#     print("Kuplar ruyxati:", kub)

# ====== d ===========

# import math

# ildizlar = []

# for i in range(1, 11):
#     ildiz = math.sqrt(i)  #kvadrat sonlar ildizi hisoblashdagi arifmetika
#     ildizlar.append(ildiz)
# print(ildizlar)    

# ====== e ===========

# karrali_sonalar = []

# for i in range(0, 21):
#     if i % 5 ==0: #i sonini 5 ga bulgandagi qoldiqni beradi
#         karrali_sonalar.append(i)

# print(karrali_sonalar)        

# ====== f ===========

# ismlar = []

# for i in range(5):
#     ism = input("Ismlarni kiriting: ")
#     ismlar.append(ism)
# print(ismlar)

# ====== g ===========

# ismlar = ['ali', 'vali', 'soli', 'dali']

# for ism in ismlar:
#     print(ism + " - Salom! ")

# ====== h ===========

# raqamlar = [23, 22, 11, 4, 56, 78, 3]

# for son in raqamlar:
#     if son > 10:
#         print(son)

# ====== i ===========        

# toq_sonlar = []
# juft_sonlar = []

# for i in range(5):
#     son = int(input("Sonlarni kiriting! "))
#     if son % 2 == 0:
#         juft_sonlar.append(son)
#     else:
#         toq_sonlar.append(son)

# print("Toq sonlar:", toq_sonlar)
# print(" Juft sonlar:", juft_sonlar)            


# ====== j ===========        

# natijalar = []

# for i in range(1, 11):
#     natijalar.append(i * 2)

# print(natijalar)    

# ====== k ===========      

# karrali_sonlar = []

# for i in range(1, 21):
#     if i % 3 == 0 and i % 4 == 0: # 3 g ham 4 ga ham bulinishi lozim.
#         karrali_sonlar.append(i)
# print(karrali_sonlar)        

# ====== l ===========   
# products = ['non', 'sut', 'yog', 'olma', 'banan', 'shakar']

# for mahsulot in products:
#     if len(mahsulot) > 3:
#         print(mahsulot)


# ====== m ===========  

# ismlar = ['Ali', 'Sobirjon', 'Alinur', 'Sidamir']

# for ism in ismlar:
#     print(ism, "uzunligi:", len(ism))

# ====== n ===========  

# sonlar = []
# yigindi = 0

# for i in range(5):
#     num = int(input("Istalga sonni kiriting: "))
#     sonlar.append(num)
#     yigindi += num
# orta = yigindi / 5

# print("kiritilgan sonlar:", sonlar)
# print("O'rtach qiymat:", orta)

# ====== o ===========  

# narxlar = [10000, 25000, 30000, 15000, 45000]
# yangi_narxlar = []

# for narx in narxlar:
#     yangi_narx = narx * 15
#     yangi_narxlar.append(yangi_narx)

# print(yangi_narxlar)

# ====== p =========== 

# for i in range(1, 11):
#     print(f"3 * {i} = {3 * i}")


# ====== q =========== 

# for i in range(1, 10):
#     for a in range(1, 10):
#         print(f"{i} * {a} = {i * a}", end="\t")

# ====== r =========== 

# sozlar = []

# for i in range(5):
#     soz = input(" Sozni kiriting: ")
#     sozlar.append(soz)
# for soz in sozlar:
#     print(soz.upper())



# ====== s =========== 

# for i in range(0, 11):
#     if i > 1:
#         tub = True
#         for a in range(2, i):
#             if i % a == 0:
#                 tub = False
#                 break

#         if tub:
#             print(i)        



# ====== t  =========== 

# for i in range(1, 101):
#     if i % 7 == 0 and i % 5 != 0:
#         print(i) 