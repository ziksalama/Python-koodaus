alin = None
ylin = None

while True:
    syote = input("Syötä luku:")
    if syote == "":
        break

    numero = float(syote)

    if alin is None or numero < alin:
        alin = numero
    if ylin is None or numero > ylin:
        ylin = numero

if ylin is not None:
    print("Pienin luku:", alin)
    print("Suurin luku:", ylin)
else:
    print("Ei lukua")