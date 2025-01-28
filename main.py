# DO NOT MODIFY THE NODE CLASS!
class Node:

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        

def convert(tree):
    # Your solution here!
    pass


r"""
       d
      / \
     e   v
"""
tree = Node("d", Node("e"), Node("v"))
assert convert(tree) == {
    "d": ("e", "v"),
    "e": (None, None),
    "v": (None, None),
}

r"""
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
"""
tree = Node("a", Node("x", Node("e"), Node("m")), Node("y", None, Node("p")))
assert convert(tree) == {
    "a": ("x", "y"),
    "x": ("e", "m"),
    "y": (None, "p"),
    "e": (None, None),
    "m": (None, None),
    "p": (None, None),
}

r"""
           g
         /   \
        /     \
       e       f
      /         \
     k           d
    /             \
   w               z
"""
tree = Node("g", Node("e", Node("k", Node("w"))), Node("f", None, Node("d", None, Node("z"))))
assert convert(tree) == {
    "g": ("e", "f"),
    "e": ("k", None),
    "k": ("w", None),
    "w": (None, None),
    "f": (None, "d"),
    "d": (None, "z"),
    "z": (None, None),
}

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
