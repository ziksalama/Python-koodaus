# Kysytään käyttäjältä kolme kokonaislukua
luku1_str = input("Syötä ensimmäinen kokonaisluku: ")
luku2_str = input("Syötä toinen kokonaisluku: ")
luku3_str = input("Syötä kolmas kokonaisluku: ")
luku1 = int(luku1_str)
luku2 = int(luku2_str)
luku3 = int(luku3_str)

# Lasku
summa = luku1 + luku2 + luku3
tulo = luku1 * luku2 * luku3
keskiarvo = summa / 3

# Tulos
print("Lukujen summa on: " + str(summa))
print("Lukujen tulo on: " + str(tulo))
print("Lukujen keskiarvo on: " + str(keskiarvo))