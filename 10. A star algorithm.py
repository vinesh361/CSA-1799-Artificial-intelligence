import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, cost):
        self.edges[from_node].append((to_node, cost))
        self.edges[to_node].append((from_node, cost))  # Assuming an undirected graph

def astar(graph, start, goal):
    open_set = []
    closed_set = set()
    heapq.heappush(open_set, (0, start, []))  # Priority queue with initial cost, current node, and path

    while open_set:
        current_cost, current_node, path = heapq.heappop(open_set)

        if current_node == goal:
            return path + [current_node]

        if current_node in closed_set:
            continue

        closed_set.add(current_node)

        for neighbor, cost in graph.edges[current_node]:
            if neighbor not in closed_set:
                g_value = current_cost + cost
                h_value = heuristic(neighbor, goal)  # Heuristic function
                f_value = g_value + h_value
                heapq.heappush(open_set, (f_value, neighbor, path + [current_node]))

    return None  # No path found

def heuristic(node, goal):
    # Example heuristic function (Euclidean distance for simplicity)
    x1, y1 = node
    x2, y2 = goal
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Example usage:
if __name__ == "__main__":
    # Create a graph
    g = Graph()
    g.add_node((0, 0))
    g.add_node((1, 0))
    g.add_node((1, 1))
    g.add_node((2, 1))
    g.add_node((2, 2))
    g.add_node((3, 2))

    g.add_edge((0, 0), (1, 0), 1)
    g.add_edge((1, 0), (1, 1), 1)
    g.add_edge((1, 1), (2, 1), 1)
    g.add_edge((2, 1), (2, 2), 1)
    g.add_edge((2, 2), (3, 2), 1)

    start_node = (0, 0)
    goal_node = (3, 2)

    path = astar(g, start_node, goal_node)

    if path:
        print(f"Shortest Path from {start_node} to {goal_node}: {path}")
    else:
        print("No path found.")
