# Use string functions to make case insensitive comparisons

# country = 'CANADA'
# if country.lower() == 'canada':
#     print('oh look a Canadian')
# else:
#     print('You are not from Canada')


country = input('Enter the name of your home country: ')

if country.lower() == 'canada':
    print('So you must like hockey!')
else:
    print('You are not from Canada')