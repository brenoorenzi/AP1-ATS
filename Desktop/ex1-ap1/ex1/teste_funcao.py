import unittest
from funcao import calcular_area

class TestCalcularArea(unittest.TestCase):

    def test_funcional(self):
        resultado = calcular_area(5, 10)
        self.assertEqual(resultado, 50)

    def test_type_error(self):
        with self.assertRaises(TypeError):
            calcular_area("cinco", 10)

    def test_value_error(self):
        with self.assertRaises(ValueError):
            calcular_area(-5, 10)

if __name__ == '__main__':
    unittest.main()