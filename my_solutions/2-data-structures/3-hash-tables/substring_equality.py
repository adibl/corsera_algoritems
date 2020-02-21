# python3
import sys
from substring_comperison import FindPattern

s = sys.stdin.readline()
f = FindPattern(s)
q = int(sys.stdin.readline())
for i in range(q):
    a, b, l = map(int, sys.stdin.readline().split())
    print('Yes' if f.is_equal_substrings(a, b, l) else 'No')
