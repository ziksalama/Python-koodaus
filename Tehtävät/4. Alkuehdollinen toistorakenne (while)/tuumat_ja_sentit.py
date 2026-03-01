numero = float(input("Muutetaan tuumat senteiksi \nSyötä tuumat:"))
while numero >= 1:
        print(numero * 2.54, "cm")
        numero = float(input("Syötä tuumat:"))
        if numero < 1:
            break
        print("Numero oli negatiivinen")
        exit
