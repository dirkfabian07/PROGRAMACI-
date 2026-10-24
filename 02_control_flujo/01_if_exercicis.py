###
# EXERCICIS
###

# Exercici 1: Qualitat del senyal Wi-Fi
# Demana el nivell de senyal rebut (RSSI) en dBm i classifica la cobertura:
# - -50 dBm o superior: excel·lent
# - Entre -67 dBm i menys de -50 dBm: bona
# - Entre -75 dBm i menys de -67 dBm: feble
# - Inferior a -75 dBm: molt feble
senyal= float(input("Nivell senyal rebut en dBm"))
if senyal >= -50:
 print ("Excel·lent")
elif -50 > senyal >= -67:
 print("Bona")
elif -67 > senyal >= -75:
 print("feble")
else:
 print("Molt feble")


# Exercici 2: Nivell de recepció d'una connexió de fibra òptica
# Demana la potència òptica rebuda en dBm. Per a aquest exercici, considera
# acceptable un nivell entre -27 dBm i -8 dBm, ambdós inclosos.
# Indica si el nivell és massa baix, acceptable o massa alt.
p_optica= float(input("lA POTENCIA OPTICA REBUDA ÉS:"))
if -8 >= p_optica >= -27:
 print("Acceptable")
elif -8 < p_optica:
 print("Massa alt")
else:
  print("Massa baix")
# Exercici 3: Consum mensual de dades mòbils
# Demana el consum de dades en GB d'una línia mòbil. El pla inclou 20 GB.
# Indica si el consum és dins del límit o si l'ha superat; en aquest últim cas,
# calcula quants GB addicionals s'han consumit.
consum= float(input("Consum de dades:"))
pla= 20 
if pla < consum:
  print("Límit superat")
  addicionals= consum-pla
  PRINT("Gb adicionales:", addicionals)
else:
  print("Dins del límit")
  
# Exercici 4: Diagnòstic d'una connexió de fibra
# Demana si l'indicador LOS del terminal òptic està encès i si l'indicador
# d'Internet del router està encès. Segons aquestes dues dades, indica si cal
# revisar el cable de fibra, comprovar el servei del proveïdor o si la connexió
# sembla funcionar correctament.
LOS= input("Esta encendido:")
Router= input("Esta encendido:") 
if LOS==si:
  print("Revisar cable fibra")
elif Router==no:
  print("Revisar internet")
else:
print ("connexió correcter")
 
# Exercici 5: Bateria d'un sistema d'alimentació ininterrompuda (SAI)
# Demana el percentatge de bateria disponible al SAI que alimenta un armari
# de comunicacions. Indica si el nivell és crític (menys del 20 %), baix
# (del 20 % al 49 %) o suficient (50 % o més). Rebutja valors fora del rang
# del 0 % al 100 %.
bateria= float(input("Percentatge de bateria:"))
if 0 <= bateria < 20:
 print("Nivell crític")
elif  20 <= bateria > 50:
 print("Nivell baix")
elif  100 >= bateria >= 50:
 print("Suficient")
else:
 print("rebutja als valors fora del rang")
