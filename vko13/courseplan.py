"""
CSES-3184 Kurssisuunnitelma

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko13

Anna Sokolova • December 2024
"""


class TopologicalSort:
    def __init__(self, nodes):
        self.nodes = nodes
        self.graph = {node: [] for node in self.nodes}

    def add_edge(self, a, b):
        self.graph[a].append(b)

    def visit(self, node):
        if self.state[node] == 1:
            self.cycle = True
            return
        if self.state[node] == 2:
            return

        self.state[node] = 1
        for next_node in self.graph[node]:
            self.visit(next_node)

        self.state[node] = 2
        self.order.append(node)

    def create(self):
        self.state = {}
        for node in self.nodes:
            self.state[node] = 0

        self.order = []
        self.cycle = False

        for node in self.nodes:
            if self.state[node] == 0:
                self.visit(node)

        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order


class CoursePlan:
    # refactored to use TopologicalSort as per course material
    # and not the bruteforce course chain approach

    def __init__(self):
        self.courses = []
        self.edges = []

    def add_course(self, course):
        self.courses.append(course)

    def add_requisite(self, course1, course2):
        self.edges.append((course1, course2))

    def find_order(self):
        t = TopologicalSort(self.courses)
        for course1, course2 in self.edges:
            t.add_edge(course1, course2)
        return t.create()


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe", "Ohja")
    c.add_requisite("Ohja", "Tira")
    c.add_requisite("Jym", "Tira")
    print(c.find_order())  # esim. [Ohpe, Jym, Ohja, Tira]
    c.add_requisite("Tira", "Tira")
    print(c.find_order())  # None
