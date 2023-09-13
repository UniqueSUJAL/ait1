from sys import maxsize
from itertools import permutations
from sys import maxsize
from itertools import permutations
V=4
def tsf(graph,s):
    vertex=[]
    for i in range(V):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    curr_per=permutations(vertex)
    for i in curr_per:
        curr_pathweight=0
        k=s
        for j in i:
            curr_pathweight+=graph[k][j]
            k=j
        curr_pathweight+=graph[k][s]
        m=min(min_path,curr_pathweight)
    return m
        
if __name__=='__main__':
    graph = [[0, 10, 15, 20], [10, 0, 35, 25],
             [15, 35, 0, 30], [20, 25, 30, 0]]
    s = 0
    print(tsf(graph, s))

        

    s = 0
    print(tsf(graph, s))

        
