

def Floydwarshall(graph,numvertex):
    
    dist = graph 
    for k in range(numvertex):
        for i in range(numvertex):
            for j in range(numvertex):
                if dist[i][j] > (dist[i][k] + dist[k][j]) and (dist[k][j] != float('inf') and dist[i][k] != float('inf')):
                    dist[i][j] = dist[i][k] + dist[k][j]
    

    return dist

def how_to():
    print("Use a adjacency matrix to use the algorithm, if vertices u and v are not connected,\n the graph[u][v] = float('inf')")


graph = {}

for i in range(5):
    graph[i] = []

for i in range(5):
    for j in range(5):
        graph[i].append(float('inf'))

graph[0][1] = 1
graph[0][2] = 5
graph[1][4] = 3
graph[1][3] = 7
graph[2][1] = 8
graph[2][3] = 10
graph[3][4] = 4


d = Floydwarshall(graph,5)

print(d)
