import re
print("exemplo 1:  \n")

regex = re.compile(r'(a|b)*(aa|bb)')

testes = ["abba", "aabb", "bbaa", "abab", "baab"]
for t in testes:
    if regex.fullmatch(t):
        print(f"{t} → aceita")
    else:
        print(f"{t} → rejeita")


print("exemplo 2:  \n")

regex = re.compile(r'a*b{1}a*b{1}a*')

testes = ["bb", "abba", "aabbaa", "baaab", "aaa"]
for t in testes:
    if regex.fullmatch(t):
        print(f"{t} → aceita")
    else:
        print(f"{t} → rejeita")

print("exemplo 3:  \n")

regex = re.compile(r'(a|)(b|ba)*')

testes = ["b", "ba", "bababa", "ababa", "aab"]
for t in testes:
    if regex.fullmatch(t):
        print(f"{t} → aceita")
    else:
        print(f"{t} → rejeita")
