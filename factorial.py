def Factorial(number):
    if number==0: return 1
    return number*Factorial(number-1)

number = int(input("Digite um número inteiro: "))
print(Factorial(number))