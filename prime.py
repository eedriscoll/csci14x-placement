def nth_prime(n):
    prime_list = [2]
    # to start list of primes
    num = 3
    if n <= 0:
        raise ValueError("try again")
    while len(prime_list) < n:
        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]