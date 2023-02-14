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
		dec_a_hex(cadena, obj.ipv4)
		#nuevo_archivo(cadena)

def dec_a_hex(cadena, ID):
	for obj in list:
		if ID == obj.ipv4:
			D = obj.ipv4.split(".")
			ultimo = D[-1]
			for numero in D:
				H = hex(int(numero))
				if numero == ultimo:
					cadena += H[2:]
				else:
					cadena += H[2:] + "."
			nuevo_archivo(cadena)


def nuevo_archivo(cadena):
	with open("prueba3.txt", "a") as final:
		final.write(cadena)
		final.write("\n")



contenido_archivo("prueba2.txt")
hex_a_dec()