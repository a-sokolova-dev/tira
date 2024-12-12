"""
CSES-3182 Junien hinnat

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko14

Anna Sokolova • December 2024
"""


class FloydWarshall:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {}
        for a in self.nodes:
            for b in self.nodes:
                distance = 0 if a == b else float("inf")
                self.graph[(a, b)] = distance

    def add_edge(self, a, b, w):
        self.graph[(a, b)] = min(self.graph[(a, b)], w)

    def find_distances(self):
        distances = self.graph.copy()

        for k in self.nodes:
            for a in self.nodes:
                for b in self.nodes:
                    distance = min(distances[(a, b)],
                                   distances[(a, k)] +
                                   distances[(k, b)])
                    distances[(a, b)] = distance

        return distances


class TrainPrices:
    def __init__(self):
        self.cities = {}

    def add_city(self, name):
        self.cities[name] = []

    def add_train(self, city1, city2, price):
        self.cities[city1].append((city2, price))
        self.cities[city2].append((city1, price))

    def find_distances(self):
        # refactored to use Floyd-Warshall algorithm
        prices = {}
        f = FloydWarshall(sorted(list(self.cities.keys())))

        for city1, connections in self.cities.items():
            for city2, price in connections:
                f.add_edge(city1, city2, price)

        prices = f.find_distances()

        return prices

    def find_prices(self):
        prices = self.find_distances()

        table = [[None] + sorted(list(self.cities.keys()))]
        for city in sorted(self.cities):
            row = [city]
            for dest in sorted(list(self.cities.keys())):
                price = prices.get((city, dest), float("inf"))
                if price == float("inf"):
                    row.append(-1)
                else:
                    row.append(price)
            table.append(row)

        return table


if __name__ == "__main__":
    t = TrainPrices()

    t.add_city("Helsinki")
    t.add_city("Turku")
    t.add_city("Tampere")
    t.add_city("Oulu")

    t.add_train("Helsinki", "Tampere", 20)
    t.add_train("Helsinki", "Turku", 10)
    t.add_train("Tampere", "Turku", 50)

    print(t.find_prices())

    # metodin haluttu tulos:
    # [[None,       'Helsinki', 'Oulu', 'Tampere', 'Turku'],
    #  ['Helsinki', 0,          -1,     20,        10],
    #  ['Oulu',     -1,         0,      -1,        -1],
    #  ['Tampere',  20,         -1,     0,         30],
    #  ['Turku',    10,         -1,     30,        0]]
