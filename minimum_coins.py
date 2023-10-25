import time


def min_ignore_none(a: int | None, b: int | None) -> int | None:
    if a is None:
        return b
    if b is None:
        return a
    return min(a, b)


# top down
def top_min_coins(target: int, coins: list[int]) -> int:
    memo = {}  # Initialize memoization dictionary

    def dp(target):
        if target in memo:
            return memo[target]
        if target == 0:
            return 0
        else:
            answer = None
            for coin in coins:
                subproblem = target - coin
                if subproblem < 0:
                    continue
                sub_answer = dp(subproblem)
                if sub_answer is not None:
                    answer = min_ignore_none(answer, sub_answer + 1)
            memo[target] = answer
            return answer

    result = dp(target)
    return result



# bottom up
def bottom_min_coins(target: int, coins: list[int]) -> int:
    memo[0] = 0
    for i in range(1, target + 1):
        for coin in coins:
            subproblem = i - coin
            if subproblem < 0:
                continue
            memo[i] = min_ignore_none(
                memo.get(i),
                memo.get(subproblem) + 1
            )
    return memo[target]


if __name__ == '__main__':
    # time top down approach
    top_start = time.time()
    print(top_min_coins(13, [1, 4, 5]))  # 3
    print(top_min_coins(150, [1, 4, 5]))  # 30
    print(top_min_coins(30, [5, 10, 25]))  # 6 --> not giving the correct answer
    print(top_min_coins(11, [1, 5, 6, 9]))  # 2
    top_end = time.time()

    # reset memo
    memo = {}

    # time bottom up approach
    bottom_start = time.time()
    print(bottom_min_coins(13, [1, 4, 5]))
    print(bottom_min_coins(150, [1, 4, 5]))
    print(bottom_min_coins(30, [5, 10, 25]))
    print(bottom_min_coins(11, [1, 5, 6, 9]))
    bottom_end = time.time()

    # print times
    print(f'Top down time: {top_end - top_start}')
    print(f'Bottom up time: {bottom_end - bottom_start}')