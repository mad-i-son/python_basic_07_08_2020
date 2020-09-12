"""
1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
 Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
"""
var1 = 5
var2 = 6
operation_and = var1 & var2
operation_or = var1 | var2
operation_xor = var1 ^ var2
operation_not = ~ var2

print(f'Над числами 5 и 6 (бинарное представление {bin(var1)} и {bin(var2)}) проведены операции:\n'
      f'1) Логическое И: {operation_and} (бинарное представление {bin(operation_and)});\n'
      f'2) Логическое ИЛИ: {operation_or} (бинарное представление {bin(operation_and)});\n'
      f'3) Исключающее ИЛИ: {operation_xor} (бинарное представление {bin(operation_and)});\n'
      f'4) Отрицание: {operation_xor} (бинарное представление {bin(operation_and)}).\n')

var_left = var1 << 2
var_right = var1 >> 2
print(f'Над числом 5 (бинарное представление {bin(var1)})\nвыполнен побитовый сдвиг вправо: {bin(var_right)}'
      f' и влево на два знака: {bin(var_left)}')