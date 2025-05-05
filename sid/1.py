def create_graph():

    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B'],
        'F': ['C']
    }
    return graph

def dfs_recursive(graph, vertex, visited=None):
    
    if visited is None:
        visited = set()
    
    
    visited.add(vertex)
    print(vertex, end=' ')
    
    
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)
    
    return visited


if __name__ == "__main__":
    graph = create_graph()
    
   
    print("DFS traversal starting from vertex A:")
    dfs_recursive(graph, 'A')