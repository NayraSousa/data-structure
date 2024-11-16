def DigitAdder(number):
    if number<10: return number
    return (number%10)+DigitAdder(number//10)

number = int(input("Digite um número inteiro: "))
print(DigitAdder(number))