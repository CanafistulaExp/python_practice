# Leia o nome da exposição
exhibition_name = input()

# Leia os tamanhos das vitrines (números separados por espaços em uma linha)
case_sizes = list(map(int, input().split()))

# Leia a idade do visitante
age = int(input())

# TODO: Gere a senha a partir dos 3 primeiros caracteres do nome da exposição (em maiúsculas)
senha = exhibition_name[0:3].upper()

# TODO: Encontre o tamanho da maior vitrine
maior_tamanho = 0
for size in case_sizes:
    if size > maior_tamanho:
        maior_tamanho = size

# Determine o preço do ingresso com base na idade
# Crianças menores de 12 anos: $5
# Idades de 12-17 e 65+: $8
# Adultos de 18-64 anos: $12
preco = 0
if age < 12:
    preco = 5
elif 12 <= age <= 17 or 65 <= age:
    preco = 8
elif 17 < age < 65:
    preco = 12

# Imprima os resultados (senha, tamanho da maior vitrine, preço do ingresso)
print(f"""{senha}
{maior_tamanho}
{preco}""")
