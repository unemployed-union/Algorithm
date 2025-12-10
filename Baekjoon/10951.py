import sys

texts = sys.stdin.readlines()
for text in texts:
    t = text.split(' ')
    a, b = (int(x.strip()) for x in t)
    print(a + b)