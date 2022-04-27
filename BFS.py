from collections import defaultdict

visited = []
queue = []

def bfs(visited, graph, node, target,cost): 
    cost+=1
    visited.append(node)
    queue.append(node)
    while queue: 
        s = queue.pop(0)
        #print (s, end = " ")
        for neighbour in graph[s]:
            if neighbour not in visited:
                cost+=1;
                visited.append(neighbour)
                queue.append(neighbour)
                if neighbour == target:
                    print(*visited, sep="->")
                    print("Cost:",cost)
                    break
    if target not in visited: 
        print('Target not found')
        
def comBFS(): 
    print("Breadth First Search") 
    target = int(input('Enter Target Node: '))
    start= int(input('Enter Start Node: '))
    bfs(visited, graph, start, target,0)
    
graph = defaultdict(list)
def addEdge(graph,u,v):
    graph[u].append(v) 
def print_edges(graph): 
    edges = []
    for node in graph:
        for neighbour in graph[node]: 
            edges.append((node, neighbour))
    return edges 
   
n=int(input("Enter Number of Node \n"))
m=int(input("Enter Number of Edges \n"))

print("Enter" , m , "Edges")
for i in range(m): 
    u, v = map(int, input().split())
    addEdge(graph,u,v)
    
print("Adjacency List of Entered Graph:")
print(print_edges(graph))
comBFS() 

