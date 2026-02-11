#Kysytään säde
import math3
sade_str = input("Syötä ympyrän säde:")
sade = float(sade_str)

#laskutoimitus
pintaala =  (math.pi * (sade ** 2))
#tulostus
print("Ympyrän pinta-ala on: " + str(pintaala))
