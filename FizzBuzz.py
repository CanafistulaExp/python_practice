print("Welcome to FizzBuzz!")
n = int(input("Escolha um número inteiro para começar o jogo: "))

def fizzbuzz(num = int()):
  for i in range(1,num+1):
    
    #Checa se o contem no núemro 3 e se não é divisivel por 3 ou 7
    if (i % 3 != 0 and i % 7 != 0 and "3" in str(i)):
      print("Almost Fizz")

    else:
      #Números divisiveis por 3 e 7 são substituidos por "FizzBuzz"
      if i % 3 == 0 and i % 7 == 0:
        print("FizzBuzz")

      #Números divisiveis por 7 são substituidos por "Buzz"
      elif i % 7 == 0:
        print("Buzz")

      #Números divisiveis por 3 são substituidos por "Fizz"
      elif i % 3 == 0:
        print("Fizz")

      
      else:
        print(i)

fizzbuzz(n)
