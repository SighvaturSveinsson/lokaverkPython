from random import *

#Leikmaður velur hvaða flokk hann vill keppa í
def leikmadurGerir():
    for key, value in eval(leikmadur1[0]).items():
        #Prentar út nafnið og flokka hrútsins
        print(key)
        for x in range(8):
            print(x + 1, flokkar[x], value[x])
        #Leikmaður velur hvaða flokk hann vill keppa í
        val = int(input("Hvaða spil eiginleika viltu velja (1-8)"))
        spil.append(key)
        spil.append(value[val - 1])
        print(spil)

        #
        for key, value in eval(talvan[0]).items():
            spil.append(key)
            spil.append(value[val - 1])
            print(spil)
            print("-------------------")
            leikmadur1.remove(leikmadur1[0])
            talvan.remove(talvan[0])

#Fall fyrir
def talvanGerir():
    for key, value in eval(talvan[0]).items():
        print(key)
        for x in range(8):
            print(x + 1, flokkar[x], value[x])
        val = randrange(0,8)
        spil.append(key)
        spil.append(value[val - 1])
        print(spil)

        for key, value in eval(leikmadur1[0]).items():
            spil.append(key)
            spil.append(value[val - 1])
            print(spil)
            print("-------------------")
            leikmadur1.remove(leikmadur1[0])
            talvan.remove(talvan[0])

hrutar = []
with open ("hrutar.txt") as skra:
    for lina in skra:
        lina.strip()
        hrutar.append(lina[:-1])
print("Hrútar", hrutar)

flokkar = ["Þyngd", "Mjólkurlagni dætra", "Einkun ullar", "Fjöldi afkvæma", "Einkunn læris", "Frjósemi", "Gerð/Þykkt bakvöðva", "Einkunn fyrir malir"]

print("********************")


leikmadur1 = []
talvan = []
spil = []
komnarTolur = []

while len(leikmadur1) != 26:
    tala = randrange(0,52)
    if tala not in komnarTolur:
        komnarTolur.append(tala)
        leikmadur1.append(hrutar[tala])

while len(talvan) != 26:
    tala = randrange(0,52)
    if tala not in komnarTolur:
        komnarTolur.append(tala)
        talvan.append(hrutar[tala])

teljari = 0
tala = 0
tala2 = 0
while len(leikmadur1) != 0 and len(talvan) != 0:



    if teljari == 0:
        leikmadurGerir()
        teljari += 1
    else:
        talvanGerir()
        teljari = 0


    flag = True

    if spil[1+tala2] > spil[3+tala2]:
        print("Hrúturinn", spil[0+tala2], "á móti", spil[2+tala2])
        print("Hrúturinn",spil[0+tala2] ,"vann")
        print("Leikmaður vann")
        flag = True
        tala = 0
    elif spil[1+tala2] < spil[3+tala2]:
        print("Hrúturinn", spil[0+tala2], "á móti", spil[2+tala2])
        print("Hrúturinn", spil[2+tala2] ,"vann")
        print("Talvan vann")
        tala = 0
        tala2 = 0
        flag = True
    else:
        print("Jafntefli")
        tala += 2
        tala2 += 4
        flag = False

    if flag != False:
        for i in range(len(spil)):
            spil.remove(spil[0])
        print(spil)