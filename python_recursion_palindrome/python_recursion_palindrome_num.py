def reverse_number(number):
    return number if number < 10 else int(str(number % 10) + str(reverse_number(number // 10)))

for num in range(1, 100):
    if num == reverse_number(num):
        print(num)