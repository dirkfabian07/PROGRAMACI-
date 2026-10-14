###
# Exercicis - input()
# Practica l'entrada de dades i la conversió de tipus amb exemples de telecomunicacions.
###

# Exercici 1
# Demana el nom d'un tècnic i el nom de la xarxa que està instal·lant.
nom_tecnic= str(input("Nom del técnic és:"))
nom_xarxa= str(input("Nom de la xarxa:"))
print(f"El nom del técnic és {nom_tecnic} y el nom de la xarxa és {nom_xarxa}")
# Exercici 2
# Demana la longitud d'un enllaç de fibra en quilòmetres i la velocitat de transmissió
# en Gbps. Mostra quants segons caldrien per transmetre 1 GB de dades.
# Suposa que 1 GB = 8 Gb i que la velocitat es manté constant.
longitud= int(input("La longitud d'un enllaç de fibra en quilometres és:"))
velocitat= float(input("La velocitat de transmisió:"))
temps= 8/velocitat
print(f"El temps de transmissió es de {temps} segons")
# Exercici 3
# Demana el nombre d'hores de feina i el preu per hora d'una instal·lació de xarxa.
# Demana també el preu del material.
# Mostra el cost total de la instal·lació.
hores= int(input("Les hores de feina són:"))
preu_hora= int(input("El preu per hora és:"))
preu_material= int(input("El preu pel material és:"))
preu_total= (hores * preu_hora) + preu_material
print(f"El preu total de la isntalació és: {preu_total} euros")
