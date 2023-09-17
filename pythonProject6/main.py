user_total = []


def exact_change(user_total):
    '''Computes the least amount of coins with exact change given by user input'''

    input_val = user_total
    num_dollars = (input_val // 100)
    num_quarters = (input_val - (num_dollars * 100)) // 25
    num_dimes = (input_val - (num_dollars * 100) - (num_quarters * 25)) // 10
    num_nickels = (input_val - (num_dollars * 100) - (num_quarters * 25) - (num_dimes * 10)) // 5
    num_pennies = (input_val - (num_dollars * 100) - (num_quarters * 25) - (num_dimes * 10) - (num_nickels * 5)) // 1

    # return statement
    return num_dollars, num_quarters, num_dimes, num_nickels, num_pennies


# call function
if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    if input_val <= 0:
        print('no change')

    # Dollars
    if (input_val >= 100):
        if num_dollars == 1:
            print(num_dollars, 'dollar')
        elif num_dollars >= 2:
            print(num_dollars, 'dollars')

    # quarters
    if input_val >= 25:
        if num_quarters == 1:
            print(num_quarters, 'quarter')
        elif num_quarters >= 2:
            print(num_quarters, 'quarters')

    # dimes
    if input_val >= 10:
        if num_dimes == 1:
            print(num_dimes, 'dime')
        elif num_dimes >= 2:
            print(num_dimes, 'dimes')

    # nickels
    if input_val >= 5:
        if num_nickels == 1:
            print(num_nickels, 'nickel')
        elif num_nickels >= 2:
            print(num_nickels, 'nickels')

    # pennies
    if input_val >= 1:
        if num_pennies == 1:
            print(num_pennies, 'penny')
        elif num_pennies >= 2:
            print(num_pennies, 'pennies')