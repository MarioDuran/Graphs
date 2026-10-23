"""Checks data loading, not students' algorithms or the mystery's answer."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from starter import load_case


class DatasetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.case = load_case()

    def test_counts(self):
        self.assertEqual((len(self.case.stations), len(self.case.roads),
                          len(self.case.conflict_edges), len(self.case.pipes),
                          len(self.case.checkpoints)), (196, 690, 1000, 689, 12))

    def test_undirected_roads(self):
        for a, b, travel, cost in self.case.roads:
            self.assertIn((b, travel), self.case.travel_graph[a])
            self.assertIn((a, travel), self.case.travel_graph[b])
            self.assertIn((b, cost), self.case.cable_graph[a])
            self.assertIn((a, cost), self.case.cable_graph[b])

    def test_directed_pipes(self):
        for a, b, capacity in self.case.pipes:
            self.assertIn((b, capacity), self.case.pipe_graph[a])
        self.assertIn("SOURCE", self.case.pipe_graph)
        self.assertIn("OUTLET", self.case.pipe_graph)


if __name__ == "__main__":
    unittest.main()
