class Airports:
    def __init__(self, n):
        self.airports = {}
        for i in range(n):
            self.airports[i+1] = []
        self.visited: set

    def add_link(self, a, b):
        self.airports[a].append(b)

    def visit(self, airport):
        if airport in self.visited:
            return

        self.visited.add(airport)

        for destination in self.airports[airport]:
            self.visit(destination)

    def check(self):
        for airport in self.airports:
            self.visited = set()
            self.visit(airport)
            if self.visited != set(self.airports):
                return False

        return True

if __name__ == "__main__":
    a = Airports(5)
    a.add_link(1, 2)
    a.add_link(2, 3)
    a.add_link(1, 3)
    a.add_link(4, 5)
    print(a.check()) # False
    a.add_link(3, 5)
    a.add_link(1, 4)
    print(a.check()) # False
    a.add_link(5, 1)
    print(a.check()) # True