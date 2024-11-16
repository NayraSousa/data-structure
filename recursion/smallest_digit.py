def SmallestDigit(number):
    if number<10: return number
    else:
        lastDigit = number%10
        smallestDigit = min(lastDigit, SmallestDigit(number//10))
    return smallestDigit

number = int(input("Digite um número inteiro: "))
print(SmallestDigit(number))