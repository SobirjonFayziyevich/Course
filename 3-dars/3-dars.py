# argument  va parametr
def salomlashish(ism = "Ali", familiya = "Fayziyev"):
    print(f"Salom, {ism}, {familiya}!")

li = [i for i in range(1, 6, 1)]

def orta_arifmetik(li):
    summa = sum(li)
    length = len(li)

    return (summa / length), li #2ta qiymat qaytsa 
javob, list = orta_arifmetik(li=li) # bu joyda ham 2ta qiymat qaytishi kerak .
# print(javob) #javob ga tenglashtirilgan sababli pastda ishlatadigan bulsak.
print(orta_arifmetik(li=li))


raqam = 20  # global variable bu sababi functiondan tashqarida yashaydi
print(raqam)

def qiymatni_uzgartirish():
   #print(f"global qiymat -> {raqam}")  # bu global varaible 
   raqam = 30  # local variable hisoblanadi functiondan tashqariga qichib ketmaydi.
   print(raqam)
   print(f"local qiymat -> {raqam}")
qiymatni_uzgartirish()   


# Classlar -> functiondan iborat bulgan oopning bir turi. Classlar ichida bir qancha functionlar buladi. 

class Avtomabil:

# self - function ichidagi local variableni class ichidagi global variable ga alantiradi.
    def __init__(self, model,rang): # initialize -- self
        self.model = model
        self.rang = rang
    def malumot(self):    
        print(f"avtomobilni modeli -> {self.model} va rangi {self.rang}")

avtomobil = Avtomabil(model="lacetti", rang = "qora") #call - chaqirishni ifodalaydi         
avtomobil.malumot()

class Shaxs:

    def __init__(self,ism, familiya):
        self.name = ism
        self.familiya = familiya

    def tanishtir(self): #Agarda manashu tanishtir fnctionda self qolib ketsa bu Shaxs classiga tegishli bulmay qoladi,
        print(f"Salom , men {self.name} {self.familiya}man.")

shaxs = Shaxs(ism = "John", familiya="Johny")
shaxs.tanishtir()            


# Inheritance => meros olish,

class Ishchi(Shaxs): # butta Ishchi Shaxsdan meros ol oqda shunga Shaxsning barcha belgilarini oladi.
    def __init__(self, ism, familiya,lavozim):

        super().__init__(ism, familiya)
        self.lavozim = lavozim

    def malumot(self):
        print(f"Ishchining lavozimi -> {self.lavozim}")

ishchi = Ishchi("Ali", "Valiev", lavozim="Bugaltir")
ishchi.malumot()
ishchi.tanishtir()       

# Decorators -> dekoratorlar @belgilanadi

class Matematika:
    
    def __init__(self,son):
        self.son = son
# classni ichida qancha function bulmasin staticmethodga bug'liq bulmaydi.
# @staticmethod dekoratori bu metod klass yoki obyekt holatiga (self yoki cls) bog'liq emasligini bildiradi.
    @staticmethod 
    def kvadrat(son):
        return son ** 2
    
    def qoshish(self):
        return self.son + self.son
    
# print(Matematika.kvadrat(son = 2))
m = Matematika(son = 3)
print(m.qoshish())
print(m.kvadrat(son = 5))

class Kitob:

   def __init__(self, nomi, muallif):
       self.nomi = nomi
       self.muallif = muallif
   
   def malumot(self):   
       print(f"Kitobning nomi -> {self.nomi}va muallifi {self.muallif}")

   @classmethod
   def malumotdan(cls, malumot):
       title, author = malumot.split(",")
       return cls(title, author)
   
#    malumot = "O'tgan kunlar, Abdulla Qodiriy"
#    splitted = malumot.split(",")
#    print(splitted)

kitob_1 = Kitob(nomi = "O'tgan kunlar", muallif = "Abdulla Qodiriy")
kitob_1.malumot() 

kitob_2 = Kitob.malumotdan(malumot = 'Mehrobdan chayonn, Abdullay Qodiriy')
kitob_2.malumot()



class Hisob:

    raqam = 9

    @staticmethod # self ham cls ham olmaydi. Odiiy funksiya bulib ishkaydi.
    def uch_marta(son):
        return son * 3
    
    @classmethod # birinchi parametr cls oladi va class bilan ishlaydi
    def raqam_bilan(cls, son):
        return son * cls.raqam
    
print(Hisob.uch_marta(son = 5))  
print(Hisob.raqam_bilan(son = 5))  