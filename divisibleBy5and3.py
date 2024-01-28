n = []
num = int(input('Enter the limit: '))
for i in range(1, num):
    if (i % 5 == 0) and (i % 3 == 0):
        n.append(str(i))

print(', '.join(n))
