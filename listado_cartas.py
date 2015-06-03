
class ListadoCartas(object):
	 """Representa el listado de cartas que un jugador aun no visualizo. Permite llevar cuenta de las cartas
	 que ya se vieron, para saber cuales conviene consultar."""
	 def __init__(self, personajes_inicial, armas_inicial, lugares_inicial):
		"""Recibe un iterable para las cartas de personajes, armas y lugares."""
		self.personajes=personajes_inicial[:]
		self.armas=armas_inicial[:]
		self.lugares=lugares_inicial[:]

	 def __str__(self):
		"""Convierte el listado en una cadena"""
		listado_mensaje="\nArmas: \n"
		for index,arma in enumerate(self.armas):
			listado_mensaje += str(index+1) +". "+arma+"\n"
		listado_mensaje+="\nPersonajes: \n"
		for index,personaje in enumerate(self.personajes):
			listado_mensaje += str(index+1) +". "+personaje+"\n"
		listado_mensaje+="\nLugares:\n"
		for index,lugar in enumerate(self.lugares):
			listado_mensaje += str(index+1) +". "+lugar+"\n"
		return listado_mensaje

	 def sacar_carta(self, carta):
		"""Saca una determinada carta de los listados de personajes, armas y lugares (los marca como "vistos")"""
		if carta in self.personajes:
			self.personajes.remove(carta)
		elif carta in self.armas:
			self.armas.remove(carta)
		elif carta in self.lugares:
			self.lugares.remove(carta)
