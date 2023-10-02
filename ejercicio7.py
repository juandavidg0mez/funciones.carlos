import math
def menu():
    while True:
        try:
            print("Cálculo de la combinatoria")
            print("Convertir texto a número")
            print("Cálcular el IVA de una factura")
            print("Salir")
            opcion = int(input(">> Escoja una opción"))
            if opcion < 0 or opcion > 4:
                print("Opcion invalida")
                input()
                break
            return opcion
        except ValueError:
            print("Error. Opcion incorrecta")
            input("")

def CalcularCombi():
    n = LeerEntero("Ingrese n")
    k = LeerEntero("Ingrese k")
    combinatoria = math.comb(n,k)
    print(f"El cálculo de la combinatoria es {combinatoria}")
    MsgNotify("...")


def TextNumber():
    pass

def CalculaIVA ():
    pass
def MsgNotify(msg):
    print("\n NOTIFY!", msg)
    input(" -> Presione cualquier letra para regresar al Menú")
    print("=" * 45, "\n")

def LeerEntero(msg):
    while True:
        try:
            n = int(input(msg))
            if n < 0:
                MsgNotify("Error! Dato no valido")
                continue
            return n
        except ValueError:
            print("Error! Ingrese un numero Entero")
while True:
    Opcion = menu()
    if Opcion == 1:
        CalcularCombi()
    elif Opcion == 2:
        TextNumber()
    elif Opcion == 3:
        CalculaIVA()
    elif Opcion == 4:
        break

