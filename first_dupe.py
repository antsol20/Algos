def firstDuplicateValue(array):
    seen = set()
    for element in array:
        if element in seen:
            return element
        seen.add(element)
    return -1


array = [2, 1, 5, 3, 3, 2, 4]
print(firstDuplicateValue(array))
