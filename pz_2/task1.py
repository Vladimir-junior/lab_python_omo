def prime(n):
    if n <= 1:
        return 0
    primes = []
    for num in range(2, 20 + 1):
        is_prime = True
        for prim in primes:
            if num % prim == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print(primes)
    return primes[2]


def main():
    print(prime(2))

if __name__ == '__main__':
    main()
