import json
from datetime import datetime

from config import INVENTORY_FILE
ARCHIVO = str(INVENTORY_FILE)



#------------------------------cargar---------------------------------------------------
#SE UTLIZA PARA CARGAR EL ARCHIVO DONDE SE GUARDA EL INVENTARIO
def cargar():
    try:
        with open(ARCHIVO, "r") as f:
            return json.load(f)
    except:
        return {}

#SE USA PARA GUARDAR EL INVENTARIO
def guardar(inventario):
    with open(ARCHIVO, "w") as f:
        json.dump(inventario, f, indent=4)


# ----------------------------registrar productos-------------------------------------
#SE UTLIZA PARA REGISTRAR EL NUEVO PRODUCTO Q VAYA A INGRESAR. INGRESA: CODIGO,NOMBRE Y PUES EL PROVEEDOR Y PUES DE AHI SE GUARDA
def registrar_producto():
    inventario = cargar()

    codigo = input("codigo: ")
    nombre = input("nombre: ")
    proveedor = input("proveedor: ")

    if codigo in inventario:
        print("ya existe el producto")

    inventario[codigo] = {
        "nombre": nombre,
        "proveedor": proveedor,
        "bodegas": {},
        "movimientos": []
    }

    guardar(inventario)
    print("producto guardado")


#--------------------------ingresar productos---------------------------------- 
#ES PARA AÑADIR LA CANTIDAD DE PRODUCTOS QUE VA A INGRESAR, PERO AQUI SE LE AÑADE UNA DESCRIPCION Y UNA FECHA PARA MAS ORGANIZACION
def ingresar_producto():
    try:
        inventario = cargar()
        codigo = input("Codigo: ")

        if codigo not in inventario:
            print("no existe el producto")

        cantidad = int(input("Cantidad: "))

        print("Seleccione la bodega:")
        print("1.----Norte----")
        print("2.----Centro----")
        print("3.----Oriente----")

        op_bodega = input("Opcion, elige un numero: ")

        if op_bodega == "1":
            bodega = "norte"
        elif op_bodega == "2":
            bodega = "centro"
        elif op_bodega == "3":
            bodega = "oriente"
        else:
            print("bodega no valida")

        descripcion = input("descripcion: ")
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        if bodega not in inventario[codigo]["bodegas"]:
            inventario[codigo]["bodegas"][bodega] = 0

        inventario[codigo]["bodegas"][bodega] = cantidad

        inventario[codigo]["movimientos"].append({
            "tipo": "entrada",
            "cantidad": cantidad,
            "bodega": bodega,
            "descripcion": descripcion,
            "fecha": fecha
        })
        guardar(inventario)

        print("producto ingresado correctamente")
        print("Fecha:", fecha)

    except ValueError:
        print("la cantidad debe ser un numero")


#-------------------------- sacar producto---------------------------------
#SIRVE PARA RETIRAR PRODUCTOS DEL INVENTARIO, PUES AHI TE PIDEN EL CODIGO, 
#LA CANTIDAD Q RETIRAS Y EN QUE BODEGAS DESEA RETIRARLA, PUES TAMBIEN UAN DESCRIPCION
#Y UNA FECHA DE RETIRO
def sacar_producto():
    try:
        inventario = cargar()
        codigo = input("Codigo: ")

        if codigo not in inventario:
            print("no existe el producto:(")

        cantidad = int(input("Cantidad: "))

        print("Seleccione la bodega:")
        print("1.----Norte----")
        print("2.----Centro----")
        print("3.----Oriente----")

        op_bodega = input("Opcion, elige un numero: ")

        if op_bodega == "1":
            bodega = "norte"
        elif op_bodega == "2":
            bodega = "centro"
        elif op_bodega == "3":
            bodega = "oriente"
        else:
            print("bodega no valida")

        descripcion = input("Descripcion: ")
        fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

        if bodega not in inventario[codigo]["bodegas"]:
            inventario[codigo]["bodegas"][bodega] = 0

        if cantidad > inventario[codigo]["bodegas"][bodega]:
            print("no hay suficiente stock")

        inventario[codigo]["bodegas"][bodega] -= cantidad

        inventario[codigo]["movimientos"].append({
            "tipo": "salida",
            "cantidad": cantidad,
            "bodega": bodega,
            "descripcion": descripcion,
            "fecha": fecha
        })
        guardar(inventario)

        print("salida realizada")

    except ValueError:
        print("debe ingresar un numero")
        guardar(inventario)


