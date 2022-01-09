n = input()

position = len(n)
half = position //2
leftside = 0
rightside = 0
for _ in range(half):
    leftside += int(n[_])
for _ in range(half,position):
    rightside += int(n[_])

if rightside == leftside:
    print("LUCKY")
else:
    print("READY")
