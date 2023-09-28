# -*- coding: utf-8 -*-
from grafo import Graph

def load_from(fileName):
    f = open(fileName, 'r')
    n = int(f.readline())
    
    g = Graph(n)
    
    l = 0
    for line in f:
        line.strip()
        numeros = line.split("\t")
        c = 0
        for i in numeros:
            if(c == g.num_vertices):
                break
            #print(i)
            g.matrix[l][c] = int(i)
            if(g.matrix[l][c] > 0):
                g.list[l].append(c)
            
            c += 1
        l += 1
    return g

gr = load_from("pcv4.txt")
gr.mostrar_matriz()
gr.mostrar_listas()
print('---------BFS----------')
gr.bfs(0,3)
print('---------DFS----------')
gr.dfs(0)