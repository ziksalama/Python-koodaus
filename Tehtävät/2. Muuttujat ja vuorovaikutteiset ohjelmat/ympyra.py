#Kysytään säde
sade_str = input("Syötä ympyrän säde:")
sade = float(sade_str)
#laskutoimitus
pintaala =  (3.14159 * (sade ** 2))
#tulostus
print("Ympyrän pinta-ala on: " + str(pintaala))
