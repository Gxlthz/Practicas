import random
cont= 0
print("Adivina el número oculto \n")

numero= random.randint(1, 50)
num= int(input("Piensa un número del 1 al 50. "))
cont +=1


while True:

    if numero == num:
        print("Ganaste!! el numero correcto era "+ str(numero) + " y has realizado " + str(cont) + " intentos.")
        break;
    
    elif numero > num:
        print ("El número es más grande... \n")
        
        again= input("Quieres seguir jugando?: ")
    
    elif num > numero:
        print(" EL número es más pequeño... \n")
        again= input("Quieres seguir jugando?: ")

        
    if again.lower()== "si":
        cont+= 1
        num= int(input("Piensa un número del 1 al 50: "))
    else:
        print("Adios")
        break;





        

