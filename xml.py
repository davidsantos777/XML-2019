def nombreruta(doc):
	lista_loc = doc.xpath("/OpenData/OpenDataRow/Nombre/text()")
	lista_dif = doc.xpath("/OpenData/OpenDataRow/IdDificultad/text()")
	return zip(lista_loc,lista_dif)

def contar_caminos(doc):
	contador = 0
	for i in doc.xpath("/OpenData/OpenDataRow/CaminoSantiago_SN/text()"):
		if i == "N":
			contador += 1
	return contador

def longitud(doc):
	lista_long = doc.xpath("/OpenData/OpenDataRow/Longitud/text()")
	lista_id = doc.xpath("/OpenData/OpenDataRow/IdRecursoCategoria/text()")
	return zip(lista_long,lista_id)


from lxml import etree
doc = etree.parse('ciclismo.xml')
while True:
	print('''1.- Lista todos los nombres de las rutas cuya ID de dificultad sea 144.
2.- Contar todos los recorridos que no formen parte del camino de santiago.
3.- Mostrar la Id del recurso de categoría de las rutas cuya longitud está entre un límite inferior y otro superior.
4.- Pedir codigo de recurso y mostrar nombre de la ruta asociado a dicho codigo.
5.- Pedir por teclado una zona, mostrar las rutas que formen parte de dicha zona junto con su dificultad y mostrar si tienen o no diploma.
0.- Salir''')

	opcion = input("Opción:")

	if opcion=="1":
		for loc,dif in nombreruta(doc):
			if dif == "144":
				print("Nombre de ruta:",loc)

	if opcion=="2":
		print("Número de rutas que no forman parte del camino de santiago:",contar_caminos(doc))

	if opcion=="0":
		break