def square_of_sum(L):
    sum = 0
    for num in L:
        sum = sum + num * num
    return sum
print square_of_sum([1, 2, 3, 4, 5])
