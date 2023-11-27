import unittest
from src.dijkstra import dijkstra

class TestDijkstra(unittest.TestCase):
    def test(self):
        graph = {1: [(2, 351), (5, 585), (1, 279)], 2: [(5, 194), (2, 721), (2, 249)], 3: [(5, 935), (1, 566)], 4: [(1, 999)], 5: [(5, 818)]}
        n = 5
        result = dijkstra(graph, 1, n)
        self.assertEqual(result, 545)

        graph = {1: [(1, 46), (4, 611), (6, 276)], 2: [], 3: [], 4: [(10, 559)], 5: [(5, 277)], 6: [], 7: [(3, 910)], 8: [(10, 124)], 9: [(8, 478)], 10: [(8, 679), (6, 707)]}
        n = 10
        result = dijkstra(graph, 1, n)
        self.assertEqual(result, 1170)

if __name__ == '__main__':
    unittest.main()
