f = open("bigboy_patched.txt", "r").read().split("$ ")

f = [i.strip().split("\n") for i in f]
f = list(filter(lambda i: i != [""], f))
#print(f)

fs = {}
pwd = "/"

for cmd in f: 
    if cmd[0].startswith("cd"):
        di = cmd[0].split(" ")[1]
        if di == "..":
            pwd = "/"+("/".join(list(filter(lambda e: e != "", pwd.split("/")))[:-1]))+"/"
        else: pwd = di if di.startswith("/") else pwd+di+"/"
        if pwd [0:2] == "//": pwd = "/"+pwd[2:]
    elif cmd[0].startswith("ls"):
        for f in cmd[1:]:
            if fs.get(pwd) == None:
                fs[pwd] = []
            fs[pwd].append(f.split(" "))
    #print(cmd, pwd)
#print("\n\n")
def collect(root):
    acc = []
    for sub in fs[root]:
         if sub[0] == "dir":
            acc.extend(collect(root+sub[1]+"/"))
         else: acc.append(sub)
    return acc
#print(fs)
totals = {}
available = 70000000
need_free =  30000000
for d in fs.keys():
    files = collect(d)
    total = sum([int(i[0]) for i in files])
    totals[d] = total
    #print(d, total, files)

#t = 0
#for to in totals.values():
#    if to <= 100000:
#        t += to
#print(t)

print("free:", available-totals["/"])

todel = need_free - (available-totals["/"])
print(todel)
best_size = 99999999999999999999
for to in totals.values():
    if to >= todel and to < best_size:
        best_size = to

print(best_size)
