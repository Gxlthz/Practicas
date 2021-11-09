import random as rn
import time 

#constantes 
exit= 6
piedra= 1
papel= 2
tijera= 3
zero= 0

#menú de las opciones
def startMenu():
    print("")
    print("BIENVENIDO AL JUEGO")
    print("")
    print("PIEDRA = 1")
    print("PAPEL = 2")
    print("TIJERA = 3")
    print("")
    print("Presiona 6 para salir")
    print("")



#valida la opcion que elige el usuario
def options():
    try:
        option= input("¿Qué eliges?: ")
        value= int(option)
        return value
    except ValueError: 
        print("coloca un número, por favor. \n")
        options()


#Evalua qué eligió la maquina
def MachineOption(machine):
    if machine == piedra:
        valor= "La maquina escogió piedra"

    elif machine == papel:
        valor= "La maquina escogió papel"

    elif machine == tijera:
        valor= "La maquina escogió tijera"
    
    return valor


#Evalua qué eligió el humano
def HumanOption(human):
    if human == piedra:
        valor= " y tú escogiste piedra"

    elif human == papel:
        valor= " y tú escogiste papel"

    elif human == tijera:
        valor= " y tú escogiste tijera"
    
    return valor

#empieza el juego, la maquina genera un número aleatorio que será considerado como su opción
def GamePlay(x):
    machine= rn.randint(1,3)

    if x== piedra and machine== tijera:
        print("")
        print("-------------------------------")
        print(MachineOption(machine)+HumanOption(x))
        print("")
        print("¡Ganaste! \n")
        print("-------------------------------")
       

    elif x == papel and machine == piedra:
        print("")
        print("-------------------------------")
        print(MachineOption(machine)+HumanOption(x))
        print("")
        print("¡Ganaste! \n")
        print("-------------------------------")


    elif x == tijera and machine == papel:
        print("")
        print("-------------------------------")
        print(MachineOption(machine)+HumanOption(x))
        print("")
        print("¡Ganaste! \n")
        print("-------------------------------")
        

    elif machine == piedra and x == tijera:
        print("")
        print("-------------------------------")
        print(MachineOption(machine)+HumanOption(x))
        print("")
        print("¡Perdiste! \n")
        print("-------------------------------")
        
        
    elif machine == papel and x == piedra:
        print("")
        print("-------------------------------")
        print(MachineOption(machine)+HumanOption(x))
        print("")
        print("¡Perdiste! \n")
        print("-------------------------------")

        
    elif machine == tijera and x == papel:
        print("")
        print("-------------------------------")
        print(MachineOption(machine)+HumanOption(x))
        print("")
        print("¡Perdiste! \n")
        print("-------------------------------")
        

    elif x == machine:
        print("")
        print("-------------------------------")
        print(MachineOption(machine)+HumanOption(x))
        print("")
        print("¡Empate! \n")
        print("-------------------------------")


#declaracion de la funcion principal, "zero" está valorado en 0
def main():
    leave= zero
    cont= zero
    while leave != exit:
        if cont > zero:
            time.sleep(2)
            
        startMenu()
        leave= options()
        GamePlay(leave)
        cont=1
    print("Adios.")
   

if __name__ == "__main__":
    main()

 
