from unittest import TestCase
from fuzze.fuzzers import *


class TestCost(TestCase):

    def test_eq(self):
        cost = Cost(1)
        self.assertEqual(cost, Cost(1))
        self.assertNotEqual(cost, Cost(2))

        cost = Cost.inf()
        self.assertEqual(cost, Cost.inf())
        self.assertNotEqual(cost, Cost(1))

    def test_gt(self):
        cost = Cost(1)
        self.assertGreater(cost, 0)
        self.assertGreater(cost, Cost(0))

        self.assertGreater(Cost.inf(), 0)
        self.assertGreater(Cost.inf(), Cost(0))

        self.assertGreaterEqual(cost, 0)
        self.assertGreaterEqual(cost, Cost(0))
        self.assertGreaterEqual(cost, 1)

        self.assertGreaterEqual(Cost.inf(), cost)
        self.assertGreaterEqual(Cost.inf(), 0)
        self.assertGreaterEqual(Cost.inf(), Cost.inf())

    def test_lt(self):
        cost = Cost(1)
        self.assertLess(cost, 2)
        self.assertLess(cost, Cost(2))

        self.assertLess(0, Cost.inf())
        self.assertLess(Cost(0), Cost.inf())

        self.assertLessEqual(cost, 2)
        self.assertLessEqual(cost, Cost(2))
        self.assertLessEqual(cost, 1)

        self.assertLessEqual(0, Cost.inf())
        self.assertLessEqual(Cost(0), Cost.inf())
        self.assertLessEqual(Cost.inf(), Cost.inf())

    def test_add(self):
        cost = Cost(1)
        self.assertEqual(cost + 1, Cost(2))

        cost = Cost.inf()
        self.assertEqual(cost + 1, Cost.inf())

        self.assertEqual(cost + Cost.inf(), Cost.inf())

    def test_sub(self):
        cost = Cost(1)
        self.assertEqual(cost - 1, Cost(0))

        cost = Cost.inf()
        self.assertEqual(cost - 1, Cost.inf())

        assert cost == Cost.inf()
        with self.assertRaises(NotImplementedError):
            _ = cost - Cost.inf()

    def test_mul(self):
        cost = Cost(1)
        self.assertEqual(cost * 2, Cost(2))

        cost = Cost.inf()
        self.assertEqual(cost * 2, Cost.inf())

        assert cost == Cost.inf()
        self.assertEqual(cost * Cost.inf(), Cost.inf())

    def test_div(self):
        cost = Cost(1)
        self.assertEqual(cost / 2, Cost(0))
        self.assertEqual(cost / Cost.inf(), Cost(0))
        self.assertEqual(cost / 0, Cost.inf())

        cost = Cost.inf()
        self.assertEqual(cost / 2, Cost.inf())
        self.assertEqual(cost / 0, Cost.inf())

        with self.assertRaises(NotImplementedError):
            _ = cost / Cost.inf()

    def test_radd(self):
        cost = Cost(1)
        self.assertEqual(1 + cost, Cost(2))

    def test_rsub(self):
        cost = Cost(1)
        self.assertEqual(2 - cost, Cost(1))

        cost = Cost.inf()
        with self.assertRaises(NotImplementedError):
            _ = 2 - cost

    def test_rdiv(self):
        cost = Cost(2)
        self.assertEqual(4 / cost, Cost(2))

        cost = Cost.inf()
        self.assertEqual(2 / cost, Cost(0))

        with self.assertRaises(NotImplementedError):
            _ = Cost.inf() / Cost.inf()
