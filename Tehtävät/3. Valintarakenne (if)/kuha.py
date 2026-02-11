kuha_str = input("Kuhan pituus(cm)?: ")
kuha = float(kuha_str)

if kuha > 37:
    print("Aikamoinen saalis!")
if kuha < 37:
    vaje = (37 - kuha)
    print("Heitä kala järveen! Se on ",vaje,"cm, liian pieni")
