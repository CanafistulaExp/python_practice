# Leia dois números inteiros para o cálculo da potência
num1 = int(input())
num2 = int(input())

# Exercício
# Calcule num1 elevado à potência de num2
# Depois, encontre o primeiro dígito do resultado
leading_digit = str((num1 ** num2))[0:1]
print(leading_digit)

message = input()

# Exercício 2
# Reorganize a mensagem movendo as consoantes para o início
# Mantenha as vogais (a, e, i, o, u - maiúsculas e minúsculas), os espaços e a pontuação depois das consoantes
# Mantenha a ordem original dentro de cada grupo
temp = ""
rearranged = ""
for i in range(len(message)):
  if message[i] not in "AEIOUaeiou 0123456789!@#$%¨&*()_-=+§":
    rearranged += message[i]
  else:
    temp += message[i]

rearranged += temp

print(rearranged)
