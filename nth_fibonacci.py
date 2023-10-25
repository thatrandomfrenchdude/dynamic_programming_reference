import time

memo: dict[int, int] = {}


# top down
def top_nth_fibonacci(n: int) -> int:
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = top_nth_fibonacci(n - 1) + top_nth_fibonacci(n - 2)
    return memo[n]


# bottom up
def bottom_nth_fibonacci(n: int) -> int:
    if n <= 2:
        return 1
    memo[1] = 1
    memo[2] = 1
    for i in range(3, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


if __name__ == '__main__':
    # time top down approach
    top_start = time.time()
    print(top_nth_fibonacci(5))
    print(top_nth_fibonacci(10))
    print(top_nth_fibonacci(50))
    top_end = time.time()

    # reset memo
    memo = {}

    # time bottom up approach
    bottom_start = time.time()
    print(bottom_nth_fibonacci(5))
    print(bottom_nth_fibonacci(10))
    print(bottom_nth_fibonacci(50))
    bottom_end = time.time()

    # print times
    print(f'Top down time: {top_end - top_start}')
    print(f'Bottom up time: {bottom_end - bottom_start}')