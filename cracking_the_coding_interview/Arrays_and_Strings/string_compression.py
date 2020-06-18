"""
1.6 String Compression:
Implement a method to perform basic string compression using the counts
of repeated characters. For example, the string aabcccccaaa would become a2b1c5a3. If the
"compressed" string would not become smaller than the original string, your method should return
the original string. You can assume the string has only uppercase and lowercase letters (a - z).
"""


def string_compression(s):
    n = len(s)
    if n == 0:
        return s
    res = [s[0]]
    count = 0
    for i in range(1, n):
        if s[i - 1] == s[i]:
            count += 1
        else:
            res.append(str(count))
            res.append(s[i])
            count = 1
    res.append(str(count))
    res = "".join(res)

    if len(res) > n:
        return s
    return res


print(string_compression("aaabbccccc"))

print(string_compression(""))

print(string_compression("a"))
