def isPalindrome(word, low, high):
    while low < high:
        if word[low] != word[high]:
            return False
        low += 1
        high -= 1
    return True


def palindrome_check(complete_word, part_word, start, n, string):
    if start >= n:
        x = part_word.copy()
        complete_word.append(x)
        return

    for i in range(start, n):
        if isPalindrome(string, start, i):
            part_word.append(string[start:i + 1])
            palindrome_check(complete_word, part_word, i + 1, n, string)
            part_word.pop()


def palindrome_partitions(string):
    n = len(string)
    complete_word = []
    part_word = []
    palindrome_check(complete_word, part_word, 0, n, string)
    complete_res = []
    for i in range(len(complete_word)):
        curr_res = []
        for j in range(len(complete_word[i])):
            curr_res.append(complete_word[i][j])
            complete_res.append(curr_res)

    for each in complete_res:
        if len(each) == 3:
            return each
    return list(complete_res)


# Driver Code
if __name__ == "__main__":
    string = "nitin"
    print(palindrome_partitions(string))
