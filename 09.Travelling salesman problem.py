from itertools import permutations

def calculate_total_distance(path, graph):
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += graph[path[i]][path[i + 1]]
    total_distance += graph[path[-1]][path[0]]  # Return to the starting city
    return total_distance

def traveling_salesman_bruteforce(graph):
    num_cities = len(graph)
    all_cities = list(range(num_cities))
    all_permutations = permutations(all_cities)

    min_distance = float('inf')
    best_path = None

    for path in all_permutations:
        distance = calculate_total_distance(path, graph)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return best_path, min_distance

# Example usage:
if __name__ == "__main__":
    # Example graph (distance between cities)
    example_graph = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    best_path, min_distance = traveling_salesman_bruteforce(example_graph)

    print(f"Best Path: {best_path}")
    print(f"Minimum Distance: {min_distance}")
