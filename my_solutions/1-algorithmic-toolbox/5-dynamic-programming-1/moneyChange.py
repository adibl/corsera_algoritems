change = int(input())
coins = [1, 3, 4]
num_of_coins = [0, 1, 2, 1, 1]
while change >= len(num_of_coins):
    options = []
    for coin in coins:
        options.append(num_of_coins[-1 * coin] + 1)
    num_of_coins.append(min(*options))
print(num_of_coins[change])

