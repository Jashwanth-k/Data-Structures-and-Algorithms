
# factors until n, for every 1 <= i <= n
n = 10**6
factors = [[] for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        factors[j].append(i)

# no of factors for n
allFactors = []
for i in range(1, int(n ** 0.5) + 1):
    if n % i != 0:
        continue
    allFactors.append(i)
    if n // i != i:
        allFactors.append(n // i)

# no.of primes until n using sieve
sieve = [False] * (n+1)
allPrimes = []
for i in range(2, n + 1):
    if sieve[i]:
        continue
    for j in range(i, n + 1, i):
        sieve[j] = True
    allPrimes.append(i)
    # print(i, end=" ")

