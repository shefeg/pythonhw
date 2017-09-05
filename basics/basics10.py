def char_dic(string):
    dic = {}
    for i in string:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    print dic


char_dic("abbabcbdbabdbdbabababcbcbab")
