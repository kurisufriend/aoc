f = [i.split(" ") for i in open("input", "r").read().strip().split("\n")]
k = {"L": [-1, 0], "R": [1, 0], "U": [0, 1], "D": [0, -1]}
visited = {}
rope = []
n = 10
for i in range(n):
    rope.append([0,0])
for instruction in f:
    direc = instruction[0]
    ct = int(instruction[1])
    for i in range(ct):
        h = rope[0]
        h = [h[0]+k[direc][0], h[1]+k[direc][1]]
        rope[0] = h
        for knot in range(len(rope)-1):
            h = rope[knot]
            t = rope[knot+1]
            touchin_tail = (abs(h[0] - t[0]) <= 1) and (abs(h[1] - t[1]) <= 1)#geddit?
            mod = [0, 0]
            if not touchin_tail:
                if t[0] > h[0]: mod[0] -= 1
                if t[0] < h[0]: mod[0] += 1
                if t[1] > h[1]: mod[1] -= 1
                if t[1] < h[1]: mod[1] += 1
                t = [t[0]+mod[0], t[1]+mod[1]]
            print("teh new hpos is:", h, "doin", instruction, "T@", t, mod, touchin_tail)
            rope[knot] = h
            rope[knot+1] = t
        if visited.get(tuple(rope[-1])) == None: visited[tuple(rope[-1])] = 0
        visited[tuple(rope[-1])] += 1

    
    
print(visited)
print(len(visited.keys()))
