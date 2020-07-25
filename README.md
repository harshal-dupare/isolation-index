# <center>Isolation Index</center>
___________

## Collaboration between IIT Kharagpur & INPE - Instituto Nacional de Pesquisas Espaciais through Foregin Training Program  (FTP) of International Relations Cell IIT Kharagpur for the year 2019-2020.k
## Harshal Dupare | 18MA20015 | Sophomore at IIT Kharagpur

____________
## Introduction
Given a graph <img src="https://render.githubusercontent.com/render/math?math=G = (N,L)">, let <img src="https://render.githubusercontent.com/render/math?math=L_k"> be the set of edges connected to a node <img src="https://render.githubusercontent.com/render/math?math=k"> where <img src="https://render.githubusercontent.com/render/math?math=k \in N">. The isolation index of the node <img src="https://render.githubusercontent.com/render/math?math=k"> is given by <img src="https://render.githubusercontent.com/render/math?math=Q_k">, which is the number of 'inﬁnite length paths' between any pair of nodes in the graph <img src="https://render.githubusercontent.com/render/math?math=H = (N,(L-L_k))">. This is equivalent to the number of disconnected pairs of nodes (i.e. there does not exist a path joining one node to another). The intuition behind the Isolation index is the following: it quantifies the inaccessibility in the network when a specific element (node or edges) is disconnected, like in a flooding or construction work. 

____________
## Algorithm's Pseudocode:

```
Isolation_Index(G,v):
    H <- G.disconnect_node(v)
    component_sizes <- Connected_Component(H).sizes
    total <- G.node_count
    isolation_index_v <- 0
    for component_size in component_sizes
           total <- total - component_size
           isolation_index_v <- isolation_index_v + 2*total*component_size
    return isolation_index_v
```

_________
## Example

1. Node of interest is the red color node we will showthe computation of isolation index for it, sameprocess follows for all other nodes.

![Original graph](https://github.com/harshal3d/isolation-index/blob/master/Diagrams/original_graph.png)

2. Disconnect the red node gives the resultant graph <img src="https://render.githubusercontent.com/render/math?math=H">.

![Node disconnected](https://github.com/harshal3d/isolation-index/blob/master/Diagrams/node_disconnected.png)

3. Identifying the connected components

![](https://github.com/harshal3d/isolation-index/blob/master/Diagrams/clusters_identified.png)

4. Getting the sizes of the connected components

![](https://github.com/harshal3d/isolation-index/blob/master/Diagrams/clusters_size_calculated.png)

5. Initially set Isolation index of node to <img src="https://render.githubusercontent.com/render/math?math=0">. The lines joining 2 components represent the number of disconnected ordered pairs for nodes between them. The diagram shows calculation for the <img src="https://render.githubusercontent.com/render/math?math=1^{st}">. component <img src="https://render.githubusercontent.com/render/math?math=C_1">. w.r.t all other components ( This step is shown just for explanation sake in algorithm we directly calculate by the next method )

![](https://github.com/harshal3d/isolation-index/blob/master/Diagrams/clusters_pairs_calculation.png)

6. Simplified calculation for <img src="https://render.githubusercontent.com/render/math?math=1^{st}"> component using the compliment of the component as <img src="https://render.githubusercontent.com/render/math?math=\overline{C_1}"> add the total to the isolation index count. This is where the variable <img src="https://render.githubusercontent.com/render/math?math=total"> is used for representing the number of nodes in the compliment component for each component as we progress to calculate the isolation index

![](https://github.com/harshal3d/isolation-index/blob/master/Diagrams/compliment_cluster_calculation.png)

7. Moving on to the contributions from the next component, hence removing the <img src="https://render.githubusercontent.com/render/math?math=1^{st}"> component as it's contribution is already taken into account. Repeat this process ( from 5/6 )  for all other components and adding the contribution from each component gives the Isolation index.

![](https://github.com/harshal3d/isolation-index/blob/master/Diagrams/moving_on_to_next_cluster.png)
