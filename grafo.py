# -*- coding: utf-8 -*-
import queue
from collections import deque

class Graph:
    def __init__(self,n):
        self.num_vertices = n   
        self.matrix = [[0 for j in range(n)] for i in range(n)] 
        self.list = [[] for _ in range(n)]

    #Extra: fiz uma função para caso quisesse adicionar uma aresta no grafo
    def adiciona_aresta(self,vertice1,vertice2,peso):
        self.matrix[vertice1-1][vertice2-1] = peso 
        self.matrix[vertice2-1][vertice1-1] = peso 
        self.list[vertice2-1].append(vertice1)
        self.list[vertice1-1].append(vertice2) 
    #Função para mostrar a matriz
    def mostrar_matriz(self):
        print('A matriz de adjacências é:')
        for i in range(self.num_vertices):
            print(self.matrix[i])
    #Função para mostrar a lista de adjacências:
    def mostrar_listas(self):
        print('As listas de adjacências são:')
        count = 0
        for i in self.list:
            print(f'{count}: {i}')
            count+=1
    #Busca em largura que retorna o melhor caminho de um vertice1 a um vertice2:
    def bfs(self, vertice1, vertice2):
        dist = [-1] * self.num_vertices  
        ant = [-1] * self.num_vertices  
        isVisited = [False] * self.num_vertices

        dist[vertice1] = 0
        isVisited[vertice1] = True

        Q = deque()
        Q.append(vertice1)

        while Q:
            p = Q.popleft()

            if p == vertice2:
                break

            for v in self.list[p]:
                if not isVisited[v]:
                    dist[v] = dist[p] + 1
                    ant[v] = p
                    Q.append(v)
                    isVisited[v] = True

        if dist[vertice2] == -1:
            print("Não há caminho de", vertice1, "para", vertice2)
        else:
            elementos = []
            v = vertice2
            while v != -1:
                elementos.append(v)
                v = ant[v]
    
            
            print("O melhor caminho é:", ' -> '.join(map(str, reversed(elementos))))
            print("Distância:", dist[vertice2])            

    #Busca em profundidade(usando pilha):
    def dfs(self, source):
        isVisited = [False] * self.num_vertices
        elementos = []
        pilha = []

        pilha.append(source)

        while pilha:
            v = pilha.pop()
            if not isVisited[v]:
                elementos.append(v)
                isVisited[v] = True

                for vizinho in self.list[v]:
                    if not isVisited[vizinho]:
                        pilha.append(vizinho)

        print(f'Os elementos do grafo são: {elementos}')



  



    