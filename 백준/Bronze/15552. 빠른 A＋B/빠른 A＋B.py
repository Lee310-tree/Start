import sys

x = int(sys.stdin.readline())
for i in range(x):
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)