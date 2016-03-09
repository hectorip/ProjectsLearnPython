def losslessDataCompression(inputString, width):
    resulting = inputString[0]
    skip = 0
    for i in range(1, len(inputString)):
        if skip == 0:
            current = inputString[i]
            beforeIndex = (i - width)
            if beforeIndex < 0: 
                beforeIndex = 0
            subBefore = inputString[beforeIndex:i]
            subAfter = inputString[i:]

            length = 0
            startIndex = 0
            for j in range(len(subBefore)):
                currSB = subBefore[j:]
                currLen = 0
                min_len = min(len(currSB), len(subAfter))
                for k in range(min_len):
                    if subBefore[k] == subAfter[k]:
                        currLen = currLen + 1
                    else:
                        break
                if currLen > length:
                    length = currLen
                    startIndex = beforeIndex + j
            if length > 0:
                resulting += "(" + str(startIndex) +","+ str(length) + ")"
                skip = length - 1
            else:
                resulting += inputString[i]
        else:
            skip = skip - 1
    return resulting

print(losslessDataCompression("abacabadabacaba", 7))