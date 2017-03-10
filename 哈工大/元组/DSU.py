words = ['dfafj', 'ajgjg', 'ghgha','tu']
#decorate
lst = []
for w in words:
    lst.append((len(w), w))
#sort
lst.sort(reverse=True)
res = []
#undecorate
for length, word in lst:
        res.append(word)

print res

