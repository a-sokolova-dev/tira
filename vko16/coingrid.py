def count(r):
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