# -------------------------------------------buscar producto---------------------------------
#PERMITE CONSULTAR LA INFORMACION DEL PRODUCTO USANDO EL CODIGO Y PUES SALE LA 
#EL NOMBRE EL PROVEEDOR Y LA CANTIDAD DISPONIBLE EN CADA BODEGA ADEMÁS DEL STOCK TOTAL
def buscar_producto():
    inventario = cargar()

    codigo = input("Codigo: ")

    if codigo in inventario:
        producto = inventario[codigo]

        print("nombre:", producto["nombre"])
        print("proveedor:", producto["proveedor"])
        print("cantidad en norte:", producto["bodegas"].get("norte",0))
        print("cantidad en centro:", producto["bodegas"].get("centro",0))
        print("cantidad en oriente:", producto["bodegas"].get("oriente",0))
        stock_total = sum(producto["bodegas"].values())
        print("stock total:", stock_total)
    else: 
        print("no existe")


#-----------------------------------eliminar producto---------------------------------------
#ESTA OPCION PERMITE ELIMINAR PRODUCTOS SOLAMEMTE CON EL CODIGO
def eliminar_producto():

    inventario = cargar()

    codigo = input("codigo a eliminar: ")

    if codigo in inventario:

        del inventario[codigo]

        guardar(inventario)

        print("producto eliminado correctamente")

    else:
        print("ese producto no existe")


#-------------------historial---------------------
#MUESTRA TODOS LOS MOVIMIENTOS Q HA TENIDO EL DICHO PRODUCTO INGRESADO MOSTRANDO
#CANTIDAD,BODEGA,DESCRIPCION Y FECHA
def historial():

    inventario = cargar()

    codigo = input("Codigo: ")

    if codigo in inventario:

        print("----- HISTORIAL -----")

        for movimiento in inventario[codigo]["movimientos"]:
            print("tipo:", movimiento["tipo"])
            print("cantidad:", movimiento["cantidad"])
            print("bodega:", movimiento["bodega"])
            print("descripcion:", movimiento["descripcion"])
            print("fecha:", movimiento["fecha"])

    else:
        print("no existe el producto")


# ---------------------reporte------------------------
#ES UN RESUMEN DE   DE TODOS LOS PRODUCTOS REGISTRADO EN EL INVENTARIO JUNTO CON LA CANTIDAD DISPONIBLE
#EN CADA BODEGA  Y EL STOCK TOTAL
def reporte():
    inventario = cargar()

    for codigo, producto in inventario.items():
        print("codigo:", codigo)
        print("nombre:", producto["nombre"])
        print("proveedor:", producto["proveedor"])

        print("Norte:", producto["bodegas"].get("norte", 0))
        print("Centro:", producto["bodegas"].get("centro", 0))
        print("Oriente:", producto["bodegas"].get("oriente", 0))

        stock_total = sum(producto["bodegas"].values())
        print("Stock total:", stock_total)



def transferencia():
    inventario = cargar()

    codigo = input("Codigo del producto: ")
    if codigo not in inventario:
        print("Producto no existe")

    bodegas_validas = ["norte", "centro", "oriente"]

    origen = input("Bodega origen: ").lower()
    destino = input("Bodega destino: ").lower()

    if origen not in bodegas_validas or destino not in bodegas_validas:
        print("Bodega invalida")

    if origen == destino:
        print("No puedes transferir a la misma bodega")

    try:
        cantidad = int(input("Cantidad: "))
    except:
        print("Cantidad invalida ")

    descripcion = input("Descripcion: ")
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M")

    producto = inventario[codigo]


    for b in [origen, destino]:
        if b not in producto["bodegas"]:
            producto["bodegas"][b] = 0

    
    if producto["bodegas"][origen] < cantidad:
        print("Stock insuficiente")

    
    id_transferencia = str(datetime.now().timestamp())

    
    producto["bodegas"][origen] = cantidad
    producto["bodegas"][destino] = cantidad

    
    movimientos = [
        {
            "tipo": "salida",
            "cantidad": cantidad,
            "bodega": origen,
            "descripcion": descripcion,
            "fecha": fecha,
            "id_transferencia": id_transferencia
        },
        {
            "tipo": "entrada",
            "cantidad": cantidad,
            "bodega": destino,
            "descripcion": descripcion,
            "fecha": fecha,
            "id_transferencia": id_transferencia
        }
    ]

    producto["movimientos"].extend(movimientos)

    guardar(inventario)
    print("Transferencia hecha")

