class Datos:
	"""Una clase simple para almacenar datos"""

	def __init__(self, ipv6, nombre, apellido, correo, genero, ipv4):
		"""Inicializa los atributos de la clase"""
		self.ipv6 = ipv6
		self.nombre = nombre
		self.apellido = apellido
		self.correo = correo
		self.genero = genero
		self.ipv4 = ipv4

def contenido_archivo(filename):
	"""Abre y cierra el archivo de texto"""
	with open(filename) as lotes:
		for line in lotes: 
			info = line.split(",") #Tras leerlo linea por linea, separa las lineas por comas
			mis_datos = Datos(info[0], info[1], info[2], info[3], info[4], info[5]) #Se asignan los valores correspondientes a los atributos de la clase


contenido_archivo("prueba2.txt")