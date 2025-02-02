import timeit

# Жадный алгоритм (Greedy)


def find_coins_greedy(amount, coins=[50, 25, 10, 5, 2, 1]):
    change = {}
    for coin in coins:
        if amount >= coin:
            count = amount // coin
            change[coin] = count
            amount -= count * coin
    return change

# Алгоритм динамического программирования (DP)


def find_min_coins(amount, coins=[50, 25, 10, 5, 2, 1]):
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    coin_used = [-1] * (amount + 1)

    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                coin_used[i] = coin

    if dp[amount] == float('inf'):
        return {}  # Невозможно выдать сумму

    result = {}
    while amount > 0:
        coin = coin_used[amount]
        if coin in result:
            result[coin] += 1
        else:
            result[coin] = 1
        amount -= coin

    return result

# Функция для измерения времени выполнения


def measure_time(func, amount):
    return timeit.timeit(lambda: func(amount), number=1000)


# Тестирование алгоритмов
test_amount = 113
print("Greedy Algorithm:", find_coins_greedy(test_amount))
print("Dynamic Programming Algorithm:", find_min_coins(test_amount))

# Измерение времени выполнения
greedy_time = measure_time(find_coins_greedy, test_amount)
dp_time = measure_time(find_min_coins, test_amount)

print(f"Execution time (Greedy): {greedy_time:.6f} sec")
print(f"Execution time (DP): {dp_time:.6f} sec")
