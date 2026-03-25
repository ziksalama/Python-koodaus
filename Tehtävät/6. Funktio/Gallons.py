def muunna_litroiksi(gallonat):
    return gallonat * 3.785


print("Gallona-litra -muunnin. Lopeta syöttämällä negatiivinen luku.")

while True:
    syote = float(input("Anna gallonamäärä: "))

    if syote < 0:
        print("Ohjelma lopetetaan.")
        break

    litrat = muunna_litroiksi(syote)
    print(f"{syote} gallonaa on {litrat:.2f} litraa.")