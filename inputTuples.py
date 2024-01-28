a = []
line = input('Enter the list of tuples: ')
while (line != ''):
    a.append(tuple(line.split()))
    line = input()

print(a)
# insert a blank line to mark the end of the input
