n = 0
n2 = 1

print("Sequência de Fibonacci:")
# A sequência começa em 0 e o for define até que linha da sequência será exibida
for i in range(12):
  print(f"{i}. {n}")
  n += n2
  n2 = n - n2
