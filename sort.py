def sort_list(list):
    n = len(list)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
            # print("Pass: " + str(list))
            j = j + 1
        i = i + 1
    return list

def problem2():
    file = open("/Users/yashikdhanaraj/Desktop/Projects/SE/Python HW/document.txt")
    file = file.read()
    dic = {}
    split = file.split()
    for word in split:
        count = 0
        for words in split:
            if words == word:
                count += 1
        dic.update({word : count})
        
    dic = {k: v for k, v in sorted(dic.items(), key=lambda item: item[1], reverse = True)}
    # print(dic)
    count = 0
    list = []
    for word in dic.keys():
        if(count == 5):
            break
        list.append(word)
        count += 1
     
    
    for word in list:
        print(word + ": " + str(dic[word]))
    
    # print(dic)
    
def main():
    print("Problem 1: ")
    list = [1, 3, 2, 7]
    print("Before: ", list)
    print("After: ", sort_list(list))
    print()
    list = [3, 2, 4, 89]
    print("Before: ", list)
    print("After: ", sort_list(list))
    print()
    list = [23, 4324, 234, 234, 2]
    print("Before: ", list)
    print("After: ", sort_list(list))
    
    
    print()
    print("Problem 2: ")
    problem2()
    
main()