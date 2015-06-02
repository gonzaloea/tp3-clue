
class Jugador(object):
	 """Representa a un jugador manejado por un usuario.
	 Todo el manejo para pedirle y mostrarle cosas al usuario se hace utilizando su atributo "pedidos"
	 que se encarga de dichas tareas.
	 En este modulo no puede haber ninguna funcion raw_input ni print, ni ninguna semejante."""

	 def __init__(self, nombre, posicion_inicial, listado_inicial, dados, pedidos):
		"""Recibe su nombre, una posicion inicial, un listado ya inicializado, los dados a usar
		y alguien que le permita hacerle pedidos al usuario, de la manera que corresponda."""
		self.nombre = nombre
		self.posicion = posicion_inicial 
		self.listado_cartas = listado_inicial
		self.dados = dados
		self.pedidos = pedidos
		self.mano = []

	 def get_nombre(self):
		"""Devuelve el nombre del jugador"""
		return self.nombre

	 def __eq__(self, otro):
		"""Verifica si un jugador es igual a otro jugador.
		Dos jugadores son iguales cuando tienen el mismo nombre"""
		return self.nombre is otro.nombre
		
	 def asignar_carta(self, carta):
		"""Se le asigna una carta a la mano del jugador. Este la marca como vista en su listado
		de cartas."""
		self.listado_cartas.sacar_carta(carta)
		self.mano.append(carta)
	 
	 def get_posicion(self):
		"""Obtiene la posicion del jugador."""
		return self.posicion

	 def alguna_carta(self, jugada):
		"""Se fija si el jugador tiene alguna de las cartas indicadas en la jugada.
		Parametros:
				- jugada: iterable con cartas.
		Salida: si tiene al menos una de las cartas, debe preguntarle al usuario cual
		prefiere mostrarle. Si no tiene ninguna, devuelve None."""
		
		cartas_poseidas = []
		for carta in jugada:
			if carta in self.mano:
				cartas_poseidas.append(carta)
		if len(cartas_poseidas) > 1:
			return self.pedidos.pedir_carta_a_mostrar(self,cartas_poseidas)
		elif len(cartas_poseidas) == 1:
			return cartas_poseidas[0]
		return None

	 def arriesgar(self):
		"""Devuelve arriesgo del usuario (personaje, arma, jugador), o None si no desea arriesgarse."""
		return self.pedidos.preguntar_arriesgo()

	 def mover(self, tablero):
		"""Lanza los dados y se mueve en algun sentido por el tablero. Le muestra al usuario el resultado de
		haber lanzado los dados, y le pide el sentido en el que debe moverse."""
		puntos_dados=[]
		for dado in self.dados:
			puntos_dados.append(dado.lanzar())
		self.pedidos.mostrar_dados(puntos_dados)
		sentido = self.pedidos.pedir_sentido()
		self.posicion = tablero.siguiente(self.posicion, sum(puntos_dados), sentido)

	 def sugerir(self, tablero, otros_jugadores):
		"""Si esta en algun lugar para hacer sugerencias, le pregunta al usuario si desea hacer una.
		En caso afirmativo, le muestra la mano al jugador, le muestra el listado de cartas que aun no vio, 
		le pide la jugada, y le consulta al resto de los jugadores si tiene alguna
		de las cartas.
		Parametros:
				- tablero: tablero del juego.
				- otros_jugadores: un iterable con los demas jugadores, en el orden en el que se les debe consultar."""
		lugar = tablero[self.posicion]
		lista_cartas = []
		if lugar is not None:
			if self.pedidos.quiere_consultar(lugar):
				self.pedidos.mostrar_mano(self.mano)
				self.pedidos.mostrar_listado(self.listado_cartas)
				jugada = (lugar, self.pedidos.pedir_arma(), self.pedidos.pedir_personaje())
				for jugador in otros_jugadores:
					carta = jugador.alguna_carta(jugada)
					if carta is not None:
						lista_cartas.append(carta)
				if lista_cartas:
					self.pedidos.mostrar_carta(jugador,carta)
				else:
					self.pedidos.mostrar_no_hay_cartas()
