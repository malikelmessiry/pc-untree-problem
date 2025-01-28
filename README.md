# Consonants Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in converting a binary tree into a dictionary.

For example:

```
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
```

Would be converted to:

```py
{
    "a": ("x", "y"),
    "x": ("e", "m"),
    "y": (None, "p"),
    "e": (None, None),
    "m": (None, None),
    "p": (None, None),
}
```

Each key of the dictionary will be the data held by a parent node. Each value will be a tuple. The first element of the tuple will hold the data from the left child. The second element of the tuple will hold the data from the right child. If a node does not have a left and/or right child, the value in the corresponding spots in tuple will be None.

Write a function that takes in the root of a tree and returns a dictionary representation of the tree.

## Examples

### Example 1

The tree

```
       d
      / \
     e   v
```

produces the following dictionary

```py
{
    "d": ("e", "v"),
    "e": (None, None),
    "v": (None, None),
}
```

### Example 2

The tree

```
           a
         /   \
        /     \
       x       y
      / \       \
     e   m       p
```

produces the following dictionary

```py
{
    "a": ("x", "y"),
    "x": ("e", "m"),
    "y": (None, "p"),
    "e": (None, None),
    "m": (None, None),
    "p": (None, None),
}
```

### Example 3

The tree

```
           g
         /   \
        /     \
       e       f
      /         \
     k           d
    /             \
   w               z
```

produces the following dictionary

```py
{
    "g": ("e", "f"),
    "e": ("k", None),
    "k": ("w", None),
    "w": (None, None),
    "f": (None, "d"),
    "d": (None, "z"),
    "z": (None, None),
}
```
