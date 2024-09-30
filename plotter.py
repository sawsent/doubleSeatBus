import matplotlib.pyplot as plt

def plot_graph(data):
    plt.plot(list(data.keys()), list(data.values()))
    plt.show()
