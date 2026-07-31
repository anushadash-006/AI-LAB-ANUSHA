def dfs(graph, start_node):
    visited = []
    stack = [start_node]

    while stack:
        current_node = stack.pop()

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            # Add neighbors in reverse order to maintain traversal order
            for neighbor in reversed(graph.get(current_node, [])):
                if neighbor not in visited:
                    stack.append(neighbor)

    return visited


# ---------------- User Input Section ----------------

print("----- Build Your Graph -----")
student_graph = {}

# Get the total number of edges
num_edges = int(input("How many edges (connections) does your graph have? "))

print("Enter each edge separated by a space (e.g., A B):")

# Read all edges
for i in range(num_edges):
    u, v = input(f"Edge {i + 1}: ").split()

    # Initialize adjacency lists if nodes don't exist
    if u not in student_graph:
        student_graph[u] = []

    if v not in student_graph:
        student_graph[v] = []

    # Add the connection (undirected graph)
    student_graph[u].append(v)
    student_graph[v].append(u)

# Display the graph
print("\nGraph:")
for node in student_graph:
    print(f"{node} -> {student_graph[node]}")

# Get the starting node
start = input("\nEnter the starting node for DFS: ")

# Perform DFS
if start in student_graph:
    result = dfs(student_graph, start)
    print("\nDFS Traversal:", result)
else:
    print("Starting node not found in the graph.")