frequency = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

def frequency_counter(data_list):
    dicionario = {}
    j = 0

    for data in data_list:
        for i in range(len(data_list)):
            if data == data_list[i]:
                j += 1
        dicionario[data] = j
        j = 0

    return dicionario

print(frequency_counter(frequency))
