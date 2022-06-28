from collections import defaultdict

'''
A graph is similar with BFT of tree but only difference is graph can contain cycle
-> We have to consider whether we visited or not
Time Complexity? O(V + E) <- V is numbers of nodes and E is edges
Space Complexity? O(V) <- We store value within the node
'''

class Graph:
    def __init__(self):
        # Graph = 'A': ['B', 'C'], 'D': ['E']
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)
    
    def BFS(self, s):

        visited = [False] * (max(self.graph) + 1)
        queue = []

        queue.append(s)
        visited[s] = True
        
        while queue:
            s = queue.pop()
            print(s, end = " ")

            for i in self.graph[s]:
                if visited[i] == False:
                    queue.append(i)
                    visited[i] = True


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)
 
print ("Following is Breadth First Traversal"
                  " (starting from vertex 2)")
g.BFS(2)

