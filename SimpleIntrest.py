principal= eval(input('Enter the principal amount: '))
rate = eval(input('Enter the annual interest rate :'))
time = eval(input('Time period :'))
simple_int = (principal*rate*time)/100
amount = simple_int + principal

print('Simple Interest = ', simple_int)
print('Payable Amount = ', amount)
