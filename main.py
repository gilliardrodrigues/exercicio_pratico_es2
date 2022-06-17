from calculadora import Calculadora
from exceptions import FormulaError

data = input("Insira a operação a ser feita separada por espaço: ").split()

if len(data) != 3:
    raise FormulaError("A entrada não consiste de 3 elementos")
else:
    try:
        first_value = float(data[0])
        second_value = float(data[2])
    except ValueError:
        raise FormulaError("O primeiro e o terceiro valor de entrada devem ser números")
    operator = data[1]

calculadora = Calculadora(first_value, second_value, operator)

print("Resultado: " + str(calculadora.get_result()))