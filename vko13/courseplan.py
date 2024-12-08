class CoursePlan:
    def __init__(self):
        self.courses = {}
        self.state = {}
        self.order = []
        self.cycle = False

    def add_course(self, course):
        self.courses[course] = []

    def add_requisite(self, course1, course2):
        self.courses[course1].append(course2)

    def visit(self, course):
        if self.state[course] == 1:
            self.cycle = True
            return
        if self.state[course] == 2:
            return

        self.state[course] = 1
        for next_course in self.courses[course]:
            self.visit(next_course)

        self.state[course] = 2
        self.order.append(course)

    def find_order(self):
        self.state = {}
        for course in self.courses:
            self.state[course] = 0
        self.order = []
        self.cycle = False

        for course in self.courses:
            if self.state[course] == 0:
                self.visit(course)

        if self.cycle:
            return None
        else:
            self.order.reverse()
            return self.order


if __name__ == "__main__":
    c = CoursePlan()
    c.add_course("Ohpe")
    c.add_course("Ohja")
    c.add_course("Tira")
    c.add_course("Jym")
    c.add_requisite("Ohpe", "Ohja")
    c.add_requisite("Ohja", "Tira")
    c.add_requisite("Jym", "Tira")
    print(c.find_order()) # esim. [Ohpe, Jym, Ohja, Tira]
    c.add_requisite("Tira", "Tira")
    print(c.find_order()) # None