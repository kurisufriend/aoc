f = open("input", "r").read().split("\n")

elves = []
total = 0
for cal in f:
    if cal == '':
        elves.append(total)
        total = 0
        continue
    total += int(cal)
a = elves
a.sort()
print(a[-1])
print(a[-1]+a[-2]+a[-3])
