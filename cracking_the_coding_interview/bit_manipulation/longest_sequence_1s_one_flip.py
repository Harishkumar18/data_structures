"""
Give an integer n. We can flip exactly one bit. Write code to find the length of the longest sequence of 1 s you could create.

Input : 1775
Output : 8
Binary representation of 1775 is 11011101111.
After flipping the highlighted bit, we get
consecutive 8 bits. 11011111111.

An efficient solution is to walk through the bits in binary representation of given number. We keep track of current
1’s sequence length and the previous 1’s sequence length. When we see a zero, update previous Length:

If the next bit is a 1, previous Length should be set to current Length.
If the next bit is a 0, then we can’t merge these sequences together. So, set previous Length to 0.
We update max length by comparing following two:

Current value of max-length
Current-Length + Previous-Length .
result = return max-length+1 (// add 1 for flip bit count )
"""
#TODO: need to check

from ctypes import sizeof


def flipbit(a):
    if ~a == 0:
        return 8*sizeof()
    currLen, prevLen, maxLen = 0, 0, 0
    while (a > 0):
        print(a)

        # If Current bit is a 1
        # then increment currLen++
        if ((a & 1) == 1):
            currLen += 1;

            # If Current bit is a 0
        # then check next bit of a
        elif ((a & 1) == 0):

            # Update prevLen to 0
            # (if next bit is 0)
            # or currLen (if next
            # bit is 1). */
            prevLen = 0 if ((a & 2) == 0) else currLen;

            # If two consecutively bits
            # are 0 then currLen also
            # will be 0.
            currLen = 0;

            # Update maxLen if required
        maxLen = max(prevLen + currLen, maxLen);

        # Remove last bit (Right shift)
        a >>= 1;

        # We can always have a sequence
        # of at least one 1, this is
        # fliped bit
    return maxLen + 1;

print(flipbit(12))