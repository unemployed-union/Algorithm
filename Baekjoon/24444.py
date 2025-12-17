import sys
from collections import deque

node_num, edge_num, start_num = (int(x) for x in sys.stdin.readline().rstrip().split(' '))
node_map, visited, queue, idx = {}, {x: 0 for x in range(1, node_num + 1)}, deque(), 1

queue.append(start_num)

for _ in range(edge_num):
    a, b = (int(x) for x in sys.stdin.readline().rstrip().split(' '))

    if a in node_map:
        node_map[a].append(b)
    else:
        node_map[a] = [b]
    if b in node_map:
        node_map[b].append(a)
    else:
        node_map[b] = [a]

for key in node_map.keys():
    node_map[key] = sorted(node_map[key])

while queue:
    node = queue.popleft()
    
    if visited[node] != 0:
        continue
    visited[node] = idx
    idx += 1

    if node in node_map:
        queue.extend(node_map[node])

for item in visited.items():
    print(item[1])

