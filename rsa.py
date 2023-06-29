import sys
import math

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def factorize_rsa(number):
    if is_prime(number):
        return str(number) + "=" + str(number)
    
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            if is_prime(i) and is_prime(number // i):
                return f"{number}={i}*{number // i}"
    
    return f"Unable to factorize {number} into two prime factors."

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: rsa <file>")
    else:
        file_path = sys.argv[1]
        with open(file_path, 'r') as file:
            number = int(file.readline().strip())
            factorization = factorize_rsa(number)
            print(factorization)

