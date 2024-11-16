def LargestDigit(number):
    if number<10: return number
    else:
        last_digit = number%10
        largest_digit = max(last_digit, LargestDigit(number//10))
    return largest_digit
    
number = int(input("Digite um número: "))
print(LargestDigit(number))