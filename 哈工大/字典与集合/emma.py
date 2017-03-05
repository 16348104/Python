f = open('emma.txt')
word_freq = {}
for line in f:
    words = line.strip().split()
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
# print word_freq
word_freq_list = []
for word, freq in word_freq.items():
    word_freq_list.append((freq, word))

word_freq_list.sort(reverse=True)
# print word_freq_list
for freq,word in word_freq_list[0:10]:
    print word,freq
f.close()
