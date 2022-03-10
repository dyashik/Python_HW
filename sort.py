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

