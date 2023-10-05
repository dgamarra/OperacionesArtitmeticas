import unittest
import math

from src.OperacionesAritmeticas import OperacionesAritmeticas


class PruebaOperacionesAritmeticas(unittest.TestCase):
    def test_suma_dosNumeros_respuetaSuma(self):
        # Arrange
        operacion = OperacionesAritmeticas()
        sumando1 = 13.67
        sumando2 = 15.20
        resultadoEsperado = 28.87

        # Do
        resultadoActual = operacion.suma(sumando1, sumando2)

        # Assert
        diferencia=math.fabs(resultadoEsperado - resultadoActual)
        self.assertLessEqual(diferencia,0.1)
