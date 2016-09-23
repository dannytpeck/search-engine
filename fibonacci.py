def fibonacci_with_cache(cache, n):
    if n not in cache:
        if n == 1 or n == 2:
            cache[n] = 1
        else:
            cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return cache[n]

def fibonacci(n):
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacci_iterative(n):
    results = [0, 1]
    i = 2
    while i <= n:
        results.append(results[i - 1] + results[i - 2])
        i += 1
    return results[n]

def fibonacci_iterative_alt(n):
    current = 0
    after = 1
    for i in range(0, n):
        current, after = after, current + after
    return current


if __name__ == "__main__":
    print fibonacci_iterative(250)
