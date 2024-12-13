"""
CSES-3209 Ruudukko

Please see my GitHub repository for used theory references and writeups:
https://github.com/a-sokolova-dev/tira/tree/main/vko16

Anna Sokolova • December 2024
"""


def count(r):
    # solved this with dfs since it's a more familiar approach to me
    # similar to N-Queens, Maximum Number of Accepted Invitations

    matches = {}
    rows = len(r)
    cols = len(r[0])

    def dfs(row, visited):
        for col in range(cols):
            if r[row][col] == "X" and col not in visited:
                visited.add(col)
                if col not in matches or dfs(matches[col], visited):
                    matches[col] = row
                    return True
        return False

    for row in range(rows):
        dfs(row, set())
    return len(matches)


if __name__ == "__main__":
    r = ["........",
         "........",
         "...X..X.",
         "........",
         "....X...",
         "..X.X..X",
         "........",
         "....X..."]
    print(count(r))  # 3
