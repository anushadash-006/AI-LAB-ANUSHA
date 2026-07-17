graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

visited = []
queue = []
start = 'A'

visited.append(start)
queue.append(start)

while queue:
    current = queue.pop(0)
    print(current, end=" ")

    for neighbour in graph[current]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)