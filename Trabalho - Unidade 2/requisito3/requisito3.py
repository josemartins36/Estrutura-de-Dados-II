import networkx as nx
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


class CSVFileReader:
    def __init__(self, filename):
        self.filename = filename

    def load_csv(self):
        """Lê o arquivo CSV e retorna um DataFrame."""
        return pd.read_csv(self.filename)

class CoauthorshipGraph:
    def __init__(self, df):
        self.df = df
        self.G = nx.Graph()

    def create_graph(self):
        """Constrói um grafo com autores como nós e coautorias como arestas."""
        for _, row in self.df.iterrows():
            authors = row["Authors"].split("; ")
            for i, author1 in enumerate(authors):
                for author2 in authors[i + 1 :]:
                    if not self.G.has_edge(author1, author2):
                        self.G.add_edge(author1, author2, weight=1)
        return self.G


class GraphMetricsAnalyzer:
    def __init__(self, graph):
        self.graph = graph

    def calculate_metrics(self):
        """Analisa o grafo e retorna um dicionário com várias métricas."""
        metrics = {
            "qtd_vertices": self.graph.number_of_nodes(),
            "qtd_arestas": self.graph.number_of_edges(),
            "degree_assortativity_coefficient": nx.degree_assortativity_coefficient(self.graph),
            "qtd_comp_conectados": nx.number_connected_components(self.graph),
            "tam_comp_gigante": len(max(nx.connected_components(self.graph), key=len)),
            "avg_clustering": nx.average_clustering(self.graph),
        }
        return metrics


def main():
    """Alterar a ODS.csv"""
    csv_file = "ods_11.csv"

    read = CSVFileReader(csv_file)
    csv = read.load_csv()

    """Construindo o grafo"""
    graph_constr = CoauthorshipGraph(csv)
    netw_Graph = graph_constr.create_graph()

    """Analisando a rede"""
    calc_graph = GraphMetricsAnalyzer(netw_Graph)
    calc_results = calc_graph .calculate_metrics()

    """Imprimindo os resultados da análise"""
    print(f"Qtd vértices: {calc_results['qtd_vertices']}")
    print(f"Qtd arestas: {calc_results['qtd_arestas']}")
    print(f"Degree assortativity coefficient: {calc_results['degree_assortativity_coefficient']}")
    print(f"Qtd_comp_conectados: {calc_results['qtd_comp_conectados']}")
    print(f"Tamanho do comp. gigante: {calc_results['tam_comp_gigante']}")
    print(f"Coef. de Clustering: {calc_results['avg_clustering']}")

if __name__ == "__main__":
    main()
