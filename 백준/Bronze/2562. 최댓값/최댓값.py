number = []
for x in range(9):
    i = int(input())
    number.append(i)
    
print(max(number))
print(number.index(max(number))+1)    