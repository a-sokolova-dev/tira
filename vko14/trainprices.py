import heapq

class TrainPrices:
    def __init__(self):
        self.cities = {}

    def add_city(self, name):
        self.cities[name] = []

    def add_train(self, city1, city2, price):
        self.cities[city1].append((city2, price))
        self.cities[city2].append((city1, price))

    def find_prices_by_city(self, start):
        prices = {}
        for city in self.cities:
            prices[city] = float("inf")
        prices[start] = 0

        queue = []
        heapq.heappush(queue, (0, start))

        visited = set()
        while queue:
            a = heapq.heappop(queue)[1]
            if a in visited:
                continue
            visited.add(a)

            for b, price in self.cities[a]:
                new_price = prices[a] + price
                if new_price < prices[b]:
                    prices[b] = new_price
                    new_pair = (new_price, b)
                    heapq.heappush(queue, new_pair)

        return prices


    def find_prices(self):
        prices = {}
        for city in self.cities:
            prices[city] = self.find_prices_by_city(city)

        table = [[None] + sorted(self.cities)]
        for city in sorted(self.cities):
            row = [city]
            for dest in sorted(self.cities):
                price = prices[city][dest]
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