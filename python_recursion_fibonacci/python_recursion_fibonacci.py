def fibonacci(number):
    return number if number <= 1 else (fibonacci(number-2)) + (fibonacci(number-1))

for num in range(1, 10):
    print(fibonacci(num))
