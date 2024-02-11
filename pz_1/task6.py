from random import randint

def get_random_tuple(n: int) -> tuple:
    return tuple(randint(1,100) for _ in range(n))

def main():
    l = get_random_tuple(10)
    print(l)
    print(max(l))
    print(min(l))


if __name__ == '__main__':
    main()


