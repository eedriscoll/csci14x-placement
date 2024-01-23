def nth_prime(n):
    prime_list = [2] #to start list of primes
    num = 3 #start from 3
    while len(prime_list) < n:
        if all(num % i != 0 for i in prime_list): 
            prime_list.append(num) 
        num += 2 
    print(prime_list[-1])
