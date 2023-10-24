def checked_first_and_last_char_equal(str):
    if str[0] == str[-1]:
        return True
    else:
        return False

x = [10, 50, 6, 10, 3]
print(checked_first_and_last_char_equal(x))