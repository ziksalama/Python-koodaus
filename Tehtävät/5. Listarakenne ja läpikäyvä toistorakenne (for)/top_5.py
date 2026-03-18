#ensin tehdään tyhjä lista
luvut = []

while True:
    syote = input("Anna luku (tyhjä lopettaa): ")
    if syote == "":
        break
    luku = float(syote)
    luvut.append(luku)

luvut.sort(reverse=True)

print("Viisi suurinta lukua ovat:")
for luku in luvut[0:5]:
    print(luku)