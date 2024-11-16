def ReverseDigits(number, inverse=0):
    if number==0:
        return inverse
    else:
        last_digit = number%10
        inverse = inverse*10 + last_digit
        return ReverseDigits(number//10, inverse)
    
number = int(input("Digite um número inteiro: "))
print(ReverseDigits(number))