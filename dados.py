# -*- encoding: utf-8 -*-
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
		self.prob_caras = prob_caras

	def lanzar(self):
		"""Lanza el dado y devuelve el resultado.

		Devuelve:
		- un entero entre 1 y N, siendo N el número de caras.
		"""
		return 0
		
	def obtener_probabilidades(self):
		"""Devuelve una copia de las probabilidades de ocurrencia de cada cara del dado."""
		return self.prob_caras


class DadoEstandar(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades estandar."""

	 def __init__(self, caras):
		probabilidad = float(1)/caras
		prob_caras = [probabilidad] * caras
		Dado.__init__(self,prob_caras)

class DadoCreciente(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades creciente."""
	 def __init__(self, caras):
		pass


class DadoDecreciente(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades decreciente."""
	 def __init__(self, caras):
		raise NotImplementedError()


class DadoTriangular(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades triangular:
	 las caras cercanas al valor medio tienen mayor probabilidad, y a medida que nos alejamos
	 de dicho valor la probabilidad va disminuyendo."""
	 def __init__(self, caras):
		inicial = 1
		final = caras
		medio = math.ceil(float(final)/2)
		prob_caras=[]	
		medio_par = -1
		
		#Para que cuando es par sean iguales los del medio.
		if caras % 2 == 0:
			medio_par = medio+1
			
		#Casos especiales en donde el calculo no funciona
		if caras == 1:
			prob_caras = [1]
		elif caras == 2:
			prob_caras = [0.5,0.5]
		else:
		#Si no son los casos especiales hago el cálculo.
			for valor in range(inicial,final+1):
				prob=None
				if valor >= inicial and valor < medio:
					prob = float(2*(valor-inicial))/((final-inicial)*(medio-inicial))
				elif valor == medio:
					prob = 2/float(final-inicial)
				elif valor == medio_par:
					prob = 2/float(final-inicial)
					medio = medio_par
				elif valor > medio and valor <= final:
					prob = float(2*(final-valor))/((final-inicial)*(final-medio))
				if prob is not None:
					prob_caras.append(prob)
		Dado.__init__(self,prob_caras)


GENERADORES = [DadoEstandar, DadoCreciente, DadoDecreciente, DadoTriangular]
