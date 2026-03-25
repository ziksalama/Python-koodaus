def laske_summa(lukulista):
    summa = 0
    for luku in lukulista:
        summa += luku
    return summa

lista = [1, 2, 3, 4, 5]
tulos = laske_summa(lista)

print("Lista on:", lista)
print("Listan lukujen summa on:", tulos)