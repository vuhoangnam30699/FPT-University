def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input('n: '))
        
if n < 0:
    print("N/A")
        
primes = []
for i in range(1, n + 1):
    if isPrime(i):
        primes.append(str(i))
        
print("; ".join(primes))
        