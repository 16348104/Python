words = ['dfafj', 'ajgjg', 'ghgha']

lst = []
for w in words:
    lst.append((len(w), w))
lst.sort(reverse=True)
res = []
for length, word in lst:
        res.append(word)

print res

