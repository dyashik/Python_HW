def sort_list(list):
    n = len(list)
    i = 0
    while i < n:
        j = 0
        while j < n - 1:
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            # print("Pass: " + str(list))
            j = j + 1
        i = i + 1
    return list


print("Problem 1: ")
list = [1, 3, 2, 7]
print("Before: ", list)
print("After: ", sort_list(list))
print()

list = [3, 2, 4, 89]
print("Before: ", list)
print("After: ", sort_list(list))
print()

list = [24, 234, 234, 2, 23, 4324]
print("Before: ", list)
print("After: ", sort_list(list))
