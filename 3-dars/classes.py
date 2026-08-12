#b 
class Transport:
    def __init__(self):
        print("Transport obyekti yaratildi")

#c
class Transport:
    def __init__(self, maksimum_tezlik, masofa):
        self.maksimum_tezlik = maksimum_tezlik
        self.masofa = masofa
        print("Transport obyekti yaratildi")

mashina = Transport(180, 500)
print(mashina.maksimum_tezlik)  
print(mashina.masofa)           

#d
class Transport:
    def __init__(self, maksimum_tezlik, masofa):
        self.maksimum_tezlik = maksimum_tezlik
        self.masofa = masofa
        
class YengilAvto(Transport):
    def tezlikni_yoz(self):
        return self.maksimum_tezlik * 1.5   # 0.5 marta ko'proq

    def masofani_yoz(self):
        return self.masofa * 1.2            # 0.2 marta ko'proq
    
avto = YengilAvto(120, 400)
print(avto.tezlikni_yoz())    
print(avto.masofani_yoz()) 

#e
class SUV(Transport):
    def __init__(self, maksimum_tezlik, masofa, kafolat_yili):
        super().__init__(maksimum_tezlik, masofa)
        self.kafolat_yili = kafolat_yili

    def yaroqlilik_muddati(self):
        return (self.maksimum_tezlik / self.masofa) * self.kafolat_yili
#f
    def tezlikni_yoz(self):          
        return self.maksimum_tezlik * 1.3


suv = SUV(150, 500, 3)
print(suv.yaroqlilik_muddati())   # 0.9
print(suv.tezlikni_yoz())        

#g
class Tortburchak:
    def __init__(self, uzunlik, kenglik):
        self.uzunlik = uzunlik
        self.kenglik = kenglik

    def maydonni_hisoblash(self):
        return self.uzunlik * self.kenglik

    def perimetrni_hisoblash(self):
        return 2 * (self.uzunlik + self.kenglik)

t = Tortburchak(5, 3)
print(t.maydonni_hisoblash())      
print(t.perimetrni_hisoblash())    

#h
class Hisob:
    def __init__(self, hisob_raqami, balans=0):
        self.hisob_raqami = hisob_raqami
        self.balans = balans

    def depozit(self, summa):
        self.balans += summa
        return self.balans

    def yechish(self, summa):
        if summa > self.balans:
            print("Balansda yetarli mablag' yo'q!")
            return self.balans
        self.balans -= summa
        return self.balans

h = Hisob("UZ123456", 1000)
h.depozit(500)
print(h.balans)   
h.yechish(300)
print(h.balans)   

#i
class Kitob:
    def __init__(self, nomi, muallifi, narxi):
        self.nomi = nomi
        self.muallifi = muallifi
        self.narxi = narxi

    def chegirmadagi_narx(self, chegirma_foizi):
        return self.narxi - (self.narxi * chegirma_foizi / 100)

kitob = Kitob("Python asoslari", "John Smith", 50000)
print(kitob.chegirmadagi_narx(20))  

#j
class Matematika:
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def qoshish(self):
        return self.son1 + self.son2

    def ayirish(self):
        return self.son1 - self.son2

    def kopaytirish(self):
        return self.son1 * self.son2

    def bolish(self):
        if self.son2 == 0:
            return "Nolga bo'lish mumkin emas"
        return self.son1 / self.son2

m = Matematika(10, 5)
print(m.qoshish())       
print(m.ayirish())       
print(m.kopaytirish())   
print(m.bolish())        

#k 
class Inson:
    def __init__(self, ism, familiya, tugilgan_yil):
        self.ism = ism
        self.familiya = familiya
        self.tugilgan_yil = tugilgan_yil

    def fullname_yoz(self):
        return f"{self.ism} {self.familiya}"

    def yoshni_yoz(self, hozirgi_yil=2026):
        return hozirgi_yil - self.tugilgan_yil

inson = Inson("Ali", "Valiyev", 2000)
print(inson.fullname_yoz())     
print(inson.yoshni_yoz(2026))   

#l
class Student(Inson):
    def __init__(self, ism, familiya, tugilgan_yil, hozirgi_yil, universitet_yili):
        super().__init__(ism, familiya, tugilgan_yil)
        self.hozirgi_yil = hozirgi_yil
        self.universitet_yili = universitet_yili

    def yilni_yoz(self):
        return self.hozirgi_yil

    def majorni_yoz(self):
        return self.universitet_yili

student = Student("Ali", "Valiyev", 2000, 2025, 3)
print(student.yilni_yoz())      
print(student.majorni_yoz())    

#m
class Update:
    def __init__(self, year):
        self.year = year

    def kursni_yoz(self, student):
        farq = self.year - student.hozirgi_yil
        return student.universitet_yili + farq

student = Student("Ali", "Valiyev", 2000, 2026, 2)
update = Update(2027)
print(update.kursni_yoz(student))  

