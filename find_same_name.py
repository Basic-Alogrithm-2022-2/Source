def find_same_name(n):
    n = len(names)
    for i in range(0, n - 1):  # 0, 1, 2, 3
        j = i
        for j in range(i + 1, n):  # 0, 1, 2
            if names[i] == names[j]:
                result.add(names[i])
    return result

names = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike', 'Happy', 'Tom']
result = set()

print(find_same_name(names))

