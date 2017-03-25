# __author__ = 'dell'
# def search(lst, x):
#     for i in range(len(lst)):
#         if lst[i] == x:
#             return i
#
#     return -1
def bi_search(lst, x):
    low = 0
    high = len(lst) - 1
    while low <= high:
        mid = (low + high) / 2
        if lst[mid] == x:
            return mid
        elif lst[mid] > x:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def selection_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst.insert(i, lst.pop(min_index))

lst = [62, 7, 8, 14, 16]
selection_sort(lst)
print lst
# print search(lst, 10)
# print bi_search(lst, 10)
# print search(lst, 1)
# print lst.index(8)

# print [1, 2, 2].index(2)
