def moveElementToEnd(array, toMove):
    for j in range(array.count(toMove)):
        for k in range(0, len(array)):
            if array[k] == toMove:
                for i in range(k, len(array) - 1):
                    pop_up = array[i]
                    array[i] = array[i + 1]
                    array[i + 1] = pop_up
    return moveElementToEnd


array = [5, 1, 2, 5, 5, 3, 4, 6, 7, 5, 8, 9, 10, 11, 5, 5, 12]
toMove = 5

moveElementToEnd(array, toMove)

print(array)
