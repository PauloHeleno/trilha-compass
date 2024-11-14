def calcular_valor_maximo(operadores, operandos) -> float:
    lista = zip(operadores, operandos)
    return float(max(map(lambda x: x[1][0] + x[1][1] if x[0] == '+' 
                         else x[1][0] - x[1][1] if x[0] == '-' 
                         else x[1][0] * x[1][1] if x[0] == '*' 
                         else x[1][0] / x[1][1] if x[0] == '/' 
                         else float('-inf'), lista)))


operadores = ['+','-','*','/','+']
operandos  = [(3,6), (-7,4.9), (8,-8), (10,2), (8,4)]

print(calcular_valor_maximo(operadores, operandos))

