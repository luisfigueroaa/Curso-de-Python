def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    print(result)
    return result


raise_to_power(3, 4)
