number = [int(input()) for i in range(10)]

for i in range(10):
    number[i] = number[i] % 42
    
print(len(list(set(number))))