import matplotlib.pyplot as plt
from network_data import les_miserables_graph
from centralities import centralities_dataframe

# Criando o grafo
G = les_miserables_graph()

# Gerando tabela de centralidades
df = centralities_dataframe(G)

# Exibindo as 10 primeiras linhas
print(df.head(10))

# Opcional: salvar em CSV
df.to_csv("centralidades_les_miserables.csv", index=False)

# ---------------------------
# Visualização do grafo (opcional)
# ---------------------------
import networkx as nx

plt.figure(figsize=(18, 18))
pos = nx.spring_layout(G, seed=42, k=0.5)

# Destacar top 5 por Grau
top_nodes = df.head(5)['Personagem'].tolist()
node_sizes = [1500 if n in top_nodes else 500 for n in G.nodes()]
node_colors = ['red' if n in top_nodes else 'skyblue' for n in G.nodes()]

nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=node_colors, alpha=0.9)
nx.draw_networkx_edges(G, pos, alpha=0.2, width=1)
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

plt.title("Grafo de Coaparição de Personagens - Les Misérables", fontsize=18)
plt.axis('off')
plt.show()
