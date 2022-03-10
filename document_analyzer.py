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
    for word in dic.keys():
        if(count == 5):
            break
        list.append(word)
        count += 1
     
    
    for word in list:
        print(word + ": " + str(dic[word]))
    
    # print(dic)
    
problem2("/Users/yashikdhanaraj/Desktop/Projects/SE/Python HW/document.txt")