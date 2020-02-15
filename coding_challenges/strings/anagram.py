def is_anagram(s, t):
    dic = {}
    for i in s:
        if i not in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    for i in t:
        if i not in dic:
            return False
        else:
            dic[i] -= 1
    print(dic)
    for each in dic.values():
        if each!=0:
            return False
    return True

if __name__ == '__main__':
    s = 'anagram'
    t = "nagaram"
    # s = "aaa"
    # t = "a"
    res = is_anagram(s, t)
    print(res)
