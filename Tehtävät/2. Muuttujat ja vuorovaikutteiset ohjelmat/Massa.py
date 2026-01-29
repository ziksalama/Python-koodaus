# Kysytään käyttäjältä syötteet
leiviskat = float(input("Anna leiviskät.\n"))
naulat = float(input("Anna naulat.\n"))
luodit = float(input("Anna luodit.\n"))
#Muunnetaan yksikköjä
luodit_yhteensa = (leiviskat * 20 * 32) + (naulat * 32) + luodit
grammat_yhteensa = luodit_yhteensa * 13.3
kilogrammat = int(grammat_yhteensa // 1000)
grammat = grammat_yhteensa % 1000
print("\nMassa nykymittojen mukaan:")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")