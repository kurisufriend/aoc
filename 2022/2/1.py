f = open("input", "r").read().split("\n")

key = {
    "A": "R",
    "B": "P",
    "C": "S",
    "X": "R",
    "Y": "P",
    "Z": "S",
}

trumps = {
    ("R", "S"): "LOSS",
    ("R", "P"): "WIN",
    
    ("P", "R"): "LOSS",
    ("P", "S"): "WIN",
    
    ("S", "R"): "WIN",
    ("S", "P"): "LOSS",
}

scorekey = {
    "R": 1,
    "P": 2,
    "S": 3
}

outkey = {
    "WIN": 6,
    "DRAW": 3,
    "LOSS": 0
}

towin = {
    "R": "P",
    "P": "S",
    "S": "R"
}

tolose = {
    "R": "S",
    "P": "R",
    "S": "P"
}

total = 0
for round in f:
    if round == '': continue
    t = round.split(" ")
    opp = key[t[0]]
    u = t[1]
    if u == "X":
        u = tolose[opp]
    elif u == "Y":
        u = opp
    elif u == "Z":
        u = towin[opp]
    res = "DRAW" if opp==u else trumps[(opp, u)]
    sc = scorekey[u]
    sc = sc + outkey[res]
    print(opp, u, res, sc)
    total += sc
print(total)
