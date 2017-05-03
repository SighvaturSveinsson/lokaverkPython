#3.5.2017
#Sighvatur sveinsson
#Mikolaj oskar

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
        #Setur spilð sem notandi valdi í lista
        spil.append(key)
        spil.append(value[val - 1])
        print(spil)

        #
        for key, value in eval(talvan[0]).items():
            # Setur spilð sem talvan fékk í listann
            spil.append(key)
            spil.append(value[val - 1])
            print(spil)
            print("-------------------")

            #Fjarlægir svo spilin úr stokknum þeirra
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

#Opnar skránna með öllum hrútunum og setur þá í lista
hrutar = []
with open ("hrutar.txt") as skra:
    for lina in skra:
        lina.strip()
        hrutar.append(lina[:-1])
print("Hrútar", hrutar)

#Allir flokkanir
flokkar = ["Þyngd:", "Mjólkurlagni dætra:", "Einkun ullar:", "Fjöldi afkvæma:", "Einkunn læris:", "Frjósemi:", "Gerð/Þykkt bakvöðva:", "Einkunn fyrir malir:"]

#Býr til alla listana
leikmadur1 = []
talvan = []
spil = []
komnarTolur = []

#Setur 26 spil í bunkann hjá leikmanni 1
while len(leikmadur1) != 26:
    tala = randrange(0,52)
    if tala not in komnarTolur:
        komnarTolur.append(tala)
        leikmadur1.append(hrutar[tala])

# og 26 spil í bunkann hjá tölvunni
while len(talvan) != 26:
    tala = randrange(0,52)
    if tala not in komnarTolur:
        komnarTolur.append(tala)
        talvan.append(hrutar[tala])

teljari = 0
tala = 0
tala2 = 0

#Keyrir þangað til talvan eða leikmaður klára spilin
while len(leikmadur1) != 0 and len(talvan) != 0:

    #Leikmaður og talvan skiptast á að gera
    if teljari == 0:
        leikmadurGerir()
        teljari += 1
    else:
        talvanGerir()
        teljari = 0


    flag = True

    if spil[1+tala] > spil[3+tala]:
        print("Hrúturinn", spil[0+tala], "á móti", spil[2+tala])
        print("Hrúturinn",spil[0+tala] ,"vann")
        print("Leikmaður vann")
        flag = True
        tala = 0
        tala2 = 1
    elif spil[1+tala] < spil[3+tala]:
        print("Hrúturinn", spil[0+tala], "á móti", spil[2+tala])
        print("Hrúturinn", spil[2+tala] ,"vann")
        print("Talvan vann")
        tala = 0
        tala2 = 2
        flag = True
    else:
        print("Jafntefli")
        tala += 4
        tala2 = 0
        flag = False

    #Fjarlægir svo spilin
    if flag != False:
        for i in range(len(spil)):
            if tala == 1:
                leikmadur1.append(i)
            elif tala == 2:
                print()



            spil.remove(spil[0])
        print(spil)