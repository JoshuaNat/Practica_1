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
	for obj in list: #Recorre todos los objetos en la lista
		cadena = obj.apellido
		H = obj.ipv6.split(":") #H es una lista de todos los numeros hex de la ipv6
		ultimo = H[-1]
		for numero in H:
			if numero == ultimo:
				imp = numero.split("/") #El ultimo numero en hex tiene una diagonal, hacemos esto para separar el número
				D = int(imp[0], base=16) #y solo trabajar con los valores antes de la diagonal
				cadena += ':' + str(D) + ':'
			else:
				D = int(numero, base=16) #convertimos el valor en hex a valor dec
				cadena += ':' + str(D)
		dec_a_hex(cadena, obj.ipv4) #mandamos la cadena y la ipv4 como una id
		#nuevo_archivo(cadena)

def dec_a_hex(cadena, ID):
	for obj in list: #revisamos cada objeto en la lista
		if ID == obj.ipv4: #y trabajamos con el que tenga la misma ipv4 que recibimos
			D = obj.ipv4.split(".") #dividimos la ipv4
			ultimo = D[-1]
			for numero in D:
				H = hex(int(numero)) #convertimos los numeros en Dec a Hex
				if numero == ultimo:
					cadena += H[2:]
				else:
					cadena += H[2:] + "."
			nuevo_archivo(cadena) #Enviamos la cadena resultante a la ultima función.


def nuevo_archivo(cadena):
	with open("prueba3.txt", "a") as final:
		final.write(cadena) #adjuntamos la linea obtenida junto a un salto de linea
		final.write("\n")



contenido_archivo("prueba2.txt")
hex_a_dec()