def SumOddDigits(number:int):
    if number==0:
        return 0
    last_digit = number%10
    if last_digit%2 != 0:
        return last_digit+SumOddDigits(number//10)
    return SumOddDigits(number//10)

print(SumOddDigits(569))
