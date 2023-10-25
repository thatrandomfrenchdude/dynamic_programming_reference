import time


def how_many_paths_maze() -> int:
    pass

if __name__ == '__main__':
    # time bottom up approach
    start = time.time()
    print(how_many_paths_maze())
    print(how_many_paths_maze())
    print(how_many_paths_maze())
    end = time.time()

    # print times
    print(f'Top down time: {end - start}')