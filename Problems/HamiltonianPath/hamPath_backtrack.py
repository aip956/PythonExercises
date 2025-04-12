
def hamiltonian_path_backtracking(graph):
    n = len(graph) # Num nodes
    visited = [False] * n # Track nodes visited

    def backtrack(current_node, path):
        if len(path) == n:
            return path # Found a valid path
        
        for neighbor in range(n):
            if graph[current_node][neighbor] == 1 and not visited[neighbor]:
                visited[neighbor] = True
                result = backtrack(neighbor, path + [neighbor])
                if result:
                    return result # Found a path deeper in recursion
                visited[neighbor] = False # Backtrack
        return None # No valid path from this node
    
    # Try starting from every node
    for start in range(n):
        visited[start] = True
        result = backtrack(start, [start])
        if result:
            return result #Found a valid path starting here
        visited[start] = False # Try next starting node
    return [] # No Ham Path found

islands = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

print(hamiltonian_path_backtracking(islands))