from random import randint


def d6():
    return randint(1, 6)

if __name__ == '__main__':
    """
    Using iter with a Callable
    """
    d6_iter = iter(d6, 1)   # 1 이 나오면 iter 종료

    for roll in d6_iter:
        print(roll)
