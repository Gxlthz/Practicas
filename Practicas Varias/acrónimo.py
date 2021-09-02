print("Acronimos")
def acro(x):
    lis= x.split()

    acron= " "
# el lis es para almancenar el split y el acron luego será para almacenar las uniciales
    for i in lis:
        acron += i[0]

    op = acron.upper()

    return op


ape=input("Dame una org: ")

print(acro(ape))
