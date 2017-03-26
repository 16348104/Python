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


def selection_sort_1(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        lst.insert(i, lst.pop(min_index))


def swap(lst, i, j):
    t = lst[i]
    lst[i] = lst[j]
    lst[j] = t


def selection_sort_2(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j
        swap(lst, i, min_index)


def bubble_sort(lst):
    exchanged = True
    top = len(lst) - 1
    while exchanged:
        exchanged = False
        for i in range(top):
            if lst[i] > lst[i + 1]:
                swap(lst, i, i + 1)
                exchanged = True
        top -= 1


lst = [900, 62, 5, 8, 14, 16, 56, 3, 42,-1, 29, 0]
# selection_sort_2(lst)
bubble_sort(lst)
print lst
# print search(lst, 10)
# print bi_search(lst, 10)
# print search(lst, 1)
# print lst.index(8)

# print [1, 2, 2].index(2)
