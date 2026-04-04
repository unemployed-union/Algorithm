import sys

string = sys.stdin.readline().rstrip()
temp = []
bomb = list(sys.stdin.readline().rstrip())
m = len(bomb)

for s in string:
    temp.append(s)

    if len(temp) >= m:
        if temp[-m:] == bomb:
            del temp[-m:]

if len(temp) == 0:
    print('FRULA')
else:
    print(''.join(temp))