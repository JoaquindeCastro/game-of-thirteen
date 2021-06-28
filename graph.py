import matplotlib.pyplot as plt
from simulation import Simulation
from utils.math import factorial, derangement
from math import e

class Graph(Simulation):

    def __init__(self, cards, num_of_sims, min, max):
        self.min = min
        self.max = max
        super().__init__(cards, num_of_sims)

    def plot(self):
        min, max = self.min, self.max
        x = list(range(min, max+1))
        y = [self.run_for_cards(n) for n in x]
        plt.plot(x, y, 'r')
        actual = [derangement(n)/factorial(n) for n in x]
        plt.plot(x, actual, 'b')
        estimate = [1/e for _ in x]
        plt.plot(x, estimate, 'y')
        plt.xlabel("Number of Cards")
        plt.ylabel("Probability of winning")
        plt.ylim(1)
        plt.axis((min-1,max,0,1))
        plt.show()

if __name__ == "__main__":
    graph = Graph(13, 1200, 1, 20)
    graph.plot()