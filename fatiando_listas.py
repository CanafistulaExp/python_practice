lst = "red,orange,yellow,green,blue,purple,pink,brown,black,white,gray,violet,indigo,maroon,navy".split(",")

# Exercicio de fatiamento de listas
print(lst[1::3]) #Fatiamento a cada 3 indices do indice 1 até o final da lista
print(lst[5::-1]) #Fatiamento regressivo da posição 6 até 0
print(lst[len(lst)//2::2]) #Fatiamento a cada dois indices da metade da lista até o final
