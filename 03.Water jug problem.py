from collections import deque

def water_jug_problem(capacity_x, capacity_y, target):
    visited = set()
    initial_state = (0, 0)  # Initial state with both jugs empty
    queue = deque([initial_state])

    while queue:
        current_state = queue.popleft()
        x, y = current_state

        if x == target or y == target:
            return current_state

        # Define possible actions: Fill jug x, fill jug y, empty jug x, empty jug y, pour from x to y, pour from y to x
        actions = [
            (capacity_x, y),
            (x, capacity_y),
            (0, y),
            (x, 0),
            (min(x + y, capacity_x), max(0, x + y - capacity_x)),
            (max(0, x + y - capacity_y), min(x + y, capacity_y))
        ]

        for action in actions:
            if action not in visited:
                queue.append(action)
                visited.add(action)

    return None  # If no solution is found

def print_solution(solution, capacity_x, capacity_y):
    if solution:
        x, y = solution
        print("Solution:")
        print(f"Jug X: {x}/{capacity_x}")
        print(f"Jug Y: {y}/{capacity_y}")
    else:
        print("No solution exists.")

if __name__ == "__main__":
    capacity_x = 4  # Capacity of jug X
    capacity_y = 3  # Capacity of jug Y
    target = 2  # Desired amount of water

    solution = water_jug_problem(capacity_x, capacity_y, target)
    print_solution(solution, capacity_x, capacity_y)
