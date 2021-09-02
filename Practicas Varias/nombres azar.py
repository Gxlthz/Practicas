import random

Nombres_de_niño = ["Aarón", "Abdul",  "Abel",  "Abelardo",  "Abraham", "Adam","Manuel", "Moises", "Edgard"]

apellidos= ["Hidalgo", "Hurrieta", "Smith", "Lopez", "Polo", "Leon"]


i = random.randint(0, 5)
nombre= Nombres_de_niño[i]
nombre += " "

x = random.randint(0, 5)
ape= apellidos[x]

ls= nombre + ape

print (ls)


