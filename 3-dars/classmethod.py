#classmathod and @staticmethod

#a
class MathUtils:
    @staticmethod
    def max_son(a, b):
        return a if a > b else b
    
print(MathUtils.max_son(15,40))
print(MathUtils.max_son(100, 50))

#b
class MathUtils:
    @staticmethod
    def max_son(a, b):
        return a if a > b else b


class Converter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32
print(MathUtils.max_son(45, 60))              
print(Converter.celsius_to_fahrenheit(25))  

#c
class IsmTekshirish:
    @staticmethod
    def ism_tekshir(ism):
        return len(ism) > 3
print(IsmTekshirish.ism_tekshir("Ali"))
print(IsmTekshirish.ism_tekshir("Saidamir"))

#d
class Shakl:
    @staticmethod
    def doira_maydon(radius):
        return 3.14 * (radius ** 2)
print(Shakl.doira_maydon(5))
print(Shakl.doira_maydon(10))

#e
class Foydalanuvchi:
    def __init__(self,ism, email):
        self.ism = ism
        self.email = email

    @classmethod
    def stringdan(cls, malumot):
        ism, email = malumot.split(",")
        return cls(ism, email)
foydalanuvchi = Foydalanuvchi.stringdan("Saidamir,saidamir@gmail.com")

print(foydalanuvchi.ism)
print(foydalanuvchi.email)

#f
class Mahsulot:
    def __init__(self, nom, narx):
        self.nom = nom
        self.narx = narx

    @classmethod
    def dictdan(cls, malumot):
        return cls(malumot['nom'], malumot['narx'])

mahsulot = Mahsulot.dictdan({'nom': 'non', 'narx': 3000})
print(mahsulot.nom)   
print(mahsulot.narx)   

#g
class Talaba:
    def __init__(self, ism, kursi, gpa):
        self.ism = ism
        self.kursi = kursi
        self.gpa = gpa

    @staticmethod
    def baho_ber(gpa):
        return "Yaxshi o'quvchi" if gpa > 3.5 else "O'rtacha"

talaba = Talaba("Vali", 2, 3.8)
print(Talaba.baho_ber(talaba.gpa))   
print(Talaba.baho_ber(3.0))          

#h
class Hisoblagich:
    sonlar = []   # class atributi - barcha obyektlar uchun umumiy

    @classmethod
    def add_number(cls, son):
        cls.sonlar.append(son)
        return cls.sonlar
Hisoblagich.add_number(5)
Hisoblagich.add_number(10)
Hisoblagich.add_number(15)
print(Hisoblagich.sonlar)   

#i
class Ishchi:
    def __init__(self, ism, soatlik_haq, soat):
        self.ism = ism
        self.soatlik_haq = soatlik_haq
        self.soat = soat

    @staticmethod
    def hisobla(haq, soat):
        return haq * soat
    
ishchi = Ishchi("Sardor", 25000, 8)
umumiy_haq = Ishchi.hisobla(ishchi.soatlik_haq, ishchi.soat)
print(umumiy_haq)   

#j
class Narxlar:
    valyuta_kursi = 15560

    @classmethod
    def valyuta_kursini_yangila(cls, yangi_kurs):
        cls.valyuta_kursi = yangi_kurs
        return cls.valyuta_kursi

print(Narxlar.valyuta_kursi)
Narxlar.valyuta_kursini_yangila(15600)
print(Narxlar.valyuta_kursi)