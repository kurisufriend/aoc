f = open("input", "r").read().split("\n\n")

cols = list(map(lambda c: c.replace("    ", ".").replace(" ", "").replace("[", "").replace("]", ""), f[0].split("\n")))

n = int(cols[-1][-1])
cols = cols[:n]
cols.reverse()

stacks = []
for i in range(n): stacks.append([])
for c in cols:
    for idx, l in enumerate(c):
        if not(l == "."):
            stacks[idx].append(l)

instructions  = f[1].split("\n")

print(stacks)
print(instructions)

for ins in instructions:
    if ins == "": continue
    amt = int(ins.split("move ")[1].split(" from")[0])
    fr = int(ins.split("move ")[1].split(" from")[1].split(" to ")[0])
    to = int(ins.split("move ")[1].split(" from")[1].split(" to ")[1])
    #for i in range(amt):# p1
    #    crate = stacks[fr-1].pop(-1)
    #    stacks[to-1].append(crate)
    crates = stacks[fr-1][-1*amt:]
    for i in range(amt): stacks[fr-1].pop(-1)
    stacks[to-1].extend(crates)
    print(stacks)
print("".join([i[-1] for i in stacks]))
