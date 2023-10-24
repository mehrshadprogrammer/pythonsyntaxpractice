def multi_or_sum_function(num1, num2):
    if num1 * num2 >= 1000:
        return num1 + num2
    elif num1 * num2 < 1000:
        return num1 * num2
    else:
        pass
print(multi_or_sum_function(30, 20))