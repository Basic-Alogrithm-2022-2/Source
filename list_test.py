a = [5, 7, 9, 2, 4, 20, 21, 45, 91]
print('length =', len(a))

# 리스트 인덱싱
# print(a[0])
# print(a[1])
# print(a[2])

for i in range(0,len(a)) :
    print(i, ':', a[i])

for value in a:
    print(value)

# enumerate
for i in enumerate(a):
    print(i[0], i[1])

for i, value in enumerate(a):
    print(i, ':', value)


# 리스트 역인덱싱
# print(a[-1])
# print(a[-2])ß
# print(a[-3])