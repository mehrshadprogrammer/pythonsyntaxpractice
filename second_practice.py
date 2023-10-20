name = input('enter your name: ')
name = name.lower()
# name = name.strip()
name = name.replace(" ","")
array = []
for char in name:
    if char not in array:
        print(f"{name.count(char)} : {char}")
        array.append(char)

