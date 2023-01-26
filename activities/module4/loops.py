
def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
summ = 0
evens = list()
primes = list()
for x in range(1, num+1):
    summ += x
    if x % 2 == 0:
        evens.append(x)
    if is_prime(x):
        primes.append(x)
else:
    print("Sum:", summ)
    print("Evens:", evens)
    print("Primes:", primes)
