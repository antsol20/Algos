class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value

    def __repr__(self):
        return f"weight:{self.weight}, value:{self.value}"


def knapsack(max_weight, items, n):

    if n == 0 or max_weight == 0:
        return 0

    if items[n - 1].weight > max_weight:
        return knapsack(max_weight, items, n-1)

    # return the maximum of two cases:
    # (1) nth item included
    # (2) not included
    else:
        return max(items[n-1].value + knapsack(max_weight-items[n-1].weight, items, n-1), knapsack(max_weight, items, n-1))


if __name__ == '__main__':
    item_list = [Item(10, 60), Item(20, 100), Item(30, 120)]
    max_w = 50
    number_items = len(item_list)
    print(knapsack(max_w, item_list, number_items))

