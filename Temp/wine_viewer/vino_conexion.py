#!/usr/bin/python3

from mysql.connector import *
from mysql.connector import Error

""" Class to connect to DB and make the CRUD options. """
class DataConexion():
	def __init__(self, host, port, user, password, db):
		self.host = host
		self.port = port
		self.user = user
		self.password = password
		self.db = db
		try:
			self.conexion = connect(
				host = self.host,
				port = self.port,
				user = self.user,
				password = self.password,
				db = self.db)
			print("Conexion realizada con éxito")
		except Error as ec:
			print(f"No se ha podido conectar, error {ec} ocurrido.")

	def listaProductos(self):
		""" Method to connect, get and show the data from DB """ 
		if self.conexion.is_connected():
			try:
				productos = self.conexion.cursor()
				productos.execute("SELECT * FROM Vinos ORDER BY Identificador ASC")
				resultado = productos.fetchall()
				return resultado
			except Error as ec:
				print(f"Se ha producido un error {ec}.")

	def registrarProductos(self, referencias):
		""" Method to make the registration of new products """
		if self.conexion.is_connected():
			try:
				productos = self.conexion.cursor()
				sql = "INSERT INTO Vinos (Identificador, Nombre, Precio, Stock, Lugar) VALUES (%s, %s,%s,%s,%s)"
				resultado = productos.execute(sql, referencias)
				self.conexion.commit()
				print("Productos registrados con éxito.")
			except Error as ec:
				print(f"Se ha producido el error {ec} al registrar los productos.")

	def actualizarProductos(self, referencias):
		""" Method to make actualization of the products """
		if self.conexion.is_connected():
			try:
				productos = self.conexion.cursor()
				sql = "UPDATE `Vinos` SET Nombre=%s, Precio=%s, Stock=%s, Lugar=%s WHERE Identificador=%s;"
				producto = productos.execute(sql, referencias)
				self.conexion.commit()
				print("Productos actualizados con éxito.")
			except Error as ec:
				print(f"Se ha producido el error {ec} al actualizar los productos.")

	def eliminarProducto(self, referencias_eliminar):
		""" Method to erase one product from DB """
		if self.conexion.is_connected():
			try:
				productos = self.conexion.cursor()
				sql = f"DELETE FROM Vinos WHERE Identificador={referencias_eliminar}"
				productos.execute(sql)
				self.conexion.commit()
				print("Producto eliminado con éxito.")
			except Error as ec:
				print(f"Se ha producido el error {ec} al eliminar los productos.")


