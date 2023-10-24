def result_two_list(list1, list2):
    new_list=[]
    for i in list1:
        if i % 2 != 0:
            new_list.append(i)
        else:
            pass

    for i in list2:
        if i % 2 == 0:
            new_list.append(i)
        else:
            pass
    return new_list

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

new_list = result_two_list(list1, list2)
print(new_list)