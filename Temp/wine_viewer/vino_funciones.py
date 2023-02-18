#!/usr/bin/python3
from scrapers import covylsa_main
from scrapers import lukas_main

def listar(productos):
	""" Function to show the products from DB """
	print("Estos son los productos: \n")
	for pro in productos:
		print(f"-Id: {pro[0]} -Nombre: {pro[1]}, -Precio: {pro[2]}€, -Opciones de stock: {pro[3]}, -Información adicional: {pro[4]}")
	print("############################## \n")

def datosProductos():
	""" Function to get the scrapped products price """
	datos_productos_1 = covylsa_main.main()
	datos_productos_2 = lukas_main.main()
	datos_productos_2.extend(datos_productos_1)
	return datos_productos_2

def datosProductosActualizar(productos):
	""" Function to actualize the products """
	#listar(productos)
	actualizar = input("¿Procedo a actualizar la base?(S/N): ")
	if actualizar.upper() == 'S':
		print("Actualización en curso ahora")
		datos_productos_1 = covylsa_main.main()
		datos_productos_2 = lukas_main.main()
		datos_productos_2.extend(datos_productos_1)
		print("Actualización en curso")
		return datos_productos_2
	else:
		print("Actualización cancelada.")
		datos_productos_2 = None
		return datos_productos_2

def registroEliminar(productos):
	""" Function to delete the required product """
	listar(productos)
	existe = False
	nombre_eliminar = int(input("Escribe el id de producto a eliminar:"))
	for pro in productos:
		print(f"{pro[0]}")
		if pro[0] == nombre_eliminar:
			print("Dato encontrado para eliminar. \n")
			existe = True
			break
	if not existe:
		nombre_eliminar = ''
	return nombre_eliminar

if __name__=='__main__':
	datosProductosActualizar()
