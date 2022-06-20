def palindrom(number, string_result = ''):
    if number < 1:
        return string_result
    else:
        if str(number) == str(number)[::-1]:
            string_result += (str(number)+" ")
        return palindrom(number-1, string_result)

palindrom_num = palindrom(100)

print(palindrom_num)