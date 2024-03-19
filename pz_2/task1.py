def prime(n: int) -> int:
    if n <= 1:
        return 0

    prime_numbers = []
    for num in range(2, 100 + 1):
        flag = True
        for el in prime_numbers:
            if num % el == 0:
                flag = False
                break
        if flag:
            prime_numbers.append(num)

    print(prime_numbers)
    return prime_numbers[n]


def main():
    print(prime(7))

if __name__ == '__main__':
    main()
