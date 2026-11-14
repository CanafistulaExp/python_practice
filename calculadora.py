print("""Bem-vindo!!

Informe a operação desejada:
1. Somar (+)
2. Subtrair (-)
3. Multiplicar (*)
4. Dividir (/)
5. Potência (^)
0. Sair""")

x = y = 0
i = None

while i != 0:
    i = float(input("Informe a operação desejada: ").replace(",", ".").replace("+", "1").replace("-", "2").replace("*", "3").replace("/", "4").replace("^","5"))
    if i == 1:
        x = float(input("Informe o primeiro número: ").replace(",", "."))
        y = float(input("Informe o segundo número: ").replace(",", "."))
        print(f"A soma de {x} + {y} é = {x+y}")
    elif i == 2:
        x = float(input("Informe o primeiro número: ").replace(",", "."))
        y = float(input("Informe o segundo número: ").replace(",", "."))
        print(f"A subtração de {x} - {y} é = {x-y}")
    
    elif i == 3:
        x = float(input("Informe o primeiro número: ").replace(",", "."))
        y = float(input("Informe o segundo número: ").replace(",", "."))
        print(f"O produto de {x} * {y} é = {x*y}")

    elif i == 4:
        x = float(input("Informe o primeiro número: ").replace(",", "."))
        y = float(input("Informe o segundo número: ").replace(",", "."))
        print(f"O quociente de {x} / {y} é = {x/y}")
    
    elif i == 5:
        x = float(input("Informe o primeiro número: ").replace(",", "."))
        y = float(input("Informe o segundo número: ").replace(",", "."))
        print(f"{x} elevado a {y} = {x**y}")
    
    elif i == 0:
        print("Tachu, até a próxima!!")
    
    else:
        print("Operador matemático inválido. Tente uma opção do menu.")
