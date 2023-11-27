def main():
    with open('case/1.in', 'r') as file:
        n, m = map(int, file.readline().split())

        graph = {i: [] for i in range(1, n + 1)}

        for _ in range(m):
            x, y, z = map(int, file.readline().split())
            graph[x].append((y, z))

    print(graph)

if __name__ == "__main__":
    main()