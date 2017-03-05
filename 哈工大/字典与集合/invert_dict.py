d1 = {'zhang': 123, 'wang': 456, 'li': 123, 'zhao': 456, 'deng': 999, 'YU': 78}
d2 = {}
for name, room in d1.items():
    if room in d2:
        d2[room].append(name)
    else:
        d2[room] = [name]
print d2
