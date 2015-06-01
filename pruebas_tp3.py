# Importa el paquete para realizar pruebas automatizadas de Python.
import unittest
from unittest import TestCase

# Importa las clases que se van a probar
from dados import DadoEstandar
from dados import DadoCreciente
from dados import DadoDecreciente
from dados import DadoTriangular
from tablero import Tablero
from listado_cartas import ListadoCartas



# Definimos una clase que hereda de TestCase por cada Clase que queremos probar.

#Se creo una clase para dado en general para probar varias cosas en comun de los dados.
class TestDado(TestCase):
	 # Este otro metodo, por ejemplo, verifica que las probabilidades de ocurrencia de
	 # cada cara no se puedan modificar.
	def test_probabilidades_no_se_deben_modificar(self):
		 #El metodo "obtener_probabilidades" corresponde a la clase padre Dado. 
		 #Por lo tanto, no tiene caso probarlo en todos los tipos.
		dado = DadoEstandar(6)
		probabilidades = dado.obtener_probabilidades()

		# Modifico el resultado devuelto.
		probabilidad_anterior = probabilidades[0]
		probabilidades[0] = probabilidad_anterior + 1

		# Verifico que no se haya modificado su probabilidad dentro del dado.
		self.assertEqual(probabilidad_anterior, dado.obtener_probabilidades()[0])

# Esta clase esta dedicada a probar la clase de DadoEstandar.
class TestDadoEstandar(TestCase):

	 # Cada metodo debe probar una funcionalidad de la clase.
	 # Este, por ejemplo, verifica que las probabilidades de cada cara son iguales.
	def test_probabilidades_son_equiprobables(self):
		# Dentro de un metodo realizo la prueba:

		# Creo un dado estandar de seis caras.
		dado = DadoEstandar(6)

		# Obtengo sus probabilidades.
		# Este metodo no se usa en el juego pero se agrego para poder correr la prueba.
		probabilidades = dado.obtener_probabilidades()

		prob = probabilidades[0]
		for i in range(1, len(probabilidades)):
				# Se usan los metodos de unittest para hacer verificaciones.
				self.assertEqual(prob, probabilidades[i])

	def test_porcentaje_probabilidades_es_cien(self):
		#Se usa 0.99 porque por razones de aproximacion al dividir nunca llega a dar 1 la suma.
		dado = DadoEstandar(6)
		self.assertTrue(sum(dado.obtener_probabilidades()) > 0.99)


class TestDadoCreciente(TestCase):
	def test_probabilidades_son_crecientes(self):
		dado = DadoCreciente(5)
		prob_anterior = 0
		
		for probabilidad in dado.obtener_probabilidades():
			self.assertTrue(probabilidad > prob_anterior)
			prob_anterior = probabilidad
	def test_porcentaje_probabilidades_es_cien(self):
		#Se usa 0.99 porque por razones de aproximacion al dividir nunca llega a dar 1 la suma.
		dado = DadoCreciente(6)
		self.assertTrue(sum(dado.obtener_probabilidades()) > 0.99)

class TestDadoDecreciente(TestCase):
	def test_probabilidades_son_decrecientes(self):
		dado = DadoDecreciente(5)
		prob_anterior = 2
		
		for probabilidad in dado.obtener_probabilidades():
			self.assertTrue(probabilidad < prob_anterior)
			prob_anterior = probabilidad
	def test_porcentaje_probabilidades_es_cien(self):
		#Se usa 0.99 porque por razones de aproximacion al dividir nunca llega a dar 1 la suma.
		dado = DadoDecreciente(6)
		self.assertTrue(sum(dado.obtener_probabilidades()) > 0.99)

class TestDadoTriangular(TestCase):
	def test_prob_son_triang_con_caras_par(self):
		dado = DadoTriangular(6)
		prob_anterior = 0
		
		for prob in dado.obtener_probabilidades()[:3:]:
			self.assertTrue(prob > prob_anterior)
			prob_anterior = prob
		for prob in dado.obtener_probabilidades()[3::]:
			self.assertTrue(prob <= prob_anterior)
			prob_anterior = prob
		
	def test_prob_son_triang_con_caras_impar(self):
		dado = DadoTriangular(5)
		prob_anterior=0
		for prob in dado.obtener_probabilidades()[:3:]:
			self.assertTrue(prob > prob_anterior)
			prob_anterior = prob
		for prob in dado.obtener_probabilidades()[4::]:
			self.assertTrue(prob < prob_anterior)
			prob_anterior = prob

	def test_porcentaje_probabilidades_es_cien(self):
		dado = DadoTriangular(6)
		self.assertEqual(sum(dado.obtener_probabilidades()), 1)
		
		dado = DadoTriangular(5)
		self.assertEqual(sum(dado.obtener_probabilidades()), 1)
		
class TestTablero(TestCase):

	 # Prueba que la creacion usando listas de diferentes largos levante una excepcion.
	 def test_inicializacion_con_distintos_largos_invalida(self):
		casilleros = ['1', None, '3']
		posiciones = ['1', '2']

		# Estructura que verifica que se levante una excepcion de tipo ValueError
		# dentro del bloque with.
		with self.assertRaises(ValueError):
				Tablero(casilleros, posiciones)

	 # Prueba que los casilleros no se puedan modificar desde afuera.
	 def test_casilleros_no_se_deben_modificar(self):
		casilleros = [1,2,3]
		posiciones = [(1,1),(2,2),(3,3)]
		tablero = Tablero(casilleros, posiciones)
		
		casilleros[0]=2
		
		self.assertNotEqual(casilleros[0], tablero[0])


class TestListadoCartas(TestCase):
	#Prueba que los distintos tipos de cartas no se puedan modificar desde afuera.
	def test_listados_de_cartas_no_se_modifican(self):
		carta_arma_prueba = "arma1"
		carta_pj_prueba = "pj1"
		carta_lugar_prueba = "lugar1"
		
		armas=[carta_arma_prueba,"arma2"]
		personajes=[carta_pj_prueba,"pj2"]
		lugares=[carta_lugar_prueba,"lugar2"]
		
		listado = ListadoCartas(personajes, armas, lugares)
		
		listado.sacar_carta(carta_arma_prueba)
		self.assertTrue(armas[0] is carta_arma_prueba)
		
		listado.sacar_carta(carta_pj_prueba)
		self.assertTrue(personajes[0] is carta_pj_prueba)
		
		listado.sacar_carta(carta_lugar_prueba)
		self.assertTrue(lugares[0] is carta_lugar_prueba)
	def test_sacar_carta_inexistente(self):
		listado = ListadoCartas([], [], [])
		with self.assertRaises(ValueError):
			listado.sacar_carta("")


# Ejecuta todas las pruebas cuando se ejecute este archivo.
if __name__ == "__main__":
	 unittest.main()
