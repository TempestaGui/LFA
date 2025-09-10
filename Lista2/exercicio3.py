import re

texto = "banco brincar bolso burro baba"
palavras = re.findall(r'\bb\w{4}\b', texto)

#\bb garante que seja uma palavra que comece com b
#\w{4} garante que tenha 4 caracteres seguidos

print(palavras)