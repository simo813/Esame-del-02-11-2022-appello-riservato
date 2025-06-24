import flet as ft
import networkx as nx
from model.album import Album


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self.view = view
        # the model, which implements the logic of the program and holds the data
        self.model = model


    def fillDD(self):
        listGenres = self.model.passGenres()
        for genre in listGenres:
            self.view.ddGenre.options.append(ft.dropdown.Option(key=genre.GenreId, text=genre.Name))
        self.view.update_page()

    def handleCreaGrafo(self, e):
        if self.view.txtInMin.value is not None and self.view.txtInMax.value is not None and self.view.ddGenreValue is not None:
            try:
               tMin = int(self.view.txtInMin.value)
               tMax = int(self.view.txtInMax.value)
               genreId = int(self.view.ddGenreValue)
               genre = self.model.idMapGenres[genreId]
               if tMin >= genre.minD:
                   self.view.txt_result.clean()
                   self.model.createGraph(genreId, tMin, tMax)
                   graph = self.model.graph
                   self.view.txt_result.controls.append(ft.Text(
                       f"Grafo creato!\n"
                       f"# Vertici: {graph.number_of_nodes()}\n"
                       f"# Archi: {graph.number_of_edges()}\n"))
                   listConnectedComp = nx.connected_components(graph)



               else:
                   self.view.txt_result.clean()
                   self.view.txt_result.controls.append(ft.Text(
                       f"Inserisci un valore di minimo più grande di {genre.minD}"))

            except ValueError:
                self.view.txt_result.clean()
                self.view.txt_result.controls.append(ft.Text(
                    f"Inserisci un valore di minimo in formato secondi di tipo numerico"))
        else:
            self.view.txt_result.clean()
            self.view.txt_result.controls.append(ft.Text(
                f"Seleziona genere, tMin e tMax per creare un grafo"))

        self.view.update_page()


    def handleStampaAdiacenze(self, e):
       pass




    def handleMyPlaylist(self, e):
       pass



