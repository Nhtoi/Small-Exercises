def BinaryToDecimal(s):
    decimal = []
    index = 0
    for i in range(len(s)-1, -1, -1):
        decimal.append( int(s[i]) * (2**index))
        index += 1
    return (sum(decimal))

print(BinaryToDecimal("100"))

def DecimalToBinary(decimal):
    binary = ""
    def convert(decimal):
        nonlocal binary
        if decimal is None or decimal == 0:
            return
        elif decimal % 2 == 0:
            binary += str(0)
        else:
            binary += str(1)
        decimal = convert(decimal // 2)
    convert(decimal)
    return binary[::-1]

print(DecimalToBinary(4))