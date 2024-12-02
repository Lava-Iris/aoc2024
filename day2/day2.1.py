with open('input.txt', 'r') as f:
    data = map(lambda x: list(map(int, x.split(' '))), f.read().split('\n'))
    ans = 0
    for row in data:
        mult = 1
        ans += 1
        if row[0] < row[1]:
            mult = -1
        for i in range(1, len(row)):
            diff = (row[i-1] - row[i]) * mult
            if diff > 3 or diff <= 0:
                ans -= 1
                break

        

        
    # print(ans)