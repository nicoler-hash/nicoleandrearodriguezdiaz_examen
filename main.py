from inventario import *
while True:
    try:
        print("----------EMPRESA ACME-----------")
        print("------GESTION DE INVENTARIO------")
        print("1. Registrar producto")
        print("2. Ingresar producto")
        print("3. Sacar producto")
        print("4. Buscar producto")
        print("5. Eliminar producto")
        print("6. Historial")
        print("7. Reporte")
        print("8. Transferencia de productos ")
        print("9. Salir")

        op = input("Seleccione una opcion: ").strip()
    
        if op == "1":
            registrar_producto()

        elif op == "2":
            ingresar_producto()

        elif op == "3":
            sacar_producto()

        elif op == "4":
            buscar_producto()
        elif op == "5":
            eliminar_producto()


        elif op == "6":
            historial()

        elif op == "7":

            reporte()
        elif op == "8":
            transferencia()
        elif op == "9":
            print("saliendo")
            break

        else:
            print("opcion no valida")

    except Exception as e:
        print("ocurrio un error:", e)