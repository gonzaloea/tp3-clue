
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
        return self.name is otro.name
        
    def asignar_carta(self, carta):
        """Se le asigna una carta a la mano del jugador. Este la marca como vista en su listado
        de cartas."""
        self.listado_inicial.sacar_carta(carta)
        mano.append(carta)
    
    def get_posicion(self):
        """Obtiene la posicion del jugador."""
        return posicion

    def alguna_carta(self, jugada):
        """Se fija si el jugador tiene alguna de las cartas indicadas en la jugada.
        Parametros:
            - jugada: iterable con cartas.
        Salida: si tiene al menos una de las cartas, debe preguntarle al usuario cual
        prefiere mostrarle. Si no tiene ninguna, devuelve None."""
        raise NotImplementedError()

    def arriesgar(self):
        """Devuelve arriesgo del usuario (personaje, arma, jugador), o None si no desea arriesgarse."""
        raise NotImplementedError()

    def mover(self, tablero):
        """Lanza los dados y se mueve en algun sentido por el tablero. Le muestra al usuario el resultado de
        haber lanzado los dados, y le pide el sentido en el que debe moverse."""
        raise NotImplementedError()

    def sugerir(self, tablero, otros_jugadores):
        """Si esta en algun lugar para hacer sugerencias, le pregunta al usuario si desea hacer una.
        En caso afirmativo, le muestra la mano al jugador, le muestra el listado de cartas que aun no vio, 
        le pide la jugada, y le consulta al resto de los jugadores si tiene alguna
        de las cartas.
        Parametros:
            - tablero: tablero del juego.
            - otros_jugadores: un iterable con los demas jugadores, en el orden en el que se les debe consultar."""
        raise NotImplementedError()
