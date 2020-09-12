def fibonacci(n):
    previous = 0
    current = 1
    for i in range(n-1):
        old = current
        current =  previous + current 
        previous = old
    return current

print(fibonacci(10))
print(fibonacci(3))        