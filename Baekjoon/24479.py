import sys

node_num, line, start = (int(x) for x in sys.stdin.readline().rstrip().split(' '))
node_map, visited, record = {}, {x: False for x in range(node_num)}, []
stack = [start - 1]

for _ in range(line):
    a, b = (int(x) - 1 for x in sys.stdin.readline().rstrip().split(' '))

    if a in node_map.keys():
        node_map[a].append(b)
    else:
        node_map[a] = [b]

    if b in node_map.keys():
        node_map[b].append(a)
    else:
        node_map[b] = [a]

for n in node_map.keys():
    node_map[n] = sorted(node_map[n])[::-1]

while stack:
    node = stack.pop()

    if visited[node] is True:
        continue
    visited[node] = True

    if node in node_map.keys():
        stack.extend(node_map[node])

for node in visited.keys():
    if visited[node] is True:
        print(node + 1)
    else:
        print(0)
