def floyd_warshall(graph):
    n = len(graph)
    for k in range(n):
        for i in range(n):
            for j in range(n):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
    return graph

graph = [
    [0, float('inf'), 5],
    [3, 0, float('inf')],
    [float('inf'), 2, 0]]
for row in floyd_warshall(graph):
    print(*[f'{a:>3}' for a in row])