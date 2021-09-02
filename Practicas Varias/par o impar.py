num=0

def principal():
    print("En qué número estás pensando?: ")

    global num
    num= int(input(": "))

    if num%2== 0:
        print(str(num) + " es número par")

    else:
        print(str(num) + " no es par")

principal()
while True:

    cont=input("Deseas continuar?: ")

    if cont=="si":
        principal()

    else:
        break; 

        


    