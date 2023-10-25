import time
from collections import defaultdict


def how_many_ways_coins(target: int, coins: list[int]) -> int:
    memo = defaultdict(lambda _: 0)

    memo[0] = 1
    for i in range(1, target + 1):
        memo[i] = 0
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] += memo[subproblem]
    return memo[target]

if __name__ == '__main__':
    start = time.time()
    print(how_many_ways_coins(5, [1, 4, 5]))
    print(how_many_ways_coins(87, [1, 4, 5, 8]))
    end = time.time()
    print(f'Runtime: {end - start}')