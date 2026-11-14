despesas = []
total = 0
i = 0

print("""Bem-vindo ao Rastreador de Despesas Diárias!

Menu:
1. Adicionar uma nova despesa
2. Ver todas as despesas
3. Calcular o total e a média das despesas
4. Deletar todas as despesas
5. Sair""")

while i != 5:
    i = float(input("Escolha uma opção do menu: ").replace(",", "."))
    if i == 1:
        despesas.append(float(input("Digite o valor que deseja adicionar: ").replace(",", ".")))
        print("Despesa adicionada com sucesso!")
  
    elif i == 2:
        if despesas == []:
            print("Ainda não tem despesas registradas.")
        else:
            print("Suas despesas:")
            for indice, despesa in enumerate(despesas, start = 1):
                print(f"{indice}. {despesa}")
        
    elif i == 3:
        if despesas == []:
            print("Ainda não tem despesas registradas.")
        else:
            for despesa in despesas:
                total += despesa
            print(f"""Despesa total: {total}
Despesa média: {total/len(despesas)}""")
    
    elif i == 4:
        despesas.clear()
        print("Todas as despesas foram deletadas.")
    
    elif i == 5:
        print("Saindo do Rastreador de Despesas Diárias. Tchau, até a próxima!!")
    else:
        print("Escolha invalida. Por favor, escolha uma opção do menu.")
