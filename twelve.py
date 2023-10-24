def count_substring_from_string(str1, str2):
    count = 0
    new_str = str1.split(" ")
    for str in new_str:
        if str == str2:
            count += 1
    print(str2, count) 

count_substring_from_string("mehrshad jan amdii mehrshad", "mehrshad")