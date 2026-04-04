n, k = (int(x) for x in input().split(' '))
coin, memory = [], {x: 0 for x in range(k + 1)}

for _ in range(n):
    coin.append(int(input()))

memory[0] = 1

for c in coin:
    for i in range(c, k + 1):
        memory[i] += memory[i - c]

print(memory[k])