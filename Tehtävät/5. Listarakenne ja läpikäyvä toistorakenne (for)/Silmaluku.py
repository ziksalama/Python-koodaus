import random

maara = int(input("Anna arpakuutioiden lukumäärä: "))
summa = 0
#käytetään määrää rangena
for i in range(maara):
    heitto = random.randint(1, 6)
    summa = summa + heitto

print("Silmälukujen summa on:", summa)