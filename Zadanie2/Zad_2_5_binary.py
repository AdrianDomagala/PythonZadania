def longestBinaryBreak(n):
    longest = temp = 0
    num = bin(n)[2:]
    for s in num:
        if (s == '1'):
            if(temp > longest):
                longest = temp
            temp = 0
        else:
            temp += 1
    return longest

print(longestBinaryBreak(1065985))