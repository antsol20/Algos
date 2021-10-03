def arrayOfProducts(array):
    ret_array = []
    for outer_idx, outer_element in enumerate(array):
        prod = 1
        for inner_idx, inner_element in enumerate(array):
            if inner_idx != outer_idx:
                prod = inner_element * prod

        ret_array.append(prod)
    return ret_array


array = [5, 1, 4, 2]
print(arrayOfProducts(array))
