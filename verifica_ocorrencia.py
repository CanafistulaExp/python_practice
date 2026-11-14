a = input()
b = input()

def find_occurrences(text, pattern):
    position = []
    valid = False
    for i in range(len(text)):
        if pattern in text[i:i+len(pattern)]:
            position.append(i)
    if position != []:
        valid = True
    return(valid, len(position), position) #Verifica se b está em a, informa quantas vezes ocorre e indica o indice onde b aparece

resultado = find_occurrences(a, b)
print(resultado)
