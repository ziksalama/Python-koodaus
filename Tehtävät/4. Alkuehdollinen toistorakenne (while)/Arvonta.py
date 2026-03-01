import random

luku = random.randint(1, 10)

arvaus = int(input("Luvun arvaus peli, luku on arvottu 1-10 välillä arvaa luku:"))

while(arvaus != luku):
    if(luku < arvaus):
        arvaus = int(input("Luku on pienempi kuin arvaus! \nArvaa uudestaan: "))

    elif(luku > arvaus):
        arvaus = int(input("Luku on suurempi kuin arvaus! \nArvaa uudestaan: "))
    elif (luku == arvaus):
        break
str_luku = str(luku)
print("Oikein! Luku on: "+ str_luku)