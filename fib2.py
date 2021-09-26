def findThreeLargestNumbers(array, out_array=[], tries=0):
    if tries == 3:
        return

    current_largest_value = float('-inf')
    current_largest_idx = -1

    for idx, element in enumerate(array):
        if element >= current_largest_value:
            current_largest_value = element
            current_largest_idx = idx

    out_array.append(array.pop(current_largest_idx))
    findThreeLargestNumbers(array, out_array, tries + 1)
    return sorted(out_array)

array = [55,7,8]


print(findThreeLargestNumbers(array))
