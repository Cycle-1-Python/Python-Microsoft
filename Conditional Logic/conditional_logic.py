# price = input('Please enter the price: ')

# if float(price) >= 1.00:
#     tax = .07
#     print(tax)
# else:
#     tax = 0
#     print(tax)

# if float(price) >= 1.00:
#     tax = .07
# else:
#     tax = 0
# print(tax)

price = input('How much did you pay? ')

price = float(price)
if price >= 1.00:
    tax = .07
else:
    tax = 0
    print('Tax rate is: ' + str(tax))