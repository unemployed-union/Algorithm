from itertools import permutations

n, k = [int(x) for x in input().split(' ')]
weights = [int(x) for x in input().split(' ')]
check, answer = set(), 0

orders = tuple(permutations(weights))

for order in orders:
    base, history = 500, []
    for o in order:
        base += o - k
        history.append(o)

        if base < 500 or tuple(history) in check:
            history = tuple(history)
            if history not in check:
                check.add(history)
            break

    if base >= 500:
        answer += 1

print(answer)
