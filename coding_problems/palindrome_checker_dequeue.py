from Practice.double_ended_queue import Deque


def palindrome_checker(inp_string):
    queue = Deque()
    for entity in inp_string:
        queue.addFront(entity)
    palindrome = True
    while queue.size() >1 and palindrome:
        first_elem = queue.removeFront()
        last_elem = queue.removeRear()
        if first_elem!=last_elem:
            palindrome = False
            break
    return palindrome


print(palindrome_checker("lsdkjfskf"))
# print(palindrome_checker("radar"))