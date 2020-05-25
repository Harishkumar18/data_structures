"""
Given a singly linked list, determine if it is a palindrome.

Example 1:

Input: 1->2
Output: false
"""
from linked_list.linked_list_implementation import LinkedList


def isPalindrome(head):
    # rev records the first half, need to set the same structure as fast, slow, hence later we have rev.next
    rev = None
    # initially slow and fast are the same, starting from head
    slow = fast = head
    # import pdb;
    # pdb.set_trace()
    while fast and fast.next:
        # fast traverses faster and moves to the end of the list if the length is odd
        fast = fast.next.next

        # take it as a tuple being assigned (rev, rev.next, slow) = (slow, rev, slow.next), hence the re-assignment of slow would not affect rev (rev = slow)
        rev, rev.next, slow = slow, rev, slow.next
    if fast:
        # fast is at the end, move slow one step further for comparison(cross middle one)
        slow = slow.next
    # compare the reversed first half with the second half
    while rev and rev.data == slow.data:
        slow = slow.next
        rev = rev.next

    # if equivalent then rev become None, return True; otherwise return False
    return not rev


if __name__ == '__main__':
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(2)
    ll.insert(1)
    print(f"Linked List")
    res = isPalindrome(ll.head)
    print(res)
