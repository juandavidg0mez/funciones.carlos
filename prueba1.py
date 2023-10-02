import math

def text(menj):
    candenaN = ""
    for i in menj:
        if  i.isdigit() == True:
            candenaN = candenaN + i         
    return candenaN


def cal(factura, iva): 
    calculo = factura * iva  
    return  calculo + factura

def com (n, k):
    if n > k:
        combinatoria = math.factorial(n) / (math.factorial((n-k)) * math.factorial(k))
    else:
        print("recuerde que N debe ser mayor que K ")
    return combinatoria

def menu():
    while True:
        try:
            print("*** menu calculadora********")
            print ( " 1.Calculo de la combinacion ")
            print ( " 2. convertir texto a numero  ")
            print ( " 3. calcular el IVA de una factura ")
            print ( " 4. salir")
            op = int(input("opcion del 1 al 4: "))
            if op < 1 or op >4:
                print("opcion no validad escoja del 1  al 4: ")
                input("presione cualquier tecla para continuar")
                print("=" * 30)
                continue
            return op
        except ValueError:
            print("opcion no validad. escoja de 1 al 4: ")
            input("presione cualquier tecla para continuar")

        return op
while True:
    opcion = menu()
    if opcion == 1:
        n1 = int(input("ingrese un numero : "))
        n2 = int(input("ingrese otro numero : "))
        combi = com(n1, n2)
        print(f"esta cantidad de combinaciones posibre entre {n1} y {n2} es: {combi:.0f} ")
    elif opcion == 2:
        dato = input("ingrese texto and numerico: ")
        ads = text(dato)
        print("el texto sin letras es: ", ads)
    elif opcion == 3:
        iva = float(input("ingrese iva: "))
        factura = int(input("ingrerse la factura: "))
        resultado = cal(factura, iva)
        print("el total de la factua es de : ", resultado)
        print(f"este es su iva neto: {iva}")
        print(f"esta es su factura sin el iva aplicado : {factura}")
    
    elif opcion == 4:
        print("\n\nGracias por itilizar EL MENU")
        print("adios")
        input()
    break
menu()