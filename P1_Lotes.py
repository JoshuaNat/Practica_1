class DatosO:
	"""Una clase simple para almacenar datos"""

	def __init__(self, ipv6, apellido, ipv4):
		"""Inicializa los atributos de la clase"""
		self.ipv6 = ipv6
		self.apellido = apellido
		self.ipv4 = ipv4

class DatosF:
	"""Clase para almacenar los datos de salida"""

	def __init__(self, NumH, apellido, NumD):
		"""Inicializa los atributos de la clase"""
		self.NumH = NumH
		self.apellido = apellido
		self.NumD = NumD


#Lista de datos
Datos_Originales = []
Datos_Finales = []

def contenido_archivo(filename):
	"""Abre y cierra el archivo de texto"""
	with open(filename) as lotes:
		for line in lotes: 
			info = line.split(",") #Tras leerlo linea por linea, separa las lineas por comas
			Datos_Originales.append(DatosO(info[0], info[2], info[5])) #Se asignan los valores y se anexan a la lista

def hex_a_dec():
	for obj in Datos_Originales:
		H = obj.ipv6.split(":")
		for numero in H:
			D = int(numero, base=16)
			print(D)


contenido_archivo("prueba2.txt")
hex_a_dec()