stored_pass = "12345"

def enter_pass():
    return input("enter your password : ")

spassword = enter_pass()
boolean = True

while boolean:
    if stored_pass == spassword:
        print("success")
        boolean = False
        break
    else:
        while stored_pass != spassword:
            print("unsuccess!!!")
            print("try again")
            spassword = enter_pass()
    

