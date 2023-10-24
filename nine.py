# def remove_char(str, num):
#     for char in str[num::1]:
#         print(char)
# remove_char("mehrshad", 3)
def remove_char(str, num):
    new_str = str[num:]
    return new_str

print(remove_char("merhahd", 4))