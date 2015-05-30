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

	 # Este otro metodo, por ejemplo, verifica que las probabilidades de ocurrencia de
	 # cada cara no se puedan modificar.
	 def test_probabilidades_no_se_deben_modificar(self):
		dado = DadoEstandar(6)
		probabilidades = dado.obtener_probabilidades()

		# Modifico el resultado devuelto.
		probabilidad_anterior = probabilidades[0]
		probabilidades[0] = probabilidad_anterior + 1

		# Verifico que no se haya modificado su probabilidad dentro del dado.
		self.assertEqual(probabilidad_anterior, dado.obtener_probabilidades()[0])

class TestDadoCreciente(TestCase):
	pass

class TestDadoDecreciente(TestCase):
	pass

class TestDadoTriangular(TestCase):
	pass

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
