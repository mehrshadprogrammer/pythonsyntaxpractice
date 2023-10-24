import sys

def sum_with_previos_number(num):
    for i in range(num):
        if i == 0:
            print(f"current number:{i} sum previos number :{0} equal :{i + 0}")
        else:
            print(f"currect number:{i} sum previos number {i-1} equal :{i + (i-1)}")

sum_with_previos_number(9)


