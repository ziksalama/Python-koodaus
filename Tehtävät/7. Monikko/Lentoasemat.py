lentoasemat = {}

while True:
    print("\n--- Lentoaseman haku ja tallennus ---")
    print("1 - Syötä uusi lentoasema")
    print("2 - Hae lentoaseman tiedot")
    print("3 - Lopeta")
    valinta = input("Valintasi (1, 2 tai 3): ")
#tämä ei toimi, selvitellään - Okei nyt pitäs toimia
    if valinta == "1":
        icao = input("Anna lentoaseman ICAO-koodi: ").upper().strip()
        nimi = input("Anna lentoaseman nimi: ").strip()
        lentoasemat[icao] = nimi
        print(f"Tiedot tallennettu.")

    elif valinta == "2":
        haku_icao = input("Anna haettavan lentoaseman ICAO-koodi: ").upper().strip()
        if haku_icao in lentoasemat:
            print(f"Lentoaseman nimi: {lentoasemat[haku_icao]}")
        else:
            print(f"Virhe: Koodia {haku_icao} ei löydy rekisteristä.")

    elif valinta == "3":
        print("Ohjelma päättyy. Hei hei!")
        break

    else:
        print("Virheellinen valinta, yritä uudelleen.")