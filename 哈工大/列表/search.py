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


lst = [6, 7, 8, 10, 16]
# print search(lst, 10)
print bi_search(lst, 10)
# print search(lst, 1)
# print lst.index(8)

# print [1, 2, 2].index(2)
