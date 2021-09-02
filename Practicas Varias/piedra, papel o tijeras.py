import random
conta_humano= 0
conta_maq= 0 
humano= 0 
maq = 0




print("¡Esto es piedra, papel o tijera!!")
print("----------------------------------")
print("Gana el mejor de 3...")
print("-------------------------------")
#-----------------------------------------------------juego--------------------------------------------------
def juego():
    global humano
    humano= int(input("qué eliges?: "))

    global maq
    maq= random.randint(1, 3)


#----------------------------------condicionales------------------------------------------
def condicinal():
    global humano
    global maq
    global conta_humano
    global conta_maq
    if humano== 1 and maq== 3:
        print("Ganaste!! piedra mata tijeras")
        print("-------------------------------")
        conta_humano+=1
        

    elif humano == 2 and maq == 1:
        print ("ganaste!!! papel mata piedra")
        print("-------------------------------")
        conta_humano+=1

    elif humano == 3 and maq == 2:
        print("ganaste!!!! tijera mata papel")
        print("-------------------------------")
        conta_humano+=1

#---------------------------------el turno de la maquina---------------------------------------------
    elif maq == 1 and humano == 3:
        print("Oppps!!! perdiste, piedra mata tijeras")
        print("-------------------------------")
        conta_maq+=1

    elif maq == 2 and humano == 1:
        print("opsss! perdiste, papel mata piedra")
        print("-------------------------------")
        conta_maq+=1

        
    elif maq == 3 and humano == 2:
        print("Oppps perdiste, tijera mata papel")
        print("-------------------------------")
        conta_maq+=1

    elif humano == maq:
        print("Empate!!!")
        print("-------------------------------")

while True:
    

    juego()
    condicinal()

    if conta_humano == 3:
        print("Felicidades!!! has ganando el juego")
        break;
    elif conta_maq== 3:
        print("has perdido el juego!!!")
        break;


