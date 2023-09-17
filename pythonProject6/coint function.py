def exact_change(user_total):
    num_dollars = (input_val // 100)
    num_quarters = (input_val - (num_dollars*100)) // 25
    num_dimes = (input_val - (num_dollars*100) - (num_quarters*25)) // 10
    num_nickels = (input_val - (num_dollars*100) - (num_quarters*25) - (num_dimes*10)) // 5
    num_pennies = (input_val - (num_dollars * 100) - (num_quarters * 25) - (num_dimes * 10) - (num_nickels * 5)) // 1

    user_total = [num_dollars, num_quarters, num_dimes, num_nickels, num_pennies]
    return user_total

if __name__ == '__main__':
    input_val = int(input())
    num_dollars, num_quarters, num_dimes, num_nickels, num_pennies = exact_change(input_val)

    exact_change(user_total)
