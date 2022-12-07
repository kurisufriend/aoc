f = open("input", "r").read().split("\n")
total = 0
for pair in f:
    if pair == "": continue
    t = [[int(j) for j in i.split("-")] for i in pair.split(",")]
    #if (t[1][0] >= t[0][0] and t[1][1] <= t[0][1]) or (t[0][0] >= t[1][0] and t[0][1] <= t[1][1]):
    if ((t[0][0] <= t[1][1]) and (t[0][0] >= t[1][0])) or ((t[1][0] <= t[0][1]) and (t[1][0] >= t[0][0])):
        total += 1
print(total)
