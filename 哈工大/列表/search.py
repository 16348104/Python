# __author__ = 'dell'
def search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i

    return -1


lst = [10, 6, 7, 8]
print search(lst, 10)
# print search(lst, 1)
print lst.index(8)

print [1, 2, 2].index(2)
