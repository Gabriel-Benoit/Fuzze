from unittest import TestCase
from fuzze.grammars import *


class TestGrammarClass(TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        super().setUpClass()
        cls.exemple_grammar: GrammarDict = {
            "<noun>": ["cat", "dog"],
            "<verb>": ["eats", "sleeps", "sits"],
            "<article>": ["The", "A"],
            "<sentence>": [
                "<article> <noun> <verb>",
            ],
        }

    def is_param_exp_equal(
        self, pe1: types.Parametrized_Expansion, pe2: types.Parametrized_Expansion
    ):
        if pe1[0] != pe2[0]:
            return False
        if len(pe1[1]) != len(pe2[1]):
            return False
        for k1 in pe1[1].keys():
            if k1 not in pe2[1]:
                return False
            if pe1[1][k1] != pe2[1][k1]:
                return False
        return True

    def is_equal(self, g1: types.GrammarDict, g2: types.GrammarDict):
        if len(g1) != len(g2):
            return False
        for key in g1.keys():
            if key not in g2:
                return False
            if g1[key] != g2[key]:
                return False

        return True

    def test_grammar_init(self):
        with self.assertRaises(AssertionError):
            Grammar(grammar={})

        with self.assertRaises(AssertionError):
            Grammar(grammar={"S": []}, start_symbol="Det")

    def test_merge(self):
        g1 = Grammar(self.exemple_grammar)
        g2 = Grammar(
            {
                "<noun>": ["parrot", "panda"],
            }
        )

        result: GrammarDict = g1.merge_with(g2).grammar  # type: ignore
        expected_result: GrammarDict = {
            "<noun>": ["cat", "dog", "parrot", "panda"],
            "<verb>": ["eats", "sleeps", "sits"],
            "<article>": ["The", "A"],
            "<sentence>": [
                "<article> <noun> <verb>",
            ],
        }
        self.assertTrue(self.is_equal(result, expected_result))
