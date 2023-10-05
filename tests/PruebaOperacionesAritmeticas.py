import math
import unittest

from src.OperacionesAritmeticas import OperacionesAritmeticas


class PruebaOperacionesAritmeticas(unittest.TestCase):
    def setUp(self):
        self.operacion = OperacionesAritmeticas()

    def tearDown(self):
        self.operacion = None

    def test_suma_dosNumeros_respuetaSuma(self):
        # Arrange
        sumando1 = 13.67
        sumando2 = 15.20
        resultadoEsperado = 28.87

        # Do
        resultadoActual = self.operacion.suma(sumando1, sumando2)

        # Assert
        diferencia = math.fabs(resultadoEsperado - resultadoActual)
        self.assertLessEqual(diferencia, 0.1)

    def test_MCD_dosNumerosNaturales_respuetaMCD(self):
        # Arrange
        numero1 = 12
        numero2 = 48
        resultadoEsperado = 12

        # Do
        resultadoActual = self.operacion.MCD(numero1, numero2)

        # Assert
        self.assertEqual(resultadoActual, resultadoEsperado)
