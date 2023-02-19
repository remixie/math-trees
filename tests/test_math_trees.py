#!/usr/bin/env python

import unittest

from math_trees.math_trees import convertToPostfix, makeExpressionTree, evaluate, asciiToInfix


class TestMathTrees(unittest.TestCase):
    def test_add_and_mult(self):
        math_string = "3 + 4 * 2"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        answer = evaluate(tree)
        self.assertEqual(answer, 11)

    def test_multiple_digits(self):
        math_string = "3 + 14 * 2"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        answer = evaluate(tree)
        self.assertEqual(answer, 31)

    def test_sub_and_divide(self):
        math_string = "8 - 9 / 3"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        answer = evaluate(tree)
        self.assertEqual(answer, 5)

    def test_binary_ascii(self):
        # 8 + 11 / 3
        binary_ascii = "00111000001000000010101100100000001100010011000100100000001011110010000000110011"
        math_string = asciiToInfix(binary_ascii)
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        # check if the tree was made correctly for step 3
        self.assertEqual(tree.value, "+")

    def test_decimal_ascii(self):
        # ( 2 + 2 ) / ( 6 - 10 )
        decimal_ascii = "40 32 50 32 43 32 50 32 41 32 47 32 40 32 54 32 45 32 49 48 32 41"
        math_string = asciiToInfix(decimal_ascii)
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        # check if the tree was made correctly for step 3
        self.assertEqual(tree.value, "/")
