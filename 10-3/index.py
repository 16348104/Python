# def toUppers(L):
#     return [x.upper() for x in L if isinstance(x, str)]
#
#
# print toUppers(['Hello', 'world', 101])

L = ['Hello', 'world', 10]
for y in L:
    if isinstance(y, str):
        L.append(y.upper())
print L