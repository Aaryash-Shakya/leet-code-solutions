# Brute Force method
'''
def count_primes(n):
    primes = []

    # iterate over each number from 1 to n
    for i in range(1, n + 1):
        # if the number is less than or equal to 1, skip it and dont add it to the primes list
        if i <= 1:
            continue

        # assume the number is prime
        is_prime = True

        # iterate over each number from 2 to half of the number
        for j in range(2, int(i / 2 + 1)):
            # if the number is divisible by any number from 2 to half of the number, it is not prime
            if i % j == 0:
                is_prime = False
                break

        # if the number is prime, add it to the primes list
        if is_prime:
            primes.append(i)
    print(len(primes), ",", primes)
'''

# 

# Examples:
count_primes(10)  # 4
count_primes(0)  # 0
count_primes(1)  # 0
count_primes(20)  # 8
