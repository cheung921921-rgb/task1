from collections import deque

def create_graph():
    print("Please enter the names of 5 nodes:")
    nodes = []
    for i in range(5):
        node_name = input(f"Enter name for node {i+1}: ").strip()
        nodes.append(node_name)

    graph = {node: [] for node in nodes}

    for node in nodes:
        while True:
            connections = input(f"Which nodes should node {node} be connected to? (separate by spaces): ").split()
            valid = True
            for conn in connections:
                if conn not in nodes:
                    print(f"Invalid name! Please enter again. The names of nodes are: {', '.join(nodes)}")
                    valid = False
                    break
            if valid:
                for conn in connections:
                    if conn not in graph[node]:
                        graph[node].append(conn)
                    if node not in graph[conn]:
                        graph[conn].append(node)
                break

    return graph, nodes


def shortest_path(graph, start, end):
    visited = set()
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path

        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None


def query_graph(graph, nodes):
    while True:
        print("\nOptions:")
        print("1. Check connections of node")
        print("2. Shortest distance from node to node")
        print("3. Exit programme")

        choice = input("Enter your choice (1-3): ").strip()

        if choice == "3":
            print("Exiting programme.")
            break

        elif choice == "1":
            node = input("Enter node name: ").strip()
            if node not in nodes:
                print(f"Invalid name! The names of nodes are: {', '.join(nodes)}")
            else:
                connections = graph[node]
                if connections:
                    print(f"{node} is connected to: {', '.join(connections)}")
                else:
                    print(f"{node} has no connections.")

        elif choice == "2":
            start = input("Enter start node: ").strip()
            end = input("Enter end node: ").strip()
            if start not in nodes or end not in nodes:
                print(f"Invalid name! The names of nodes are: {', '.join(nodes)}")
            else:
                path = shortest_path(graph, start, end)
                if path:
                    print(f"Shortest path from {start} to {end}: {' -> '.join(path)} (length {len(path)-1})")
                else:
                    print(f"No path found between {start} and {end}.")

        else:
            print("Invalid option! Please enter 1, 2, or 3.")


def main():
    graph, nodes = create_graph()
    print("\nGraph successfully created!")
    query_graph(graph, nodes)


if __name__ == "__main__":
    main()
