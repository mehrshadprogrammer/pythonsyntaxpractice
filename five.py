def checked_odd_or_even_numeric(number):
    if number % 2 == 0:
        print("this is even number")
    elif number % 2 != 0:
        print("this is odd number ")
    else:
        pass

number = input("enter your number: ")
number = int(number)

checked_odd_or_even_numeric(number)