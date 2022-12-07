f = open("input", "r").read().replace("\n", "")

buf = []
for idx, c in enumerate(f):
    buf.append(c)
    if len(buf) > 14:
        buf.pop(0)
    good = True
    for i in buf:
        if buf.count(i) > 1 or len(buf) < 14: good = False
    if good:
        print(idx+1)
        input()
    
    #print(buf, good, buf.count(i), idx+1)
