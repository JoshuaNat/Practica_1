

def contenido_archivo(filename):
	with open(filename) as lotes:
		for line in lotes:
			contenido = line.split(",")


contenido_archivo("prueba2.txt")