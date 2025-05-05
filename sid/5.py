def prim_mst(graph, n):
    keys = [float('inf')] * n
    parent = [-1] * n
    keys[0] = 0
    mst_set = [False] * n

    for _ in range(n):
        u = min((keys[i], i) for i in range(n) if not mst_set[i])[1]
        mst_set[u] = True

        for v in range(n):
            if graph[u][v] and not mst_set[v] and graph[u][v] < keys[v]:
                keys[v] = graph[u][v]
                parent[v] = u

    print("Edge \tWeight")
    for i in range(1, n):
        print(f"{parent[i]} - {i} \t{graph[i][parent[i]]}")


n = int(input("Enter number of vertices: "))
graph = [list(map(int, input().split())) for _ in range(n)]
prim_mst(graph, n)
