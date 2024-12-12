"""
CSES-3186 Lentokentät

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko13

Anna Sokolova • December 2024
"""


class Airports:
    # could also be solved using Kosaraju's algorithm
    # from the course material

    def __init__(self, n):
        self.airports = {}
        for i in range(n):
            self.airports[i+1] = []

        self.reverse = {}
        for i in range(n):
            self.reverse[i+1] = []

        self.visited: set

    def add_link(self, a, b):
        self.airports[a].append(b)
        self.reverse[b].append(a)

    def visit(self, airport):
        if airport in self.visited:
            return

        self.visited.add(airport)

        for d in self.airports[airport]:
            self.visit(d)

    def check(self):
        for airport in self.airports:
            self.visited = set()
            self.visit(airport)
            if len(self.visited) != len(self.airports):
                return False

        return True


if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1, 2)
    a.add_link(2, 3)
    a.add_link(1, 3)
    a.add_link(4, 5)
    print(a.check())  # False
    a.add_link(3, 5)
    a.add_link(1, 4)
    print(a.check())  # False
    a.add_link(5, 1)
    print(a.check())  # True
