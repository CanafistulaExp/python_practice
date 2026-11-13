lst = list(map(int, input().split(",")))

lista_ind = []
for index, i in enumerate(lst):
  if i < 50 or i % 5 == 0:
    lista_ind.append(index)
  else:
    continue

print(lista_ind)
