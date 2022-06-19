list_data = [1,2,3,4,5,6,7,8,9,10]

def sum_list(list):
    return list[0] if len(list) == 1 else list[0] + sum_list(list[1:])

print(sum_list(list_data))