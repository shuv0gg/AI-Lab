# Romania Map (graph with distances)
graph = {
    'Arad': [('Zerind',75), ('Sibiu',140), ('Timisoara',118)],
    'Zerind': [('Arad',75), ('Oradea',71)],
    'Oradea': [('Zerind',71), ('Sibiu',151)],
    'Sibiu': [('Arad',140), ('Oradea',151), ('Fagaras',99), ('Rimnicu Vilcea',80)],
    'Timisoara': [('Arad',118), ('Lugoj',111)],
    'Lugoj': [('Timisoara',111), ('Mehadia',70)],
    'Mehadia': [('Lugoj',70), ('Drobeta',75)],
    'Drobeta': [('Mehadia',75), ('Craiova',120)],
    'Craiova': [('Drobeta',120), ('Rimnicu Vilcea',146), ('Pitesti',138)],
    'Rimnicu Vilcea': [('Sibiu',80), ('Craiova',146), ('Pitesti',97)],
    'Fagaras': [('Sibiu',99), ('Bucharest',211)],
    'Pitesti': [('Rimnicu Vilcea',97), ('Craiova',138), ('Bucharest',101)],
    'Bucharest': []
}

# Heuristic (straight-line distance to Bucharest)
h = {
    'Arad':366,'Zerind':374,'Oradea':380,'Sibiu':253,'Timisoara':329,
    'Lugoj':244,'Mehadia':241,'Drobeta':242,'Craiova':160,
    'Rimnicu Vilcea':193,'Fagaras':178,'Pitesti':98,'Bucharest':0
}

Start = 'Arad'
Goal = 'Bucharest'

def A_star():
    OPEN = [(Start, 0, [Start])]  # (node, g, path)
    CLOSED = []

    while OPEN:
        # sort by f(n) = g + h
        OPEN.sort(key=lambda x: x[1] + h[x[0]])
        
        node, g, path = OPEN.pop(0)

        if node == Goal:
            return path, g

        CLOSED.append(node)

        for neighbor, cost in graph[node]:
            if neighbor not in CLOSED:
                OPEN.append((neighbor, g + cost, path + [neighbor]))

    return None, None

# Run
path, cost = A_star()

print("Final Path:", " → ".join(path))
print("Total Cost:", cost)