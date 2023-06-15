import heapq

def dijkstra(graph, start, end):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    previous_vertices = {vertex: None for vertex in graph}

    heap = [(0, start)]

    while heap:
        current_distance, current_vertex = heapq.heappop(heap)

        if current_vertex == end:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_vertices[neighbor] = current_vertex
                heapq.heappush(heap, (distance, neighbor))

    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = previous_vertices[current_vertex]
    path.insert(0, start)

    return path, distances[end]

# Exemple d'utilisation
graph = {
    'A': {'B': 1, 'C': 2},
    'B': {'A': 1, 'D': 2, 'F': 3},
    'C': {'A': 2, 'D': 3, 'E': 4},
    'D': {'B': 2, 'C': 3, 'F': 3, 'G': 3, 'E':2},
    'E': {'C': 4, 'D': 2, 'G': 5},
    'F': {'B': 3, 'D': 3, 'G':4},
    'G': {'F':4, 'D':3, 'E':5 }
}

start_vertex = 'A'
end_vertex = 'G'

shortest_path, distance = dijkstra(graph, start_vertex, end_vertex)

print("Plus court chemin:", shortest_path)
print("Distance:", distance)
