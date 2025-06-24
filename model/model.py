import copy

from database.DAO import DAO
import networkx as nx
from model.album import Album


class Model:
    def __init__(self):
        self.sumDuration = None
        self.optPath = None
        self.DAO = DAO()
        self.graph = None
        self.listNodes = None
        self.idMapGenres = {}

    def passGenres(self):
        listGenres  = self.DAO.getGenres()
        for genre in listGenres:
            self.idMapGenres[genre.GenreId] = genre
        return listGenres



    def createGraph(self, genreId, tMin, tMax):
        self.graph = nx.Graph()
        listNodes = self.DAO.getNodes(genreId, tMin, tMax)
        self.graph.add_nodes_from(listNodes)
        for track1 in listNodes:
            for track2 in listNodes:
                if track1.nPlaylist == track2.nPlaylist and track1.TrackId != track2.TrackId and track1.TrackId > track2.TrackId:
                    self.graph.add_edge(track1, track2)



    def getOptPath(self, dTot):
        self.optPath = []
        self.sumDuration = 0
        largest_cc = max(nx.connected_components(self.graph), key=len)

        for node in largest_cc:
            partial = [node]
            print("Inizio ricorsione")
            self.recursion(
                node = node,
                largest_cc = largest_cc,
                partial= partial,
                partialDuration=node.duration,
                dTot=dTot
            )
            partial.pop()
        print(self.sumDuration)
        print(self.optPath)
        print("\nFINE\n")

        return self.optPath

    def recursion(self, node, largest_cc, partial, partialDuration, dTot):

        if len(partial) > len(self.optPath):
            print("\n---------------------------------")
            print("aggiornamento self.sumDuration")
            print(partial)
            self.sumDuration = partialDuration
            self.optPath = copy.deepcopy(partial)

        for node in largest_cc:
            durationN = node.duration
            if node not in partial and durationN + partialDuration <= (dTot * 60):
                print("node valido")
                partial.append(node)
                self.recursion(node, largest_cc, partial, durationN + partialDuration , dTot)
                print("NUOVA RICORSIONE")
                partial.pop()
            else:
                print("nodo non valido")
                return






