def bfs(graph, start_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)
        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            # .get() prevents errors if a node has no outgoing edges
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

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
start = input("\nEnter the starting node for BFS: ")

# Perform BFS
if start in student_graph:
    result = bfs(student_graph, start)
    print("\nBFS Traversal:", result)
else:
    print("Starting node not found in the graph.")