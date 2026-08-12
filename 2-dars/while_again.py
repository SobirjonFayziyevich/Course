#b
for i in range(10):
    print(i)

#c
for i in range(11,20,2):
    print(i)

#d
for i in range(1000,1020,2):
    print(i)

#e 
i = -10

while i <= 0:
    print(i)
    i += 1

#f
i = -10

while i <= 0:
    if i % 2 != 0:
        print(i)
    i += 1 

#g    
i = 0

while i < 8:
    print(i)
    i+=3
#yoki    
for i in range(0,8,3):
    print(i)

#h
for i in range(12,41,4): #10dan 40gacha 4ga qoldiqsiz bulinish kerak edi lekin 10 qoldiqli bulgani sababli 12dan boshlab bulinma oldim.
    print(i)
# 
i = 12
while i < 40:
    print(i)
    i += 4

#i
for i in range(1,4):
    print(i**2)     
#yoki
i = 1
while i < 4:
    print(i*i)
    i+=1
#k
for i in range(8,12):
    print(i**0.5)

#yoki
import math

i = 8 
while i <= 12:
    print(math.sqrt(i))
    i+=1
#yoki
i = 8

while i <= 12:
    print(i**0.5)
    i+=1

#j
i = 2
while i <= 5:
    print(i**3)
    i += 1    
#yoki
for i in range(2,5):
    print(i**3)    

#l
i = 100

while i <= 120:
    print(i ** 1/3) # kup ildizini 1/3 qilib olsa ham buladi 0.33 qilib olsa ham buladi.
    i+=1


#m va p gacha 
list = []
nums = 0
while nums <= 10:
    list.append(nums)
    nums+=1
print(list)
a_max=max(list)
b_min=min(list)
mysum=sum(list) 
mean= sum(list) / len(list)
print(max)
print(min)
print(mysum)
print(mean)

#q
i = 1
while i < 20:
    print(i)
    i+=1

#r     
i = 1
while i<30:
    i+=1
    if i % 2 == 0: #juft sonlarni topish.
        print(i)

#s
i = 0
while i<30:
    i+=1
    if i % 2 != 0: # toq sonlarni topish
        print(i)

#t        
sonlar = []
i = 1

while i <= 30:
    if i % 3 == 0:
        sonlar.append(i * 2)
    i += 1

print(sonlar)    


#u
cars = ['lacetti', 'nexia', 'tayota', 'nexia', 'audi','malibu','nexia']
while 'nexia' in cars:
    cars.remove('nexia')
print(cars)