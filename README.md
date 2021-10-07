# AlgosandDataStructures
A python package that provides useful algorithms and data structures commonly used in competitive programming contests.
 To install, use 
```bash
pip install AlgosandDataStructures==1.0
```

Exemple:
```python
from AlgosandDataStructures import Dijkstra

graph = {}

for i in range(5):
    graph[i] = []

graph[0].append((1,1))
graph[0].append((2,5))
graph[1].append((4,3))
graph[1].append((3,7))
graph[2].append((1,8))
graph[3].append((4,7))

print(Dijkstra.Dijkstra(graph,0,4,5))
```

Algorithms: <br />
Binary search <br />
Lower bound <br />
Upper bound <br />
Dijkstra <br />
Floyd warshal <br />
An explanation on how to implement a graph using adjancency list of adjacency matrix (Use 
```bash
from AlgosandDataStructures import howtoGraph
```
and then do
```bash
from  howtoGraph.how_to()
```
to see the information)
<br />
Data structures: <br />
Fenwick tree <br />
Stack <br />

I'm gonna keep adding new stuff to the package when i have time
