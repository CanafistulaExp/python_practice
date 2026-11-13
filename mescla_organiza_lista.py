lst1 = [100, 99, 88, 77]
lst2 = [1, 9, 2, 8, 3, 7, 5]

def merge(lst1, lst2):
  
  #Checa se alguma das listas está vazia;
  if lst1 == []:
    print(lst2)
  elif lst2 == []:
    print(lst1)

  #Compara o tamanho das listas;
  elif len(lst1) >= len(lst2):
    for i in range(len(lst2)):
      lst1.append(lst2[i])
    lst1.sort()
    print(lst1)
    
  else:
    for i in range(len(lst1)):
      lst2.append(lst1[i])
    lst2.sort()
    print(lst2)

merge(lst1, lst2)
