import sys

def factorize(n):
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def factorize_numbers(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            number = int(line.strip())
            factors = factorize(number)
            factor_str = '*'.join(str(f) for f in factors)
            print(f"{number}={factor_str}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: factors <file>")
    else:
        file_path = sys.argv[1]
        factorize_numbers(file_path)

