def with_for() -> None:
    s = 'ABC'
    for char in s:
        print(char)

def without_for() -> None:
    s = 'ABC'
    it = iter(s)
    
    while True:
        try:
            char = next(it)
            print(char)
        except StopIteration:
            del it # iterator 폐기
            break

if __name__ == '__main__':
    # with_for()
    without_for()
