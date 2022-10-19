def find_fair(n):
    n = len(names)
    for i in range(0, n):
        j = i
        for j in range(j, n-1):
            print(j, names[j], '-', names[j+1])
            print('--------------')

names = ['Tom', 'Jerry', 'Mike', 'Happy']
find_fair(names)