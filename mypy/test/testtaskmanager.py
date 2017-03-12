import time

from mypy.graph import Graph
from mypy.coordinator import Coordinator

DELAY = 1

class TestTask:
    def __init__(self, value):
        self.value = value

    def run(self):
        time.sleep(DELAY)
        t = time.time()
        return self.value, t

    def __repr__(self):
        return str(self.value)


def test_coordinator():
    g = Graph()
    nodes = [g.add_node(TestTask(i).run) for i in range(4)]
    g.add_edge(nodes[2], nodes[3])
    g.add_edge(nodes[1], nodes[3])
    g.add_edge(nodes[3], nodes[0])
    c = Coordinator(g, 4)
    results = c.run()
    v, t = zip(*results)
    assert {v[0], v[1]} == {1, 2}
    assert abs(t[1] - t[0]) < 0.1
    assert v[2] == 3
    assert abs(t[2] - t[1] - DELAY) < 0.1
    assert v[3] == 0
    assert abs(t[3] - t[2] - DELAY) < 0.1


if __name__ == '__main__':
    test_coordinator()