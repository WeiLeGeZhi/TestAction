import heapq

def dijkstra(graph, start, end):
    # 使用堆实现优先队列
    heap = [(0, start)]
    visited = set()

    while heap:
        (cost, current) = heapq.heappop(heap)

        if current in visited:
            continue

        visited.add(current)

        if current == end:
            return cost

        for neighbor, neighbor_cost in graph[current]:
            heapq.heappush(heap, (cost + neighbor_cost, neighbor))

    return -1

def main():
    n, m = map(int, input().split())

    graph = {i: [] for i in range(1, n + 1)}

    for _ in range(m):
        x, y, z = map(int, input().split())
        graph[x].append((y, z))

    result = dijkstra(graph, 1, n)

    print(result)

if __name__ == "__main__":
    main()