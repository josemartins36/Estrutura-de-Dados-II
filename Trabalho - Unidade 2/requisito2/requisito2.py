import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import seaborn as sns


class CSVFileReader:
    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.df = None

    def load_csv(self):
        """Lê o arquivo CSV e retorna um DataFrame."""
        self.df = pd.read_csv(self.csv_file)
        return self.df


class CoauthorshipGraph:
    def __init__(self, df):
        self.df = df
        self.G = nx.Graph()

    def create_graph(self):
        """Builds a graph where nodes are authors and edges represent co-authorship."""
        for _, row in self.df.iterrows():
            authors_id = row["Author(s) ID"].split("; ")
            authors = row["Authors"].split("; ")
            affiliations = row["Affiliations"].split("; ")

            authors_information = list(zip(authors_id, authors, affiliations))

            for index, (id_1, name_1, affiliation_1) in enumerate(authors_information):
                if not self.G.has_node(id_1):
                    self.G.add_node(id_1, name=name_1, affiliation=affiliation_1)

                for id_2, name_2, affiliation_2 in authors_information[index + 1 :]:
                    if not self.G.has_node(id_2):
                        self.G.add_node(id_2, name=name_2, affiliation=affiliation_2)

                    if not self.G.has_edge(id_1, id_2):
                        self.G.add_edge(id_1,id_2,weight=1,)
        return self.G


class GraphPlotter:
    def __init__(self, graph):
        self.graph = graph

    def plot(self):
        """Plota a assortatividade do grafo e salva como uma imagem."""

        """Calcula os graus dos nós e o médio dos vizinhos"""
        degrees = dict(self.graph.degree())
        avg_neighbor_degrees = nx.average_neighbor_degree(self.graph)

        data = {
            "Grau do nó": list(degrees.values()),
            "Grau médio de vizinhança": list(avg_neighbor_degrees.values()),
        }
        df = pd.DataFrame(data)

        plt.figure(figsize=(6, 6))
        sns.regplot(
            x="Grau do nó",
            y="Grau médio de vizinhança",
            data=df,
            scatter_kws={"s": 40}
        )

        """ativando layout de grid"""
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("ods_x.png")

"""Processamento e construção do grafo"""
def main() -> None:
    """Alterar a ODS.csv"""
    csv_file = "ods_11.csv"

    data_processor = CSVFileReader(csv_file)
    df = data_processor.load_csv()

    graph_builder = CoauthorshipGraph(df)
    G = graph_builder.create_graph()

    """Exposição do plot"""
    visualizer = GraphPlotter(G)
    visualizer.plot()


if __name__ == "__main__":
    main()
