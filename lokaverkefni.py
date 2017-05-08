#8.5.2017
#Sighvatur sveinsson
#Mikolaj oskar

from random import *

#Fall fyrir leikmann
def leikmadurGerir():
    for key, value in eval(leikmadur1[0]).items():
        #Prentar út nafnið og flokka hrútsins
        print(key)
        for x in range(8):
            print(x + 1, flokkar[x], value[x])
        #Leikmaður velur hvaða flokk hann vill keppa í
        val = int(input("Hvaða flokk viltu velja (1-8)"))
        #Setur spilð sem notandi valdi í lista
        spil.append(key)
        spil.append(value[val - 1])

        #Finnur spilið hjá tölvunni
        for key, value in eval(talvan[0]).items():
            # Setur spilð sem talvan fékk í listann
            spil.append(key)
            spil.append(value[val - 1])

            #Fjarlægir svo spilin úr stokknum þeirra
            leikmadur1.remove(leikmadur1[0])
            talvan.remove(talvan[0])

#Fall fyrir tölvuna
def talvanGerir():
    for key, value in eval(talvan[0]).items():
        # Prentar út nafnið og flokka hrútsins
        print(key)
        for x in range(8):
            print(x + 1, flokkar[x], value[x])
        #Talvan velur (random) hvaða flokk er keppt í
        val = randrange(0,8)
        # Setur spilð sem talvan valdi í lista
        spil.append(key)
        spil.append(value[val - 1])

        # Finnur spilið hjá leikmanni
        for key, value in eval(leikmadur1[0]).items():
            # Setur spilð sem leikmaður fékk í listann
            spil.append(key)
            spil.append(value[val - 1])

            # Fjarlægir svo spilin úr stokknum þeirra
            leikmadur1.remove(leikmadur1[0])
            talvan.remove(talvan[0])

#Opnar skránna með öllum hrútunum og setur þá í lista
hrutar = []
with open ("hrutar.txt") as skra:
    for lina in skra:
        lina.strip()
        hrutar.append(lina[:-1])

#Allir flokkanir í lista
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
print(leikmadur1)
print(talvan)
#Keyrir þangað til talvan eða leikmaður klára spilin
while len(leikmadur1) != 0 and len(talvan) != 0:

    #Leikmaður og talvan skiptast á að gera
    if teljari == 0:
        leikmadurGerir()
        input("(Enter)")
        teljari += 1
    else:
        talvanGerir()
        input("(Enter)")
        teljari = 0

    #Flag verður false ef það er jafntefli
    flag = True

    #Fer yfir hver vinnur
    print("Hrúturinn", spil[0 + tala], "með", spil[1 + tala], "á móti", spil[2 + tala], "með", spil[3 + tala])
    if spil[1+tala] > spil[3+tala]:
        print("Hrúturinn",spil[0+tala] ,"vann")
        print("Leikmaður vann")
        flag = True
        tala = 0
        tala2 = 1
    elif spil[1+tala] < spil[3+tala]:
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

    #Setur svo spilin aftast í bunkann hjá þeim sem vinnur
    if flag != False:
        if tala2 == 1:
            leikmadur1.append(leikmadur1[0])
            leikmadur1.append(talvan[0])
        elif tala2 == 2:
            talvan.append(talvan[0])
            talvan.append(leikmadur1[0])

        #Og fjarlægir spilin úr listanum
        for i in range(len(spil)):
            spil.remove(spil[0])
        print(leikmadur1)
        print(talvan)