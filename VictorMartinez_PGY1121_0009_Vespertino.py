import random

vehs=[]

def grabve():
    tip=input("Tipo de vehículo: ")
    pat=input("Patente: ")
    marc=input("Marca: ")
    prec=float(input("Precio: "))
    mult=[]
    while True:
        opcion=input("¿Agregar multa? (Si/No): ")
        if opcion.lower() == 'no':
            break
        mont=float(input("Monto de la multa: "))
        fech=input("Fecha de la multa: ")
        mult.append((mont, fech))
    feregis=input("Fecha de registro del vehículo: ")
    due=input("Nombre del dueño: ")

    if not valpat(pat):
        print("La patente ingresada no es válida.")
        return

    if not valmarc(marc):
        print("La marca debe tener entre 2 y 15 caracteres.")
        return

    if prec<=5000000:
        print("El precio debe ser mayor a $5.000.000.")
        return

    veh={
        "Tipo": tip,
        "Patente": pat,
        "Marca": marc,
        "Precio": prec,
        "Multas": mult,
        "Fecha de registro": feregis,
        "Dueño": due
    }

    vehs.append(veh)
    print("Vehículo registrado exitosamente.")

def buscveh():
    pat=input("Ingrese la patente del vehículo: ")
    encontrado=False
    for veh in vehs:
        if veh["Patente"]==pat:
            print("Información del vehículo:")
            print("Tipo:", veh["Tipo"])
            print("Patente:", veh["Patente"])
            print("Marca:", veh["Marca"])
            print("Precio:", veh["Precio"])
            print("Multas:", veh["Multas"])
            print("Fecha de registro:", veh["Fecha de registro"])
            print("Dueño:", veh["Dueño"])
            encontrado = True
            break
    if not encontrado:
        print("Vehículo no encontrado.")

def imprcert():
    for veh in vehs:
        certemi=random.uniform(1500, 3500)
        certanotac=random.uniform(1500, 3500)
        certmult=random.uniform(1500, 3500)

        print("Certificado de Emisión de Contaminantes")
        print("Patente:", veh["Patente"])
        print("Dueño:", veh["Dueño"])
        print("Valor:", certemi)

        print("Certificado de Anotaciones Vigentes")
        print("Patente:", veh["Patente"])
        print("Dueño:", veh["Dueño"])
        print("Valor:", certanotac)

        print("Certificado de Multas")
        print("Patente:", veh["Patente"])
        print("Dueño:", veh["Dueño"])
        print("Valor:", certmult)

def valpat(pat):
    return True

def valmarc(marc):
    return 2 <= len(marc) <= 15

def menu():
    while True:
        print("\n--- Bienvenido a Automotora Auto Seguro ---")
        print("1.Grabar vehículo")
        print("2.Buscar vehículo")
        print("3.Imprimir certificados")
        print("4.Salir")
        opc=input("Ingrese una opción: ")

        if opc=='1':
            grabve()
        elif opc=='2':
            buscveh()
        elif opc=='3':
            imprcert()
        elif opc=='4':
            print("¡Hasta luego, gracias por visitar Auto Seguro!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

menu()