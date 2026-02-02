A, B = map(int, input().split())
C = int(input())

total = A * 60 + B + C
A = (total // 60) % 24
B = total % 60

print(A, B)