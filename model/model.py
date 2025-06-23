import copy

from database.DAO import DAO
import networkx as nx
from model.album import Album


class Model:
    def __init__(self):
        self.optPathBilancio = None
        self.optPath = None
        self.DAO = DAO()
        self.graph = None
        self.listNodes = None
        self.idMapAlbum = {}


    def createGraph(self, canzoniN):
        pass


    def getOptPath(self, partenza, destinazione, soglia):
        self.optPath = []
        self.optPathBilancio = 0
        bilancioPartenza = self.findBilancio(partenza)
        print(partenza.AlbumId)
        print(destinazione.AlbumId)

        self.recursion(
            node = partenza,
            destinazione = destinazione,
            soglia = soglia,
            partial=[partenza],
            bilancioPartenza = bilancioPartenza,
            optPathBilancioP=0

        )
        print(self.optPath)
        print(self.optPathBilancio)
        print("\nFINE\n")

        return self.optPath

    def recursion(self, node, destinazione, soglia, partial, bilancioPartenza, optPathBilancioP):
        graph = self.graph

        if node.__eq__(destinazione):
            if optPathBilancioP > self.optPathBilancio:
                print("\n---------------------------------")
                print("aggiornamento self.optPathBilancio")
                print(optPathBilancioP)
                print(partial)
                self.optPathBilancio = optPathBilancioP
                self.optPath = copy.deepcopy(partial)

        for node, successor, data in graph.out_edges(node, data=True):
            if successor not in partial:
                weight = graph[node][successor]['weight']
                if weight > soglia:
                    print("successore valido")
                    bilancioSuccessor = self.findBilancio(successor)
                    if bilancioSuccessor > bilancioPartenza:
                        partial.append(successor)
                        self.recursion(successor, destinazione, soglia, partial, bilancioPartenza, optPathBilancioP + 1)
                        print("NUOVA RICORSIONE con aggiornamento optPathBilancioP\n")
                        partial.pop()
                    else:
                        partial.append(successor)
                        self.recursion(successor, destinazione, soglia, partial, bilancioPartenza, optPathBilancioP)
                        print("NUOVA RICORSIONE\n")
                        partial.pop()


    def findBilancio(self, node):
        graph = self.graph
        weightOutEdge = 0
        weightInEdge = 0

        for u, v, data in graph.out_edges(node, data=True):
            weightOutEdge += data.get('weight', 1)

        for u, v, data in graph.in_edges(node, data=True):
            weightInEdge += data.get('weight', 1)

        bilancio = weightInEdge - weightOutEdge
        return bilancio





