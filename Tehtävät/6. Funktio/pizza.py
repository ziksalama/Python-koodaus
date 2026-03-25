import math

def laske_yksikkohinta(d_cm, hinta_eur):
    sade_m = (d_cm / 2) / 100
    pinta_ala_m2 = math.pi * (sade_m ** 2)
    yksikkohinta = hinta_eur / pinta_ala_m2
    return yksikkohinta

print("Tervetuloa pizzalaskuriin!")

d1 = float(input("Anna 1. pizzan halkaisija (cm): "))
hinta1 = float(input("Anna 1. pizzan hinta (€): "))

d2 = float(input("Anna 2. pizzan halkaisija (cm): "))
hinta2 = float(input("Anna 2. pizzan hinta (€): "))

yksikko1 = laske_yksikkohinta(d1, hinta1)
yksikko2 = laske_yksikkohinta(d2, hinta2)

print(f"\n1. pizzan yksikköhinta: {yksikko1:.2f} €/m^2")
print(f"2. pizzan yksikköhinta: {yksikko2:.2f} €/m^2")

if yksikko1 < yksikko2:
    print("Ensimmäinen pizza antaa paremman vastineen rahalle.")
elif yksikko2 < yksikko1:
    print("Toinen pizza antaa paremman vastineen rahalle.")
else:
    print("Molemmat pizzat antavat yhtä hyvän vastineen rahalle.")