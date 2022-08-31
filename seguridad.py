pasos=[]
indice = int (input("Ingrese el numero de pasos que llevara su protocolo: "))
for i in range(indice):
    print("Registro de pasos:", i+1)
    prot = input("Ingrese la descipcion\n")
    proto =prot.lower()
    pasos.append(proto)
print("El protocolo ha sido registrado")
for i in range(len(pasos)):
    pasos.sort()
modificar=input("Escira si, si desea hacer alguna modificacion o no, si quiere salir\n")
while modificar=="si":
    def menu():
        print("1.-Agregar elemento")
        print("2.-Borrar elemento")
        print("3.-Imprimir el protocolo")
        print("4.-Conocer el protocolo final y salir")
    menu()
    opcion1=int(input("Elija una de las opciones anteriores \n"))
    if opcion1==1:
        num=int(input("Escriba el numero de la posicion donde desea agregar \n"))
        prot=input("Escriba el elemento que desea agregar \n")
        proto=prot.lower()
        pasos.insert(num, proto)
        print("Elemento:", prot)

    elif opcion1==2:
        prot=input("Escriba el elemento que desea eliminar \n")
        proto=prot.lower()
        dele=pasos.index(prot)
        print("Desea eliminar a:", pasos[dele])
        eli=input ("Escriba si para confirmar \n")
        if eli =="si":
            input()
            pasos.pop(dele)
            print("El registro ha si do eliminado exitosamente")

    elif opcion1==3:        
        for i in range(len(pasos)):
            print (i+1,".-" , pasos[i].capitalize())
    
    elif opcion1==4:
        break
    cambio=input("Desea realizar otra operacion si/no \n")
print("El protocolo ha sido guardado")    