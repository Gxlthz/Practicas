cont= ""
lf = False
def contraseñas():
    cont= input ("Introduce tu contraseña: ")
    lf= cont.isalnum()

print ("Bienvenido a KeyGestor")

contraseñas()

if len(cont)> 6 and lf == True:
    print ("buen trabajo")

else:
    print ("tu contraseña no es valida")
