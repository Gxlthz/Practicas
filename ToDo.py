import time 

#Constantes
add= 1
edit= 2
done= 3 
delete= 4
listTask= 5
exit= 6 

class Task:
    def __init__(self, name, duedate):
      self.name = name
      self.duedate= duedate
      self.done = False
    
    def printData(self, index):
        print("{0}. Tarea: {1}. Fecha límite: {2}. Hecha: {3}.".format(index, self.name, self.duedate, self.done))


def printMenu():
    print("")
    print("*******************")
    print("*     To Do       *")
    print("*******************")
    print("\n")

    print(" Selecciona una opción ")
    print("\n")

    print("1. Agregar tarea")
    print("2. Editar tarea")
    print("3. Marcar como hecha")
    print("4. Borrar tarea")
    print("5. Mostrar tareas")
    print("6. Salir")
    print("\n")


def getOption():
    try:
        value= input("Opcion: ")
        opcion= int(value)

    except ValueError:
        print("dame un valor correcto")
    
    return opcion


def validOption(option):
    if option < 1 or option > 6:
        return False

    return True


def newlist():
    return []


def addTask(task, toDo):
    toDo.append(task)


def processAdd(toDo):
    task = createtask()
    addTask(task, toDo)
    print("* Tarea creada *")
    time.sleep(2)


def createtask():
    print("")
    print("******************")
    print("* Agregar tareas *")
    print("******************")
    print("")

    nombre= input("Nombre de la tarea: ")
    fecha= input("Fecha limite de la tarea: ")
    task= Task(nombre, fecha)
    
    return task

def getindex():
    try:
        value= input("Digite el número de  la tarea a editar: ")
        index= int(value)
    except ValueError:
        print("Digite un número válido")
    
    return index

"""def alternativeGetidex(index, toDo):
    try:
        if index in toDo:
            
            
    except ValueError:
        print("no numero no encontrado")

    return index"""
        
    


def getNewTask(index, newtask, toDo):
    toDo[index-1] = newtask

    return 

def proccessEditTask(toDo):
    print("*****************")
    print("* Editar tareas *")
    print("*****************")

    index= getindex()
    task= createtask()
    taskEdited= getNewTask(index, task, toDo)
    print("")
    print("Tarea editada con éxito")

    return taskEdited


def showtask():
    print("")
    print("******************")
    print("* Mostrar tareas *")
    print("******************")
    print("")


def printList(toDo):
    index= 0
    for task in toDo:
        index +=1
        task.printData(index)
    time.sleep(2)

def setisdone():
    value= input("Digita 1 si está hecha, de lo contrario cualquier otra tecla: ")
    if value == "1":
        return True

    return False


def GetTaskDone(index, done, toDo):
    toDo[index-1].done = done


def processDoneTask(toDo):

    index= getindex()
    done= setisdone()
    GetTaskDone(index, done, toDo)
    print("proceso realizado con éxito")

def deletetask(index, toDo):
    del toDo[index-1]

def proccessDeleteTask(toDo):
    index = getindex()
    deletetask(index, toDo)
    print("Tarea eliminada")

def whatdo(opcion, toDo):
    if opcion == add:
        processAdd(toDo)
        return

    if opcion == edit:
        printList(toDo)
        proccessEditTask(toDo)
        return

    if opcion == done:
        printList(toDo)
        processDoneTask(toDo)
        return

    if opcion == delete:
        proccessDeleteTask(toDo)
        return

    if opcion == listTask:
        showtask()
        printList(toDo)
        return


def execute():
    option= 0
    toDo = newlist()

    while option != exit:
        printMenu()
        option= getOption()

        if not validOption(option):
            print("")
            print("El valor que has digitado no es correcto. Por favor ingresa un valor entre 1 y 6.")
            continue

        whatdo(option, toDo)


execute()

