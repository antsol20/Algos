def isMonotonic(array):
    if len(array) < 2:
        return True

    counter = 0
    while (array[counter + 1] == array[counter]):
        if counter == len(array) - 2:
            break
        counter += 1

    if array[counter + 1] > array[counter + 0]:
        for j in range(len(array) - 1):
            if array[j + 1] < array[j]:
                return False

    elif array[counter + 1] < array[counter + 0]:
        for j in range(len(array) - 1):
            if array[j + 1] > array[j]:
                return False

    return True


array = [-1, -1, -1, -1, -1, -1, -1, -1]
print(isMonotonic(array))
