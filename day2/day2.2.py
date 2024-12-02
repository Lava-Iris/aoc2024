def is_safe(row, miss = 0):
    mult = 1
    if row[0] < row[1]:
        mult = -1
    for i in range(1, len(row)):
        diff = (row[i-1] - row[i]) * mult
        if diff > 3 or diff <= 0:
            if miss > 0:
                return False
            return is_safe(row[:i] + row[i+1:], miss + 1) or is_safe(row[:i-1] + row[i:], miss + 1)
    return True

with open('input.txt', 'r') as f:
    data = map(lambda x: list(map(int, x.split(' '))), f.read().split('\n'))
    ans = 0
    for row in data:
        if is_safe(row) or is_safe(row[::-1]):
            ans += 1
        
    print(ans)