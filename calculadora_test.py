import pytest
from calculadora import Calculadora
from exceptions import FormulaError

class TestCalculadora:
    def test_sum(self):
        calculadora = Calculadora(3, 4, '+')
        resultado = calculadora.get_result()
        assert resultado == 7.0
    
    def test_sub(self):
        calculadora = Calculadora(3, 4, '-')
        resultado = calculadora.get_result()
        assert resultado == -1.0

    def test_mult(self):
        calculadora = Calculadora(3, 4, '*')
        resultado = calculadora.get_result()
        assert resultado == 12.0

    def test_div(self):
        calculadora = Calculadora(3, 4, '/')
        resultado = calculadora.get_result()
        assert resultado == 0.75
        
    def test_result_type(self):
        calculadora = Calculadora(3, 4, '/')
        result_type = type(calculadora.get_result())
        assert result_type is float
    
    def test_operation_with_invalid_operator(self):
        calculadora = Calculadora(3, 4, 'a')
        with pytest.raises(FormulaError):
            calculadora.get_result()

    
