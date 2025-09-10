import re

senha_regex = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[#$%&!?])[A-Za-z\d#$%&!?]{8,16}$'

#^comeco da string
#(?=.*[a-z]) garantir que tenha pelo menos 1 letra minuscula
#(?=.*[A-Z]) garantir que tenha pelo menos 1 letra maiuscula
#(?=.*\d) garantir que tenha numero
#(?=.*[#$%&!?]) garantir que tenha algum caracter especial
#[A-Za-z\d#$%&!?]{8,16} verificar se esta dentro do temanho e com os caracteres validos 
#$ fim da string


senhas = ["Senhaaaa12!","123","SSss1234&","12345rt"]

for r in senhas:
    if re.match(senha_regex, r):
        print(f"'{r}' é valida")
    else:
        print(f"'{r}'é invalida")    