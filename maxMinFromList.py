def max_min(data):
    l = data[0]
    s = data[0]


    for n in data:
        if n > l: l = n
        elif n < s: s = n

    return l, s


print(max_min([0, 4, 6, -34, 61, 23, 90]))
