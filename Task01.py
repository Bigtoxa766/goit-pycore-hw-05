

def caching_fibonacci():
    cache = {}

    def fibonacci(n) -> int:
        cache[n] = n

        if n < 2:
            return n
        
        if n in cache:
            cache[n] = fibonacci(n - 1) + fibonacci(n -2)
            return cache[n]
            
    return fibonacci

fib = caching_fibonacci()
print(fib(10))
print(fib(15))