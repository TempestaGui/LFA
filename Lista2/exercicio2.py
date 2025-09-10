import re

texto = "Meus emails sao testegmail.com e teste@dominio.com.br"

email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

#[A-Za-z0-9._%+-]+ userName, nome, numero e alguns simbolos
#separador
#@[A-Za-z0-9.-] dominio
#  \.[A-Za-z]{2,} extensoes
#\b garante que seja uma palavra completa

emails = re.findall(email_regex, texto)
print(emails) 
