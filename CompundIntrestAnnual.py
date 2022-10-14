principal = eval(input('enter the principal amount :'))
rate = eval(input('enter the annual interest rate :'))
time = eval(input('enter the time :'))
compound_int = principal * (pow((1 + rate / 100), time))
amount = compound_int - principal

print('Compound intrest =', amount)
print('Payable amount =', compound_int)