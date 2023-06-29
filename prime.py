def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True
def print_first_n_primes(n):
    num = 2
    count = 0
    while count < n:
        if is_prime(num):
            print(num)
            count += 1
        num += 1
print_first_n_primes(10)
