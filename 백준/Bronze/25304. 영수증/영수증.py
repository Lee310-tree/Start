X = int(input())
Y = int(input())

sum = 0
for i in range(Y):
    price, cnt = map(int, input().split())
    sum += (price * cnt)
if sum == X:
    print('Yes')   
else:
    print('No')
    