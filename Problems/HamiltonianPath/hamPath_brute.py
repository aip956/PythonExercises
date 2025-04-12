import itertools

def generate_permutations(n):
    return list(itertools.permutations(range(n)))

def is_valid_path(graph, path):
    for i in range(len(path) - 1):
        if graph[path[i]][path[i+1]] == 0:
            return False # No edge between these 2 nodes
    return True

def hamiltonian_path_brute_force(graph):
    n = len(graph)
    for path in generate_permutations(n):
        if is_valid_path(graph, path):
            return list(path)
    return [] # No valid path found


# Test Case
islands = [
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1],
    [0, 1, 0, 0, 1],
    [1, 1, 0, 0, 1],
    [0, 1, 1, 1, 0]
]

print(hamiltonian_path_brute_force(islands))