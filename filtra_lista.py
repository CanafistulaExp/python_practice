lst1 = [1,2,3,4,5]
lst2 = [2,4,6]

nova_lista = []
for i in lst1:
    if i not in lst2:
        nova_lista.append(i)

print(nova_lista)
