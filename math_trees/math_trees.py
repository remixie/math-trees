"""Main module."""

from collections import deque
from textwrap import wrap

order = {"*": 1, "/": 1, "+": 2, "-": 2, "(": 3}

# In order to turn the given infix expression into an expression tree,
# it's best to convert it to a postfix first


def convertToPostfix(infix):
    stack = deque()
    postfix = ''

    infix = infix.split(' ')

    for char in infix:

        # Step 5: Make the string parser from step 3 handle parentheses ()
        if char == '(':  # add ( to the stack to recursively search for characters inside parentheses
            stack.append(char)

        # begin adding values to postfix and remove from the stack
        elif char == ')':
            while stack[-1] != '(':
                postfix += stack.pop() + " "
            stack.pop()

        # if the current character is not an operator
        elif char not in order.keys():
            postfix += char + " "

        # if the current character IS an operator
        else:
            while stack and order[char] >= order[stack[-1]]:
                postfix += stack.pop() + " "

            stack.append(char)

    while stack:
        postfix += stack.pop() + " "

    return postfix.strip()


class Node:
    def __init__(self, value):
        self.value = value
        self.children = [None, None]

    def __str__(self):
        return self.value


# Step 1: Create a data structure which can represent math expressions
def makeExpressionTree(postfix):
    root = None
    stack = []

    postfix = postfix.split(' ')

    for char in postfix:
        if char not in order:
            stack.append(Node(char))

        else:
            node = Node(char)
            node.children[1] = stack.pop()
            node.children[0] = stack.pop()
            stack.append(node)

        root = stack[-1]
    # return the root so you can begin traversing the tree
    return root


def evaluate(root):  # Step 2: Implement an evaluation method which calculates the value of the expression
    val = root.value
    if val not in order:
        return int(val)

    else:
        left, right = evaluate(root.children[0]), evaluate(root.children[1])
        return eval(str(left)+val+str(right))


# Step 3: Write a parser which converts an ascii string to your data structure.
# In order to turn the ascii to an expression tree, I have to convert the ascii to infix first
def asciiToInfix(ascii):
    is_binary = " " not in ascii
    infix = ""
    if is_binary:
        ascii = wrap(ascii, 8)
    else:
        ascii = [int(a) for a in ascii.split(" ")]
    for byte in ascii:
        if is_binary:
            byte = int(byte, 2)
        infix += chr(byte)

    return infix


# Step 4: Implement a __str__ method which converts your data structure into an ascii string equivalent
def treeToString(root):  # first turn the tree into a regular string
    st = ""
    if root.children[0]:
        st += treeToString(root.children[0]) + " "

    st += str(root)  # use the built in __str__ method of the class Node

    if root.children[1]:
        st += " "+treeToString(root.children[1])

    return st


# turn the string into binary or decimal depending on the to_binary flag
def stringToAscii(st, to_binary=True):

    if to_binary:
        return ''.join(format(ord(x), '08b') for x in st)
    else:
        return ' '.join(format(ord(x)) for x in st)
