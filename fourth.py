
def checked_count_lower_and_uppercase_charechter(str):
    upp = 0
    low = 0
    for ch in str:
        if ch.islower():
            low += 1
        elif ch.isupper():
            upp += 1
        else:
            pass
    print(f"upper charechter :{upp} and lower charechter : {low}")

boolean = True
while boolean:
    name = input("enter your name : ")
    if name.isnumeric():
        print("name is just charecter")
    else:
        checked_count_lower_and_uppercase_charechter(name)
