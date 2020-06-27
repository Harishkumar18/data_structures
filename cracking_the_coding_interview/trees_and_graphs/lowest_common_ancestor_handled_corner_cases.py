"""
Note that the previous method assumes that keys are present in Binary Tree. If one key is present and other is absent,
then it returns the present key as LCA (Ideally should have returned NULL).
We can extend this method to handle all cases by passing two boolean variables v1 and v2. v1 is set as true when n1
is present in tree and v2 is set as true if n2 is present in tree.
"""