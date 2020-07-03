"""
Given any integer, print an English phrase that describes the integer (e.g., "One Thousand,
Two Hundred Thirty Four").

#TODO: need to complete
"""


def convert_to_words(num):
    # Get number of digits
    # in given number
    l = len(num)

    # Base cases
    if l == 0:
        print("empty string")
        return

    if l > 4:
        print("Length more than 4 is not supported")
        return

        # The first string is not used,
    # it is to make array indexing simple
    single_digits = ["zero", "one", "two", "three",
                     "four", "five", "six", "seven",
                     "eight", "nine"]

    # The first string is not used,
    # it is to make array indexing simple
    two_digits = ["", "ten", "eleven", "twelve",
                  "thirteen", "fourteen", "fifteen",
                  "sixteen", "seventeen", "eighteen",
                  "nineteen"]

    # The first two string are not used,
    # they are to make array indexing simple
    tens_multiple = ["", "", "twenty", "thirty", "forty",
                     "fifty", "sixty", "seventy", "eighty",
                     "ninety"]

    tens_power = ["hundred", "thousand"]

    # Used for debugging purpose only
    print(num, ":", end=" ")
    if l ==1:
        print(single_digits[ord(num[0])-48])
        return





# Driver Code
convert_to_words("0")
# convert_to_words("9923")
# convert_to_words("523")
# convert_to_words("89")
# convert_to_words("8989")