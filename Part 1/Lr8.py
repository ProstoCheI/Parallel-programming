import networkx as nx
import matplotlib.pyplot as plt


def build_strassen_graph(depth, node_id=0):
    """Строит дерево рекурсии Штрассена (7 ветвлений)"""
    G = nx.Graph()
    current_node = node_id
    if depth > 0:
        for i in range(7):
            child_id = node_id * 10 + i + 1
            G.add_edge(current_node, child_id)
            G.update(build_strassen_graph(depth - 1, child_id))
    return G


def build_fft_butterfly_graph(n):
    """Строит граф 'бабочка' для БПФ"""
    G = nx.DiGraph()
    import math
    layers = int(math.log2(n))

    for layer in range(layers + 1):
        for i in range(n):
            G.add_node((layer, i))

    for layer in range(layers):
        step = 2 ** layer
        for i in range(0, n, 2 * step):
            for j in range(step):
                # Связи 'бабочки'
                idx1, idx2 = i + j, i + j + step
                # Прямые и перекрестные связи
                G.add_edge((layer, idx1), (layer + 1, idx1))
                G.add_edge((layer, idx2), (layer + 1, idx2))
                G.add_edge((layer, idx1), (layer + 1, idx2))
                G.add_edge((layer, idx2), (layer + 1, idx1))
    return G


# --- ВИЗУАЛИЗАЦИЯ ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Граф Штрассена (глубина 2 для наглядности)
strassen = build_strassen_graph(2)
pos_s = nx.spring_layout(strassen)
nx.draw(strassen, pos_s, ax=ax1, node_size=30, node_color='skyblue', with_labels=False)
ax1.set_title("Граф рекурсии Штрассена (Дерево)")

# Граф БПФ (n=8)
n_fft = 8
fft = build_fft_butterfly_graph(n_fft)
pos_f = {node: (node[0], -node[1]) for node in fft.nodes()}
nx.draw(fft, pos_f, ax=ax2, node_size=50, node_color='salmon', edge_color='gray', arrowsize=10)
ax2.set_title("Граф БПФ (Сеть 'Бабочка')")

plt.show()