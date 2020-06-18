def strStr(source, target):
    if source is None or target is None:
        return -1
    for i in range(len(source) - len(target) + 1):
        for j in range(len(target)):
            print(source[i+j], target[j])
            if source[i + j] != target[j]:
                break
        else: # no break
            return i
    return -1


print(strStr("harish", "ris"))