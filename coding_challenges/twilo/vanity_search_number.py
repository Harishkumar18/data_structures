

#
# Complete the 'vanity' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY codes
#  2. STRING_ARRAY numbers
#

def vanity(codes, numbers):
    # Write your code here
    mapping = {"A": 2, "B":2, "C":2,"D":3,"E":3, "F":3, "G":4, "H":4, "I":4, "J":5,"K":5, "L":5, "M":6,"N":6, "O":6, "P":7,"Q":7, "R":7, "S":7, "T":8,"U":8,"V":8, "W":9, "X":9, "Y":9, "Z":9}
    vanity_nos = []
    for each in codes:
        res = ""
        for i in each:
            res+=str(mapping[i])
        match = [element for element in numbers if res in element]
        vanity_nos.extend(match)
    return vanity_nos

if __name__ == '__main__':
    vanity()