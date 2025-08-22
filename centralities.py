import networkx as nx
import pandas as pd

def calculate_centralities(G):
    """Calcula as principais centralidades do grafo."""
    deg = nx.degree_centrality(G)
    bet = nx.betweenness_centrality(G)
    clo = nx.closeness_centrality(G)
    eig = nx.eigenvector_centrality(G)
    return deg, bet, clo, eig

def centralities_dataframe(G):
    """Cria um DataFrame com todas as centralidades."""
    deg, bet, clo, eig = calculate_centralities(G)
    df = pd.DataFrame({
        'Personagem': list(G.nodes()),
        'Grau': [deg[n] for n in G.nodes()],
        'Intermediação': [bet[n] for n in G.nodes()],
        'Proximidade': [clo[n] for n in G.nodes()],
        'Vetor Próprio': [eig[n] for n in G.nodes()]
    })
    df = df.sort_values(by='Grau', ascending=False)  # opcional: ordenar por grau
    return df
