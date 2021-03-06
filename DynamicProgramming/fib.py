def fib(n, memo = {}):
    if (n in memo):
        return memo[n]
    if (n <= 2):
        return 1
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]


print(fib(6));## 8
print(fib(7));## 13
print(fib(8));## 21
print(fib(10));## 55
print(fib(50));## 12586269025
