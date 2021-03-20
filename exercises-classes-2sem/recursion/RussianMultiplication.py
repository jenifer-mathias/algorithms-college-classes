# 1) A multiplicação Russa consiste em:
# a. Escrever os números A e B, que se deseja multiplicar na parte superior das
# colunas.
# b. Dividir A por 2, sucessivamente, ignorando o resto até chegar à 1, escrever os
# resultados da coluna A.
# c. Multiplicar B por 2 tantas vezes quantas se tenha dividido A por 2, escrever os
# resultados sucessivos na coluna B.
# d. Somar todos os números da coluna B que estejam ao lado de um número
# ímpar da coluna A.

# Exemplo: 27 × 82 = 2214
# A    B   Parcelas
# 27   82    82
# 13  164   164
# 6   328    -
# 3   656   656
# 1  1312   1312
# Soma: 2214

def russianMultiplication(a, b):
