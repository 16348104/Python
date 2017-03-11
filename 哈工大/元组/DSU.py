words = ['dfafj', 'ajgjg', 'ghghaf', 'tu']
# #decorate
# lst = []
# for w in words:
#     lst.append((len(w), w))
# #sort
# lst.sort(reverse=True)
# res = []
# #undecorate
# for length, word in lst:
#         res.append(word)
#
# print res
words.sort(key=lambda x: len(x), reverse=True)
print words
