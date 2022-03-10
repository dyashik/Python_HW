
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

def problem2(fileName):
    if  "." not in fileName:
        return
    file = open(fileName, "r")
    file = file.read()
    dic = {}
    split = file.split()
    # print(split)
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
    numbers = []
    for word in dic.keys():
        if(count == 5):
            break
        list.append(word)
        numbers.append(dic[word])
        count += 1
    
    if list.__len__() == 0:
        return
    
    print("\r")
    
    def sort_list(list, list2):
        n = len(list)
        i = 0
        while i < n:
            j = 0
            while j < n - i - 1:
                if list[j] == list[j + 1]:
                    if list2[j] > list2[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
                        list2[j], list2[j + 1] = list2[j + 1], list2[j]
                elif list[j] < list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
                    list2[j], list2[j + 1] = list2[j + 1], list2[j]
                # print("Pass: " + str(list))
                j = j + 1
            i = i + 1
        return list
    
    sort_list(numbers, list)
    
    
    for word in list:
        print(word + ": " + str(dic[word]))
    
    # print(dic)
    


problem2("/Users/yashikdhanaraj/Desktop/Projects/SE/Python HW/document.txt")