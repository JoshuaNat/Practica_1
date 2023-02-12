class Datos:
	"""Una clase simple para almacenar datos"""

	def __init__(self, ipv6, apellido, ipv4):
		"""Inicializa los atributos de la clase"""
		self.ipv6 = ipv6
		self.apellido = apellido
		self.ipv4 = ipv4


#Lista de datos
list = []


def contenido_archivo(filename):
	"""Abre y cierra el archivo de texto"""
	with open(filename) as lotes:
		for line in lotes: 
			info = line.split(",") #Tras leerlo linea por linea, separa las lineas por comas
			list.append(Datos(info[0], info[2], info[5])) #Se asignan los valores y se anexan a la lista

def hex_a_dec():
	for obj in list:
		H = obj.ipv6.split(":")
		for numero in H:
			D = int(numero, base=16)
			print(D)


contenido_archivo("prueba2.txt")
hex_a_dec()