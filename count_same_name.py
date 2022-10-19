names = ['Tom', 'Jerry', 'Mike', 'Tom', 'Mike', 'Happy', 'Tom']
n = len(names)
tom_count, jerry_count, mike_count, happy_count = 0,0,0,0

for i in range(0, n):
    if names[i] == 'Tom':
        tom_count+=1
    elif names[i] == 'Jerry':
        jerry_count+=1
    elif names[i] == 'Mike':
        mike_count+=1
    elif names[i] == 'Happy':
        happy_count+=1

print('Tom', tom_count)
print('Jerry', jerry_count)
print('Mike', mike_count)
print('Happy', happy_count)


