from exceptions import FormulaError

class Calculadora:
    def __init__(self, first_value, second_value, operator):
        self.first_value = first_value
        self.second_value = second_value
        self.operator = operator
        
    def get_result(self):
        if self.operator == '+':
            return self.get_sum()
        if self.operator == '-':
            return self.get_sub()
        if self.operator == '*':
            return self.get_mult()
        if self.operator == '/':
            return self.get_div()
        raise FormulaError(f"{self.operator} não é um operador válido")

    def get_sum(self):
        return self.first_value + self.second_value

    def get_sub(self):
        return self.first_value - self.second_value

    def get_mult(self):
        return self.first_value * self.second_value

    def get_div(self):
        return self.first_value / self.second_value


