"""
@author : srnarayanaa & pravin014
"""
"""
OS.walk() generates the file names in a directory tree - DFS.
For each directory in the tree rooted at directory top (including top itself), it yields a 3-tuple (dirpath, dirnames, filenames).
We use yield instead of return to return sequence of values.
"""

import os
def dfs(path):
    for root, dirs, files in os.walk(path):
        for i in files:
            abspath = os.path.abspath(os.path.join(root, i))
            yield abspath

if __name__ == "__main__":
    x = dfs('/Users/narayanaaramamurthy/testdirectory')
    for i in x:
        print(i)
