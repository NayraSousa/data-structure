def DigitCounter(number):
    if number<10: return 1
    else:
        return 1+DigitCounter(number//10)
    
number = int(input("Digite um número inteiro: "))
print(DigitCounter(number))