
def change_and_revers_str(num):
    str_num = str(num)
    return str_num[::-1]

def checked_palindrom(num):
  new_num = change_and_revers_str(num)
  if int(new_num) == num:
     print("this number is palindrom")
  else:
     print("this number is not palindrom")


checked_palindrom(122221)