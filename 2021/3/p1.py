f = open("input", "r")
r = f.read()
f.close()

r = r.split("\n")
r = list(filter(len, r))

gamm = ""
eps = ""

for shift in range(len(r[0])):
	slice = [n[shift] for n in r]
	gamm += (str(max(slice, key = slice.count)))
	eps += (str(min(slice, key = slice.count)))

print(int(bytes(gamm, "ascii"), 2) * int(bytes(eps, "ascii"), 2))
