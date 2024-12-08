def create(x):
    points = []

    i = 1
    while x > 0:
        if x % 2:
            points.append(i * 2)
        i += 1
        x //= 2

    edges = [(1, 2)]

    i = 0
    while i < points[-1]:
        i += 2
        edges.append((i, i + 2))
        edges.append((i, i + 1))
        edges.append((i + 1, i + 2))
        if i in points:
            edges.append((i, 100))

    return edges

if __name__ == "__main__":
    print(create(2)) # esim. [(1,2), (1,100), (2,100)]
    print(create(5))
    print(create(10))
    print(create(123456789))
    