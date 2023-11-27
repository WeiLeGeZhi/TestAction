const { expect } = require('chai');
const { dijkstra } = require('./dijkstra.py');  // 替换成你的实际代码文件路径

describe('Dijkstra Algorithm', () => {
  it('Case 1', () => {
    const graph = {
      1: [(2, 351), (5, 585), (1, 279)],
      2: [(5, 194), (2, 721), (2, 249)],
      3: [(5, 935), (1, 566)],
      4: [(1, 999)],
      5: [(5, 818)],
    };

    const result = dijkstra(graph, 1, 5);
    expect(result).to.equal(545);
  });

  it('Case 2', () => {
    const graph = {
      1: [(1, 46), (4, 611), (6, 276)],
      2: [],
      3: [(10, 910)],
      4: [(10, 559)],
      5: [(5, 277)],
      6: [],
      7: [],
      8: [(10, 124)],
      9: [(8, 478)],
      10: [(8, 679), (6, 707)],
    };

    const result = dijkstra(graph, 1, 10);
    expect(result).to.equal(1170);
  });
});
