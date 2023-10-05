class OperacionesAritmeticas:
    def suma(self, sumando1, sumando2):
        return sumando1 + sumando2

    def MCD(self, numero1, numero2):
        temporal = 0
        while numero2 != 0:
            temporal = numero2
            numero2 = numero1 % numero2
            numero1 = temporal
        return numero1
