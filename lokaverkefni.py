from random import *

def leikmadurGerir():
    for key, value in eval(leikmadur1[0]).items():
        print(key)
        for x in range(3):
            print(x + 1, flokkar[x], value[x])
        val = int(input("Hvaða spil eiginleika viltu velja (1-10)"))
        print(value[val - 1])
        spil.append(key)
        spil.append(value[val - 1])
        print(spil)
        print("-------------------")

def talvanGerir():
    print("+++++++++")
    for key, value in eval(leikmadur1[0]).items():
        print(key)
        for x in range(3):
            print(x + 1, flokkar[x], value[x])
        val2 = int(input("Hvaða spil eiginleika viltu velja (1-10)"))
        print(value[val2 - 1])
        spil.append(key)
        spil.append(value[val2 - 1])
        print(spil)
        print("-------------------")

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




flag = True
if spil[1] > spil[3]:
    print("Hrúturinn", spil[0], "á móti", spil[2])
    print("Leikmaður vann")
    flag = True
elif spil[1] < spil[3]:
    print("Hrúturinn", spil[0], "á móti", spil[2])
    print("Talvan vann")
    flag = True
else:
    print("jafntefli")
    flag = False

if flag != False:
    for i in range(len(spil)):
        spil.remove(spil[0])
    print(spil)