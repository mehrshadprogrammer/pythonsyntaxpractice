def checked_password(str):
    if len(str) < 4:
        print("your password is not currct your password must more 4 charechter")
    elif len(str) > 8:
        print("your password is not currect your pass should less 8 charchter")
    elif str.isalpha():
        print("your password is not currect there is not your password number")
    else:
        print("yes that it")


password = input("enter your password : ")


checked_password(password)