import unittest
from fuzze.grammars.types import Node


class TestNode(unittest.TestCase):

    def setUp(self) -> None:
        super().setUp()
        self.node_1 = Node("root", [Node("child1", [Node("child2")])])
        self.node_2 = Node("root")
        self.node_3 = Node("root", [self.node_1, self.node_2])

    def test_node_depth(self):
        self.assertEqual(self.node_1.depth(), 3)
        self.assertEqual(self.node_2.depth(), 0)
        self.assertEqual(self.node_3.depth(), 3)

    def test_node_to_string(self):
        self.assertEqual(self.node_1.toString(), "Root, Child 1, Child 2")
        self.assertEqual(self.node_2.toString(), "root")
        self.assertEqual(self.node_3.toString(), "rootrootChild 1, Child 2")
