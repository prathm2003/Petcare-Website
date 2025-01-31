from math import gcd
from itertools import combinations

def generate_primes(limit):
    """Generate a list of primes up to 'limit' using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [x for x in range(2, limit + 1) if is_prime[x]]

def solve():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])  # Number of test cases
    queries = []
    idx = 1
    for _ in range(T):
        N, K = map(int, data[idx:idx + 2])
        queries.append((N, K))
        idx += 2
    
    # Precompute primes up to 2 * 10^6
    primes = generate_primes(2000000)
    
    results = []
    for N, K in queries:
        max_pairs = N * (N - 1) // 2
        if K > max_pairs:
            results.append("-1")
            continue
        
        # Start with first N primes
        array = primes[:N]
        current_pairs = max_pairs
        
        # Reduce the co-prime pairs to K
        for i in range(N - 1, -1, -1):
            if current_pairs == K:
                break
            array[i] = 2  # Replace with a non-prime to reduce co-prime pairs
            current_pairs -= (i)  # Removing co-prime pairs with all prior elements
        
        results.append(" ".join(map(str, array)))
    
    sys.stdout.write("\n".join(results) + "\n")

