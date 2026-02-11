# Kysytään  tiedot
kanta = float(input("Syötä suorakulmion kannan pituus: "))
korkeus = float(input("Syötä suorakulmion korkeus: "))

# Lasketaan pinta-ala ja piiri
pinta_ala = kanta * korkeus
piiri = 2 * (kanta + korkeus)

# Tulostus
print("Suorakulmion pinta-ala on: " + str(pinta_ala))
print("Suorakulmion piiri on: " + str(piiri))