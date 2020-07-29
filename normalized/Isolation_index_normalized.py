from igraph import *
import numpy as np
import itertools
import time

class GraphMaking:


    def __init__(self):
        self.graph = None
        self.order = 0
        self.infinities = []
        self.filee = 'complete'

    def create_graph(self):
        self.graph = Graph()
        input_file = open('input\\'+self.filee+'.txt', 'r')
        self.vertices_list = []  # List that contains all the vertices of the graph
        adjacency_list = input_file.readlines()  # holds the read file's list.
        for row in adjacency_list:  # Iterate for each row in the read list
            row = row.rstrip('\n')  # Removes the break line character
            try:
                v1, v2 = row.split(',')  # Temporary vavriables to get each node of the input line
                if v1 not in self.vertices_list:  # Verifies if the node is not on the vertices_list
                    self.graph.add_vertex(v1)  # Adds the new vertex to the graph
                    self.vertices_list.append(v1)  # Adds the new vertex to the vertices_list
                if v2 not in self.vertices_list:
                    self.graph.add_vertex(v2)  # Adds the new vertex to the graph
                    self.vertices_list.append(v2)  # Adds the new vertex to the vertices_list
                self.graph.add_edge(v1, v2)  # Creates a connection between the pair o vertices
            except:  # if there there's only one vertice in the input line
                v1 = row[0:]  # v1 will be that value
                if v1 not in self.vertices_list:  # Verify if the vertex is not on the vertices_list
                    self.graph.add_vertex(v1)  # Adds the new vertex to the graph
                    self.vertices_list.append(v1)  # Adds the new vertex to the vertices_list

        input_file.close()
        self.graph.vs['label'] = self.vertices_list  # labels the vertices according to the vertices_list
        self.order = self.graph.vcount()

    def isolation(self):

        base_components_sizes = self.graph.components().sizes() #List of the sizes of components
        total = self.graph.order
        max_isolation_index=total*(total-1)
        base_isolation_index = 0
        # looping through all components and counting unreachable pairs of vertices in newly modified graph
        for c in base_components_sizes:
            total = total - c
            base_isolation_index+= 2*c*total

        for i in range(0,self.order):
            self.accumulates_infinities = 0
            graph_copy = self.graph.copy()
            del_list = []  # lista que conterá os ids das arestas do vértice 'i' que serão removidas. #will contain the edge's ids (the ones that will be removed)
            for target_vertex_id in range(0, self.order):
                try:
                    del_list.append(graph_copy.get_eid(i,target_vertex_id))  #Gets the id of the edge that belongs to the pair of vertices(i,target_vertex_id) and puts it in 'del_list'
                except:
                    pass  # in case the id does not exist
            graph_copy.delete_edges(del_list)   #deletes all edges connected to the node i

            components_sizes = graph_copy.components().sizes() #List of the sizes of components
            total = self.order
            count = 0
            # looping through all components and counting unreachable pairs of vertices in newly modified graph
            for c in components_sizes:
                total = total - c
                count+= 2*c*total
            self.infinities.append(float((count-base_isolation_index)/(max_isolation_index-base_isolation_index)))

    def create_results(self):
        output_local = open('output\output_'+self.filee+'_normalized.txt', 'a')
        output_local.write('vertice' + ':' + 'isolation_index \n')
        for i in range(0, grp.order):
            output_local.write(str(self.vertices_list[i]) + ':' + str(self.infinities[i]) + '\n')

t=time.time()
grp = GraphMaking()
grp.create_graph()
grp.isolation()
t=time.time()-t
grp.create_results()
print(t)
