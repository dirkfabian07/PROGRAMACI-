###
# Exercicis - variables
# Completa els exercicis següents creant i utilitzant variables.
###

# Exercici 1
# Crea variables per desar el nom d'un encaminador, la seva ubicació,
# el nombre de ports i si està encès. Mostra les dades en una frase
# utilitzant una f-string.
nom= "Alex"
ubicacio= "Lleida"
n_ports= 4
ences=  True
print(f"El router {nom} esta en la {ubicacio}, te {n_ports} ports y esta {ences}")


# Exercici 2
# Crea variables per desar els GB inclosos en un pla de dades mòbils
# i els GB consumits. Calcula quants GB queden i mostra el resultat.
# Després, actualitza el consum amb un valor nou i torna a calcular
# quants GB queden.
GB= 20
GB_consumit= 3
print(GB - GB_consumit)
GB_consumit= 4
print(GB - GB_consumit)
