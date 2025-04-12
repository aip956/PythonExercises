import itertools

def generate_permutations(n):
    return list(itertools.permutations(range(n)))

def is_valid_path(graph, path):
    