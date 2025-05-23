import unittest

class TestLista(unittest.TestCase):
    def test_ordenacao(self):
        lista = [3, 1, 2]
        self.assertEqual(sorted(lista), [1, 2, 3], "❌ Lista não ordenada corretamente")

    def test_elementos(self):
        lista = [3, 1, 2]
        for num in [1, 2, 3]:
            self.assertIn(num, lista, f"❌ Número {num} não está na lista")

# Execução manual (para Google Colab/GitHub sem comando unittest)
if __name__ == "__main__":
    tester = TestLista()
    tester.test_ordenacao()
    tester.test_elementos()
    print("✅ Todos os testes de lista passaram!")
