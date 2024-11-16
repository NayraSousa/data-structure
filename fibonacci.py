def Fibonacci(number):
    if number <= 1: return 1
    return Fibonacci(number-1)+Fibonacci(number-2)

number = int(input("Digite um número inteiro: "))
print(Fibonacci(number))