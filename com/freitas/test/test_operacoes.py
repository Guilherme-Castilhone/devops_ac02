from unittest import TestCase
from com.freitas.operacoes import Operacoes

class TestOperacoes(TestCase):
    def setUP(self):
        self.operacoes = Operacoes()

    def test_soma(self):
        self.assertEqual(self.operacoes.soma([1, 5]), 6, "Should be 6")

   def test_divisao(self):
        self.assertEqual(self.operacoes.divisao([6, 3], 1, "Should be 1")