#n
class Ishchi:
    def __init__(self, ismi, soatlik_ish_haqi, ishlagan_soat):
        self.ismi = ismi
        self.soatlik_ish_haqi = soatlik_ish_haqi
        self.ishlagan_soat = ishlagan_soat

    def kunlik_ish_haqi(self):
        return self.soatlik_ish_haqi * self.ishlagan_soat

    def oylik_ish_haqi(self):
        return self.kunlik_ish_haqi() * 22   # 22 ish kuni

    def yillik_ish_haqi(self):
        return self.oylik_ish_haqi() * 12

ishchi = Ishchi("Vali", 20000, 8)
print(ishchi.kunlik_ish_haqi())   
print(ishchi.oylik_ish_haqi())    
print(ishchi.yillik_ish_haqi())   

#o
class Shaxs:
    def __init__(self, ism, jinsi, manzil):
        self.ism = ism
        self.jinsi = jinsi
        self.manzil = manzil

    def tanishuv(self):
        return f"Salom, mening ismim {self.ism}, jinsim {self.jinsi}, men {self.manzil}da yashayman."

shaxs = Shaxs("Sobirjon", "erkak", "Navoiy")
print(shaxs.tanishuv())

#p
class Doira:
    def __init__(self, radius):
        self.radius = radius

    def maydon(self):
        return 3.14 * (self.radius ** 2)

    def perimetr(self):
        return 2 * 3.14 * self.radius

doira = Doira(5)
print(doira.maydon())      
print(doira.perimetr())   

#q
class IjtimoiyTarmoqFoydalanuvchisi:
    def __init__(self, ism, yosh, email):
        self.ism = ism
        self.yosh = yosh
        self.email = email

    def profil(self):
        return f"Ism: {self.ism}, Yosh: {self.yosh}, Email: {self.email}"

foydalanuvchi = IjtimoiyTarmoqFoydalanuvchisi("Sobirjon", 31, "sobirjon@mail.com")
print(foydalanuvchi.profil())

#r
class AvtoPark:
    def __init__(self):
        self.avtolar = []

    def avto_qoshish(self, avto):
        self.avtolar.append(avto)

    def avtolar_royxati(self):
        for avto in self.avtolar:
            print(f"Tezlik: {avto.maksimum_tezlik}, Masofa: {avto.masofa}")

park = AvtoPark()
park.avto_qoshish(Transport(180, 500))
park.avto_qoshish(Transport(120, 300))
park.avtolar_royxati()

#s
class Hisoblagich:
    def __init__(self):
        self.qiymat = 0

    def increment(self):
        self.qiymat += 1
        return self.qiymat

    def decrement(self):
        self.qiymat -= 1
        return self.qiymat

h = Hisoblagich()
h.increment()
h.increment()
h.decrement()
print(h.qiymat)  

#t
class Boshqaruvchi(Ishchi):
    def __init__(self, ismi, soatlik_ish_haqi, ishlagan_soat, bolim, bonus):
        super().__init__(ismi, soatlik_ish_haqi, ishlagan_soat)
        self.bolim = bolim
        self.bonus = bonus

    def yillik_daromad(self):
        return self.yillik_ish_haqi() + self.bonus

boshqaruvchi = Boshqaruvchi("Sardor", 30000, 8, "IT", 5000000)
print(boshqaruvchi.yillik_daromad())

#u
class Narx:
    def __init__(self, asl_narx, soliq_foizi, chegirma_foizi):
        self.asl_narx = asl_narx
        self.soliq_foizi = soliq_foizi
        self.chegirma_foizi = chegirma_foizi

    def yakuniy_narx(self):
        narx_chegirmadan_keyin = self.asl_narx - (self.asl_narx * self.chegirma_foizi / 100)
        yakuniy = narx_chegirmadan_keyin + (narx_chegirmadan_keyin * self.soliq_foizi / 100)
        return yakuniy


# Misol
narx = Narx(100000, 12, 10)
print(narx.yakuniy_narx())  # 100800.0

#v
import random

class BankHisobi:
    def __init__(self, ism, balans=0):
        self.ism = ism
        self.balans = balans

    def hisob_raqamini_ber(self):
        return random.randint(1000000, 9999999999)

hisob = BankHisobi("Sobirjon", 50000)
print(hisob.hisob_raqamini_ber())

#w
class Mahsulot:
    def __init__(self, nom, narx, soni):
        self.nom = nom
        self.narx = narx
        self.soni = soni

    def summani_hisobla(self):
        return self.narx * self.soni

mahsulot = Mahsulot("Noutbuk", 8000000, 3)
print(mahsulot.summani_hisobla()) 

#x
class Fayl:
    def __init__(self, fayl_nomi, fayl_turi):
        self.fayl_nomi = fayl_nomi
        self.fayl_turi = fayl_turi

    def toliq_nomi(self):
        return f"{self.fayl_nomi}.{self.fayl_turi}"

fayl = Fayl("myfile", "txt")
print(fayl.toliq_nomi())  
