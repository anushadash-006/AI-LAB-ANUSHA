# 1. Take heuristic values for each node

def get_user_inputs():
    heuristic = {}

    num_nodes = int(input("Enter total number of nodes: "))

    print("Enter heuristic values for each node:")

    for i in range(num_nodes):
        node = input("Node name: ").strip().upper()
        h_value = float(input(f"Heuristic value for {node}: "))
        heuristic[node] = h_value

    # 2. Take input for graph connections
    graph = {node: [] for node in heuristic}

    num_edges = int(input("Enter total number of directed edges: "))

    print("Enter each edge in the format (from-node to-node weight):")

    for i in range(num_edges):
        u, v, w = input(f"Edge {i + 1}: ").strip().split()

        u = u.upper()
        v = v.upper()
        weight = float(w)

        graph[u].append((v, weight))

    return graph, heuristic


# A* Search Algorithm
def a_star_search(graph, heuristic, start, goal):
    open_list = [(start, 0)]
    came_from = {}
    g_cost = {start: 0}

    while open_list:

        # Select node with minimum f(n) = g(n) + h(n)
        current = min(
            open_list,
            key=lambda x: x[1] + heuristic[x[0]]
        )

        open_list.remove(current)
        current_node = current[0]

        # Goal check and path reconstruction
        if current_node == goal:
            path = [goal]

            while current_node in came_from:
                current_node = came_from[current_node]
                path.append(current_node)

            path.reverse()

            return path, g_cost[goal]

        # Explore neighbours
        for neighbour, cost in graph.get(current_node, []):
            new_cost = g_cost[current_node] + cost

            if neighbour not in g_cost or new_cost < g_cost[neighbour]:
                g_cost[neighbour] = new_cost
                came_from[neighbour] = current_node
                open_list.append((neighbour, new_cost))

    # No path found
    return None, float("inf")


# Main Program
graph, heuristic = get_user_inputs()

start = input("Enter start node: ").strip().upper()
goal = input("Enter goal node: ").strip().upper()

path, cost = a_star_search(graph, heuristic, start, goal)

if path:
    print("\nOptimal path:", " -> ".join(path))
    print("Total cost:", cost)
else:
    print("\nNo path found")