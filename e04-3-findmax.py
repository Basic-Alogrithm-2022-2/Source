def max(x, y):
    if x > y:
        return x
    else:
        return y

def max_array(array, len):
    if len == 1:
        return array[0]
    else:
        print(array[len-1], len-1)
        return max(array[len - 1], max_array(array, len - 1))

temp_array = [33, 44, 5, 66, 139, 90, 45, 23]

print(max_array(temp_array, len(temp_array)))