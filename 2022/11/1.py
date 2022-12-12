f = [i.split("\n  ") for i in open("input", "r").read().split("\n\n")]
f = [i for i in f if i != ""]

mon = {}

for monkeys in f:
    n = int(monkeys[0].replace(":", "").split(" ")[1])
    items = [int(i) for i in monkeys[1].replace("Starting items: ", "").split(", ")]
    op = monkeys[2].replace("Operation: new = ", "").split(" ")
    test = [
        int(monkeys[3].replace("Test: divisible by ", "")),
        int(monkeys[4].replace("  If true: throw to monkey ", "")),
        int(monkeys[5].replace("  If false: throw to monkey ", "")),
    ]
    mon[n] = {"items": items, "op": op, "test": test, "shenanigan_ctr": 0}

from numpy import prod
wizardshit = prod([mon[key]["test"][0] for key in mon])

def round():
    for key in mon.keys():
        mk = mon[key] #;^)
        if len(mk["items"]) == 0: continue

        for item in mk["items"]:
            worry = eval(("".join(mk["op"])).replace("old", str(item)))
            #operation = [(str(item) if i == "old" else i) for i in mk["op"]]
            #print(operation);input()
            #worry = int(worry/3)
            worry %= wizardshit
            if worry%mk["test"][0] == 0:
                mon[mk["test"][1]]["items"].append(worry)
            else:
                mon[mk["test"][2]]["items"].append(worry)
            mon[key]["shenanigan_ctr"] += 1
        mon[key]["items"] = []

for i in range(10000):
    if i%10 == 0:
        print(i)
    round()


for key in mon: print(mon[key])
mnkybzns = [mon[key]["shenanigan_ctr"] for key in mon]
mnkybzns.sort()
print(mnkybzns[-1]*mnkybzns[-2])
