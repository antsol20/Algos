test = {
    "intervals": [
        [9, 10],
        [1, 2],
        [3, 5],
        [4, 7],
        [6, 8],
    ]
}
intervals = test['intervals']

# work in progress


def mergeOverlappingIntervals(intervals):
    intervals.sort()
    print(intervals)

# for i in range(len(intervals)):
    #     base_pair = intervals[i]
    #     for j in range(len(intervals)):
    #         if j == i:
    #             continue
    #         compare_pair = intervals[j]
    #         if base_pair[1] > compare_pair[0]:
    #             print(base_pair, compare_pair)


mergeOverlappingIntervals(intervals)
