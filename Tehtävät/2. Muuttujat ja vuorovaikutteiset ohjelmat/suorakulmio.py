# Kysytään käyttäjältä tiedot
kanta_str = input("Syötä suorakulmion kannan pituus: ")
korkeus_str = input("Syötä suorakulmion korkeus: ")

# Muunnetaan merkkijonot liukuluvuiksi (float)
kanta = float(kanta_str)
korkeus = float(korkeus_str)

# Lasketaan pinta-ala ja piiri
pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

# Tulostus
print("Suorakulmion pinta-ala on: " + str(pinta_ala))
print("Suorakulmion piiri on: " + str(piiri))