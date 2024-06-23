user_age = 12
user_country = 'BG'

if user_age:
    if user_age>=18 and user_country=='BG':
        print('111')
    elif user_age>=18 or user_country=='BG':
        print('222')
    else:
        print('333')
else:
    print('444')
