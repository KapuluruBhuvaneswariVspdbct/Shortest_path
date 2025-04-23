import heapq

def dijkstra(graph, start, end):
    queue = [(0, start, [start])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node == end:
            return cost, path

        if node in visited:
            continue

        visited.add(node)

        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(queue, (cost + weight, neighbor, path + [neighbor]))

    return float("inf"), []

def main():
    graph = {}
    edges = int(input("Enter number of edges: "))

    print("Enter edges in format: node1 node2 weight")
    for _ in range(edges):
        u, v, w = input().split()
        w = int(w)
        graph.setdefault(u, []).append((v, w))
        graph.setdefault(v, []).append((u, w))  # Remove this line if graph is directed

    start = input("Enter start node: ")
    end = input("Enter end node: ")
 
    if start not in graph or end not in graph:
        print("Start or end node not in graph.")
        return

    cost, path = dijkstra(graph, start, end)
    if cost == float('inf'):
        print(f"No path found from {start} to {end}.")
    else:
        print(f"Shortest path from {start} to {end}: {' -> '.join(path)} with cost {cost}")

if __name__ == "__main__":
    main()
