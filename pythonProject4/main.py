input_month = input()
input_day = int(input())

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
          'November', 'December']

# Checking for Invalid month and day entries
if (input_month not in months) or (input_day <= 0):
    print('Invalid')

# Split Season Months
elif input_month == 'March':
    if (input_day > 21) and (input_day < 31):
        print('Spring')
    elif(input_day < 21):
        print('Winter')
    else:
        print('Invalid')

elif input_month == 'June':
    if(input_day < 21):
        print('Spring')
    elif((input_day >= 21) and (input_day < 31)):
        print('Summer')
    else:
        print('Invalid')

elif (input_month == 'September'):
    if (input_day < 22):
        print('Summer')
    elif (input_day >= 22) and (input_day < 31):
        print('Autumn')
    else:
        print('Invalid')

elif (input_month == 'December'):
    if (input_day < 21):
        print('Autumn')
    elif (input_day >= 21) and (input_day < 31):
        print('Winter')
    else:
        print('Invalid')


# Spring Months
elif input_month == 'April' and (input_day < 31):
    print('Spring')
elif input_month == 'May' and (input_day < 32):
    print('Spring')

# Summer Months
elif (input_month == 'July') and (input_day < 32):
    print('Summer')
elif (input_month == 'August') and (input_day < 32):
    print('Summer')

# Autumn Months
elif (input_month == 'October') and (input_day < 32):
    print('Autumn')
elif (input_month == 'November') and (input_day < 31):
    print('Autumn')

# Winter Months
elif (input_month == 'January') and (input_day < 32):
    print('Winter')
elif (input_month == 'February') and (input_day < 28):
    print('Winter')
else:
    print('Invalid')

