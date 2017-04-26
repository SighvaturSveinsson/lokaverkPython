from random import *

hrutar = []
with open ("hrutar.txt") as skra:
    for lina in skra:
        lina.strip()
        hrutar.append(lina[:-1])
print("Hrútar", hrutar)

#dict = {"Hrútur 1":[1,2,3],"Hrútur 2":[4,5,6], "Hrútur 3":[7,8,9],"Hrútur 4":[1,2,3],"Hrútur 5":[4,5,6],"Hrútur 6":[7,8,9]}
#print(dict)

for key,value in eval(hrutar[0]).items():
    print(key)
    print(int(value[0]),"  ",value[1]," ",value[2])
flokkar = ["Þyngd", "Mjólkurlagni dætra", "Einkun ullar", ""]

'''
for i in dict:
    print(i)
    eiginleikar = []
    teljari = 0
    for x in dict[i]:
        eiginleikar.append(x)
        print(flokkar[teljari], eiginleikar[teljari])
        teljari += 1
    print("------------")
'''

print("********************")


leikmadur1 = []
talvan = []
spil = []
nofn = []
komnarTolur = []
while len(leikmadur1) != 3:
    tala = randrange(0,5)
    if tala not in komnarTolur:
        komnarTolur.append(tala)
        leikmadur1.append(hrutar[tala])
    else:
        teljari = 0
for i in range(3):
    for key,value in eval(leikmadur1[i]).items():
        print(key)
        for x in range(3):
            print(flokkar[x],value[x])
        print("-------------------")

print("+++++++++")
for key, value in eval(leikmadur1[0]).items():
    print(key)
    for x in range(3):
        print(x+1, flokkar[x], value[x])
    print("Hvaða flokk viltu velja? ")