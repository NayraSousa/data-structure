def ResetPairs(number):
    if number==0: return 0
    else:
        last_digit = number%10
        if last_digit%2==0:
            last_digit = 0
        return ResetPairs(number//10)*10 + last_digit
    
number = int(input("Digite um número inteiro: "))
print(ResetPairs(number))