#!/usr/bin/env python

import unittest

from math_trees.math_trees import convertToPostfix, makeExpressionTree, evaluate, asciiToInfix, treeToString, stringToAscii


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

    def test_standalone_operand(self):
        math_string = "10"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        answer = evaluate(tree)
        self.assertEqual(answer, 10)

    def test_floating_point(self):
        math_string = "1.23 - 3.21"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        answer = evaluate(tree)
        self.assertEqual(answer, -1.98)

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

    def test_tree_to_binary_ascii(self):
        math_string = "20 / 10 * 14 + 2"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        st = treeToString(tree)
        ascii = stringToAscii(st)
        self.assertEqual(
            ascii, "00110010001100000010000000101111001000000011000100110000001000000010101000100000001100010011010000100000001010110010000000110010")

    def test_tree_to_decimal_ascii(self):
        math_string = "20 / 10 * 14 + 2"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        st = treeToString(tree)
        ascii = stringToAscii(st, False)
        self.assertEqual(
            ascii, "50 48 32 47 32 49 48 32 42 32 49 52 32 43 32 50")

    def test_parenthesis_in_tree(self):
        math_string = "20 / 10 * ( ( 1 + 3 ) + 2 )"
        postfix = convertToPostfix(math_string)
        tree = makeExpressionTree(postfix)
        st = treeToString(tree)
        ascii = stringToAscii(st, False)
        self.assertEqual(
            ascii, "50 48 32 47 32 49 48 32 42 32 40 32 40 32 49 32 43 32 51 32 41 32 43 32 50 32 41")
