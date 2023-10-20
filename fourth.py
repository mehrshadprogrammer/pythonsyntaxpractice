
def checked_count_lower_and_uppercase_charechter(str):
    upper = 0
    lower = 0
    for ch in str:
        if ch.islower():
            lower += 1
        elif ch.isupper():
            upper += 1
        else:
            pass
    print(f"upper charechter :{upper} and lower charechter : {lower}")

boolean = True
while boolean:
    name = input("enter your name : ")
    if name.isnumeric():
        print("name is just charecter")
    else:
        checked_count_lower_and_uppercase_charechter(name)
