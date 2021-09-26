def findThreeLargestNumbers(in_array, out_array=[], currentlargest=float('-inf'), currentmax=float('inf'), tries=0):
    if tries == 3:
        return out_array

    for item in in_array:
        if currentlargest < item <= currentmax:
            currentlargest = item

        elif item == currentlargest:
            currentlargest = item

    out_array.append(currentlargest)
    return findThreeLargestNumbers(in_array, out_array, float('-inf'), currentlargest, tries + 1)


#array = [141, 1, 17, -7, -17, -27, 18, 541, 8, 7, 7]
array = [-141, 8, 7, 7]
print(findThreeLargestNumbers(array))





