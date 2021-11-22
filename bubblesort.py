def isSorted(array):
    for idx, element in enumerate(array):
        if idx == 0:
            continue
        if array[idx - 1] > array[idx]:
            return False

    return True

def bubblesort(array):
    while not (isSorted(array)):
        for idx, element in enumerate(array):
            if idx >= len(array) - 1:
                continue
            if array[idx + 1] < array[idx]:
                lower = array[idx + 1]
                higher = array[idx]
                array[idx] = lower
                array[idx + 1] = higher


        return bubblesort(array)

    return array


array = [8, 5, 2, 9, 5, 6, 3]
print(bubblesort(array))
