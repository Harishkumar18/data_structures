def DecimalToBinary(num):
    res = ''
    if num > 1:
        DecimalToBinary(num // 2)
    print("res her", res)
    res = res+ str(num % 2)
    return int(res)


def bitwiseComplement(N):
    X = 1
    while N > X:
        X = X * 2 + 1
    print("x value", X)
    print("n value", N)
    return X - N


# Driver Code
if __name__ == '__main__':
    # decimal value
    dec_val = 10

    # Calling function
    answer = bitwiseComplement(dec_val)
    print(answer)
