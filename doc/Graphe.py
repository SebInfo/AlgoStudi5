import heapq

def dijkstra(graph, start, end):
    # On définit un dictionnaire pour les distances les plus courtes avec le point de départ
    # on initialise les distances à inf
    distances = {sommets: float('inf') for sommets in graph}
    print ("Dictionnaire des distances",distances)

    # En partant du premier sommet de notre chemin 
    # La distance avec lui même est de 0
    distances[start] = 0

    # On définit un dictionnaire pour stocker les nœuds précédents sur le chemin le plus court 
    # depuis le point de départ. Initialisez-les tous à null.
    precedents = {sommets: None for sommets in graph}
    print ("Dictionnaire des precedents",precedents)

    print ("J'ajoute le noeud : (0, '",start,"')")
    heap = [(0, start)]

    while heap:
        noeud = heapq.heappop(heap)
        print ("Je prend le noeud ",noeud)
        current_distance, current_vertex = noeud

        if current_vertex == end:
            break

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                precedents[neighbor] = current_vertex
                print ("Dictionnaire des precedents",precedents)
                element = (distance, neighbor)
                print ("J'ajoute le noeud :",element)
                heapq.heappush(heap, element)

    path = []
    current_vertex = end
    while current_vertex != start:
        path.insert(0, current_vertex)
        current_vertex = precedents[current_vertex]
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
