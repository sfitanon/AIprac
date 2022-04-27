from collections import defaultdict

visited = []
queue = []
        
def dfs(visited, graph, node, target,cost):   
    if node not in visited:
        #print (node)
        cost+=1;
        visited.append(node)
        if node == target: 
          print(*visited, sep="->")
          print("Cost:",cost)
          return
        for neighbour in graph[node]: 
            dfs(visited, graph, neighbour, target, cost) 

    
def comDFS(): 
    print("Depth-First Search") 
    target = int(input('Enter Target Node: '))
    start= int(input('Enter Start Node: '))
    dfs(visited, graph, start, target,0)
    if target not in visited: 
        print('Target not found')
        
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
comDFS()

 
