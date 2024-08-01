example = 'This is an example!'
old = example.split()
new = len(old)
blank = []
for i in old:
    blank.append(i[::-1])

print(type(" ".join(blank)))
