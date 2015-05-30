
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
		raise NotImplementedError()

	 def sacar_carta(self, carta):
		"""Saca una determinada carta de los listados de personajes, armas y lugares (los marca como "vistos")"""
		if carta in self.personajes:
			self.personajes.remove(carta)
		elif carta in self.armas:
			self.armas.remove(carta)
		elif carta in self.lugares:
			self.lugares.remove(carta)
		else:
			raise ValueError()
