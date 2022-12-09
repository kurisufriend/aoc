from functools import reduce
grid = [[[j, False, []] for j in list(i)] for i in open("input", "r").read().split("\n")]
grid = [i for i in grid if i != []]
def disp(grid):
    for row in grid:
        if row == []: continue
        for tree in row:
            height = int(tree[0])
            print(str(height)+("t" if tree[1] else "f")+str(reduce(lambda a, b: a*b, tree[2]) if tree[2] != [] else [])+str(tree[2]), "", end="")
        print()
    print()
def line(row, order = True):
    highest_yet = -1337
    for idx in range(len(row)) if order else range(len(row)-1, 0, -1):
        tree = row[idx]
        height = int(tree[0])
        if height > highest_yet: tree[1] = tree[1] or True
        
        last_blocker = 0 if order else len(row)-1
        for jdx in range(len(row)) if order else range(len(row)-1, 0, -1):
            tree2 = row[jdx]
            hejght = int(tree2[0])
            if order and (jdx >= idx): break
            if not(order) and (jdx <= idx): break
            if hejght >= height:
                last_blocker = jdx
        tree[2].append(0 if (idx == 0 or idx == len(row)-1) else abs(idx - last_blocker))
        print(tree, idx, last_blocker, highest_yet, row, order)#;input()

        if height > highest_yet: 
            highest_yet = height

disp(grid)
for row in grid:
    if row == []: continue

    line(row)
    print()
    line(row, False)
    print("\n")
disp(grid)
t = []
for col in range(len(grid[0])):
    colacc = []
    for row in range(len(grid)):
        colacc.append(grid[row][col])
    t.append(colacc)
grid = t
for col in grid:
    if col == []: continue

    line(col)
    print()
    line(col, False)
    print("\n")
t = []
for row in range(len(grid)):
    rowacc = []
    for col in range(len(grid[0])):
        rowacc.append(grid[col][row])
    t.append(rowacc)
grid = t
disp(grid)

total = 0
for r in grid:
    for t in r:
        if t[1]: total += 1

alex_best_from_fuck_quest = 0
for r in grid:
    for t in r:
        if reduce(lambda a, b: a*b, t[2]) > alex_best_from_fuck_quest:
            alex_best_from_fuck_quest = reduce(lambda a, b: a*b, t[2])

print(grid)
print(total)
print(alex_best_from_fuck_quest)
