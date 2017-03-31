def making_change(value):
    """
    Evaluates how a given amount of money can be made with the fewest number of Canadian coins.
    Args:
        value(:float): The amount of money we want change for.
    Returns:
        change(:dictionary): The number of each coin which results in the fewest number of total coins being used to equal the value.
    """
    Canadian_coins = (100, 25, 10, 5, 1)
    change = {1.00:0, 0.25:0, 0.1:0, 0.05:0, 0.01:0}
    value *= 100
    while value != 0:
        for coin in Canadian_coins:
            if value - coin >= 0:
                change[coin/100] += 1
                value -= coin
                print(value)
                break
    return change

print(making_change(2.35))
