def contar_caminos(doc):
	lista = []
	lista_caminos = doc.xpath("count(/OpenData/OpenDataRow[@CaminoSantiago_SN='N'])")
	lista.append(int(lista_caminos))
	return lista