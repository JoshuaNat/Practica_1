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

"""
def dec_a_hex():
	cadena = ''
	for obj in list:
		D = obj.ipv4.split(".")
		ultimo = D[-1]
		for numero in D:
			H = hex(int(numero))
			cadena += H[2:] + "."
			if numero == ultimo:
				cadena += "\n"
	print(cadena)
"""

def hex_a_dec():
	for obj in list:
		cadena = obj.apellido
		H = obj.ipv6.split(":")
		ultimo = H[-1]
		for numero in H:
			if numero == ultimo:
				imp = numero.split("/")
				D = int(imp[0], base=16)
				cadena += ':' + str(D) + ':'
			else:
				D = int(numero, base=16)
				cadena += ':' + str(D)
		prueba(cadena, obj.apellido)



def prueba(cadena, apellido):
	print(cadena)
	print(f"el apellido es {apellido}")

contenido_archivo("prueba2.txt")
hex_a_dec()