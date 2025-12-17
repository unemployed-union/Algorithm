import sys

node_num, line_num, start_node = (int(x) for x in sys.stdin.readline().rstrip().split(' '))
node_map, stack, visited, record, idx = {} ,[], {x: -1 for x in range(1, node_num + 1)}, [], 1

for _ in range(line_num):
    a, b = (int(x) for x in sys.stdin.readline().rstrip().split(' '))

    if a in node_map:
        node_map[a].append(b)
    else:
        node_map[a] = [b]
    
    if b in node_map:
        node_map[b].append(a)
    else:
        node_map[b] = [a]

stack.append(start_node)

for key in node_map.keys():
    node_map[key] = sorted(node_map[key])

while stack:
    node = stack.pop()
    
    if visited[node] != -1:
        continue
    visited[node] = idx
    idx += 1
    record.append(node)

    if node in node_map:
        stack.extend(node_map[node])

for key in sorted(visited.items(), key=lambda x: x[0]):
    print(key[1] if key[1] != -1 else 0)
