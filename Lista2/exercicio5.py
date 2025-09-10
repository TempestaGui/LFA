import re

texto = "os valores sao 45, 3.14, 00.1"

numeros = re.findall(r'-?\d+\.?\d*',texto)

#-? numero negativo
#\d+ numeros inteiros
#\.? ponto decimal
#\d* parte decimal

print(numeros)