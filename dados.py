TIPO_DADO_ESTANDAR = "Estandar (todas las caras equiprobables)"
TIPO_DADO_CRECIENTE = "Creciente"
TIPO_DADO_DECRECIENTE = "Decreciente"
TIPO_DADO_TRIANGULAR = "Triangular"
TIPOS_DADOS = [TIPO_DADO_ESTANDAR, TIPO_DADO_CRECIENTE, TIPO_DADO_DECRECIENTE, TIPO_DADO_TRIANGULAR]


class Dado(object):
	"""Clase que representa un dado cargado para obtener un número
	  aleatorio, con una probabilidad diferente por cada cara.
	  """
	def __init__(self, prob_caras):
		"""Recibe un iterable con las probabilidades de cada resultado
		del dado.

		Parametros:
		  - prob_caras: un iterable con tantos elementos como caras
			tiene el dado. El elemento n-ésimo de este iterable es
			la probabilidad de la cara N.

			La suma de las probabilidades debe ser 1 (o muy similar),
			si no lanzará una excepcion de tipo ValueError.
		"""
		raise NotImplementedError()

    def lanzar(self):
		"""Lanza el dado y devuelve el resultado.

		Devuelve:
        - un entero entre 1 y N, siendo N el número de caras.
		"""
		raise NotImplementedError()
        
	def obtener_probabilidades(self):
		"""Devuelve una copia de las probabilidades de ocurrencia de cada cara del dado."""
		raise NotImplementedError()


class DadoEstandar(Dado):
    """Clase que representa un dado con una distribucion de probabilidades estandar."""

    def __init__(self, caras):
        raise NotImplementedError()


class DadoCreciente(Dado):
    """Clase que representa un dado con una distribucion de probabilidades creciente."""
    def __init__(self, caras):
        raise NotImplementedError()


class DadoDecreciente(Dado):
    """Clase que representa un dado con una distribucion de probabilidades decreciente."""
    def __init__(self, caras):
        raise NotImplementedError()


class DadoTriangular(Dado):
    """Clase que representa un dado con una distribucion de probabilidades triangular:
    las caras cercanas al valor medio tienen mayor probabilidad, y a medida que nos alejamos
    de dicho valor la probabilidad va disminuyendo."""
    def __init__(self, caras):
        raise NotImplementedError()


GENERADORES = [DadoEstandar, DadoCreciente, DadoDecreciente, DadoTriangular]
