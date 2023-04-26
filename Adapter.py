from typing import Dict, List
from abc import ABC, abstractmethod

class CsvPlotter:
    def plot_data(self, data: Dict[str, List]) -> None:
        # Implementación para graficar utilizando la librería csvplotter
        pass

class CsvPlotterAdapter():
    #metodo abstracto
    @abstractmethod
    def plot_data(csv_data):
        return "Image"
    
    def __init__(self, csv_plotter: CsvPlotter) -> None:
        self.csv_plotter = csv_plotter

    def get_countries_data(countries):
        pass

    def get_countries_historic_data(countries,start_date,end_date):
        pass


class App:
    def show_graph(self, data: Dict[str, List]) -> None:
        self.graph_generator.generate_graph(data)

class CovidDataServices:
    def get_countries_data(countries):
        pass

    def get_countries_historic_data(countries,start_date,end_date):
        pass

if __name__ == "__main__":
    data_service = CovidDataServices()
    csv_plotter = CsvPlotter()
    csv_plotter_adapter = CsvPlotterAdapter(csv_plotter)
    app = App(csv_plotter_adapter)
    data = data_service.get_countries_data('Colombia')
    app.show_graph(data)