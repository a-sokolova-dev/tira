"""
CSES-3188 Polut

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko13

Anna Sokolova • December 2024
"""


def create(x):
    points = [
        2 * index
        for index in range(1, x.bit_length() + 1)
        if x & (1 << (index - 1))
    ]

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
    print(create(2))  # esim. [(1,2), (1,100), (2,100)]
    print(create(5))
    print(create(10))
    print(create(123456789))
