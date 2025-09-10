import re

texto = "Ligue para (11) 11111-1111 ou (22) 22222-2222"

telefone_regex = r'\(\d{2}\) \d{4,5}-\d{4}'

#\(\d{2}\) DDD
#\d{4,5} prefixo de 4 ou 5 numeros
#\d{4} sufixo de 4 numeros

novo_telefone = re.sub(telefone_regex,'[telefone]', texto)
print(novo_telefone)

