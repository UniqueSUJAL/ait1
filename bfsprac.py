graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]}
visited=[]
queue=[]
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)

    while queue:
        m=queue.pop()
        print(m,end=" ")

        for i in graph[m]:
            if i not in visited:
                visited.append(i)
                queue.append(i)
bfs(visited,graph,'5')

print()

graph={
    '5':['3','7'],
    '3':['2','4'],
    '7':['8'],
    '2':[],
    '4':['8'],
    '8':[]}

vistied=set()
def dfs(vistied,graph,node):
    if node not in vistied:
        print("dfs",node)
        vistied.add(node)
        for i in graph[node]:
            
            dfs(vistied,graph,i)
dfs(vistied,graph,'5')
from sys import maxsize
from itertools import permutations
V=4
def tsf(graph,s):
    vertex=[]
    for i in range(V):

        if i!=s:
            vertex.append(i)

    min_path=maxsize
    next_p=permutations(vertex)
    for i in next_p:
        curr=0
        k=s
        for j in i:
            curr+=graph[k][j]
            k=j
        curr+=graph[k][s]
        min_path=min(min_path,curr)
    print(min_path)
    return min_path
        
if __name__=='__main__':
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(tsf(graph, s))

        

            
            
