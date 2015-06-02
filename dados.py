# -*- encoding: utf-8 -*-
import random
import math
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
		self.prob_caras = prob_caras[:]

	def lanzar(self):
		"""Lanza el dado y devuelve el resultado.

		Devuelve:
		- un entero entre 1 y N, siendo N el número de caras.
		"""
		prob = random.random()
		acum = 0
		for i,p in enumerate(self.prob_caras, start = 1):
			acum += p
			if acum >= prob:
				return i
		
	def obtener_probabilidades(self):
		"""Devuelve una copia de las probabilidades de ocurrencia de cada cara del dado."""
		return self.prob_caras[:]


class DadoEstandar(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades estandar."""
	 def __init__(self, caras):
		if caras <= 0:
			raise ValueError
		probabilidad = float(1)/caras
		prob_caras = [probabilidad] * caras
		Dado.__init__(self,prob_caras)

class DadoCreciente(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades creciente."""
	 def __init__(self, caras):
		if caras <= 0:
			raise ValueError
		caras_lista = range(1,caras+1)
		total = sum(caras_lista)
		prob_caras = [float(i)/ total for i in caras_lista]
		Dado.__init__(self,prob_caras)


class DadoDecreciente(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades decreciente."""
	 def __init__(self, caras):
		if caras <= 0:
			raise ValueError
		caras_lista = range(1,caras+1)
		total = sum(caras_lista)
		prob_caras = [float(i)/ total for i in caras_lista]
		Dado.__init__(self,prob_caras[::-1])


class DadoTriangular(Dado):
	 """Clase que representa un dado con una distribucion de probabilidades triangular:
	 las caras cercanas al valor medio tienen mayor probabilidad, y a medida que nos alejamos
	 de dicho valor la probabilidad va disminuyendo."""
	 def __init__(self, caras):
		if caras <= 0:
			raise ValueError
		lista=range(1,caras+1)
		medio = caras/2
		if caras % 2==0:
			creciente = lista[:medio]
			decreciente = lista[medio-1::-1]
		else:
			creciente = lista[:medio] 
			decreciente = lista[medio::-1]
		suma_total = sum(creciente)+ sum(decreciente)
		prob_caras=[i/float(suma_total) for i in creciente]
		prob_caras.extend([i/float(suma_total) for i in decreciente])
		Dado.__init__(self,prob_caras)

GENERADORES = [DadoEstandar, DadoCreciente, DadoDecreciente, DadoTriangular]
