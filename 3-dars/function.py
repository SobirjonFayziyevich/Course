#b
a = int(input("1-raqamni kiriting: "))
b = int(input("2-raqamni kiriting: "))

def kopaytma(a, b):
    try:
        result = a / b
        if a % b == 0:
            return result
        return 0
    except ZeroDivisionError:
        return 0

print(kopaytma(a, b))

#c

def ikkiga_bol(lst):
    yangi_list = []
    for son in lst:
        yangi_list.append(son / 2)
    return yangi_list

sonlar =[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(ikkiga_bol(sonlar))    

#d 
def ikki_marta(matn):
    result = ''
    for i in matn:
        result += i * 2
    return result
text = input("matnni kiriting:")
print(ikki_marta("salom"))

#e

name = input("isminngiz\n")
familiya = input("familiya\n")
year = input("yilinggiz\n")

def infor(name, familiya, year):
    return(f"ismingiz {name} va familiyangiz {familiya}, tug'ilgan yilim esa {year}")
print(infor(name,familiya,year))


#f

def raqamlarni_ol(matn):
    natija = []
    for soz in matn.split():
        if soz.isdigit():
            natija.append(int(soz))
    return natija

# Misol
matn = "Men 2023-yilda 20 yosh edim"
print(raqamlarni_ol(matn))

#g

def faqat_harflar(matn):
    natija = ""
    for belgi in matn:
        if belgi.isalpha():
            natija += belgi
    return natija

# Misol
matn = "abc123def45gh6"
print(faqat_harflar(matn))

#h

def bosh_harf_katta(matn):
    sozlar = matn.split()
    yangi = []

    for soz in sozlar:
        yangi.append(soz.capitalize())

    return " ".join(yangi)

# Misol
matn = "men python dasturlashni o'rganyapman"
print(bosh_harf_katta(matn))

# i
def umumiy_elementlar(list1, list2):
    return list(set(list1) & set (list2))
print(umumiy_elementlar([1,2,3,4,5,6], [2,4,5,6,3,66,]))

#j 
def musbat_toq_sonlar(son):
     return [i for i in son if i > 0 and i % 2 == 1]
print(musbat_toq_sonlar([-3, -2, -1, 0, 1, 2, 3,]))

#k
def suz_soni(matn):
    return(len(matn.split()))
suz = "good morning"
print(suz_soni(suz))

#l 
def min_max_numbers(sonlar):
    return min(sonlar), max(sonlar)
sonlar = [3,4,5,6,7,8,9,1,0,11,90]
kichik, katta = min_max_numbers(sonlar)
print(f"Eng kichik: {kichik}, Eng katta {katta}")

#m
def indeks_daraja(sonlar):
    natija = []
    for indeks, son in enumerate(sonlar):
        if indeks % 2 == 0: #juft indeks
            natija.append(son ** 2)
        else:
            natija.append(son ** 3)
    return natija

sonlar = [2,3,4,5,6,7]
print(indeks_daraja(sonlar))           

#yoki

def indeks_daraja2(sonlar):
    return [son ** 2 if indeks % 2 == 0 else son ** 3
            for indeks, son in enumerate(sonlar)]

print(indeks_daraja2([2,3,4,5,6,7]))

#n
def a_harfli_shaharlar(shaharlar):
    return [shahar for shahar in shaharlar if shahar.startswith("A")]
shaharlar = ["Amsterdam", "Berlin", "Angliya", "Toshkent","AQSH", "Toronto", "Avstraliya","Almaty"]
print(a_harfli_shaharlar(shaharlar))
 
#o

def unli_harflar_uchirish(text):
    unlilar = "dscaiuegdboa"
    return "".join(harf for harf in text if harf not in unlilar)
text = "Hello Python"
print(unli_harflar_uchirish(text))    

#p

def eng_kop_takrorlangan_harf(matn):
    matn = matn.replace(" ", "").lower()
    harflar_soni = {}
    for harf in matn:
        harflar_soni[harf] = harflar_soni.get(harf, 0) + 1
    
    eng_kop_harf = max(harflar_soni, key=harflar_soni.get)
    return eng_kop_harf

print(eng_kop_takrorlangan_harf("Salom Dunyo"))  # o (2 marta uchraydi)

#q

def musbat_manfiy_nol(sonlar):
    natija = []
    for son in sonlar:
        if son > 0:
            natija.append("musbat")
        elif son < 0:
            natija.append("manfiy")
        else:
            natija.append("nol")
    return natija


# Misol
sonlar = [5, -3, 0, 8, -1, 0, 12, -7, 4, -9]
print(musbat_manfiy_nol(sonlar))

#r

def son_ekanligini_tekshirish(matn):
    try:
        int(matn)
        return True
    except ValueError:
        return False


# Misol
print(son_ekanligini_tekshirish("123"))     
print(son_ekanligini_tekshirish("-45"))     
print(son_ekanligini_tekshirish("12.5"))   
print(son_ekanligini_tekshirish("abc"))     

#s
a =[1,2,3,4,4]
b= [0,2,3,2,5,6,7]
def finding(lis1, lis2):
    return [x for x in lis1 if x not in lis2]
print(finding(a,b))

#t
def soz_uzunliklari(matn):
    sozlar = matn.split()
    return {soz: len(soz) for soz in sozlar}

matn = "Men Python o'rganaman"
print(soz_uzunliklari(matn))

#u
import random
sonlar = [random.randint(1,100) for i in range(100)]
def uchgaboluv(x):
    return [i for i in x if i % 3 == 0]
print(uchgaboluv(sonlar))

#v
def takroriy_yoqligini_tekshirish(lst):
    return len(lst) == len(set(lst))

print(takroriy_yoqligini_tekshirish([1, 2, 3, 4, 5]))     
print(takroriy_yoqligini_tekshirish([1, 2, 2, 3, 4]))     

#w
def harf_soni(x):
    soni = {}
    for i in x:
        soni[i]=soni.get(i,0)+1
    return soni
strr = 'sajsadnklasdiaodnalndoasnd'
print(harf_soni(strr))

