def bfs_target_search(graph, start_node, target_node):
    visited = []
    queue = [start_node]

    while queue:
        current_node = queue.pop(0)

        if current_node not in visited:
            print(f"Exploring node: {current_node}")
            visited.append(current_node)

            # Check if target is found
            if current_node == target_node:
                print(f"\nTarget node '{target_node}' found!")
                return True

            # Add unvisited neighbors to the queue
            for neighbor in graph.get(current_node, []):
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)

    print(f"\nTarget node '{target_node}' not found!")
    return False


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

    # Add the connection (Undirected Graph)
    student_graph[u].append(v)
    student_graph[v].append(u)

# Display the graph
print("\nGraph:")
for node in student_graph:
    print(f"{node} -> {student_graph[node]}")

# Get start and target nodes
start = input("\nEnter the starting node: ")
target = input("Enter the target node to search: ")

# Perform Target Search
if start in student_graph:
    bfs_target_search(student_graph, start, target)
else:
    print("Starting node not found in the graph.")