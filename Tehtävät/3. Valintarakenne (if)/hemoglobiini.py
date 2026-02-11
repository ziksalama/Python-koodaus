# Kysytään käyttäjältä tarvittavat tiedot
sukupuoli = input("Anna syntymähetkelläs sinulle määritelty sukupuoli (M/N): ").upper()
hb = float(input("Anna hemoglobiiniarvo (g/l): "))

# Tarkistus naisille
if sukupuoli == "N":
    if hb < 117:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 117 <= hb <= 175:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")

# Tarkistus miehille
elif sukupuoli == "M":
    if hb < 134:
        print("Hemoglobiiniarvosi on alhainen.")
    elif 134 <= hb <= 195:
        print("Hemoglobiiniarvosi on normaali.")
    else:
        print("Hemoglobiiniarvosi on korkea.")

# Virheellinen sukupuolisyöte
else:
    print("Virheellinen sukupuoli. Käytä merkintää M tai N.")