with open('input.txt', 'r') as f:
    data = list(map(lambda x: x.split('   '), f.read().split('\n')))
    list1 = [entry[0] for entry in data]
    list2 = [entry[1] for entry in data]
    list1.sort()
    list2.sort()
    print(sum([abs(int(list1[i]) - int(list2[i])) for i in range(len(list1))]))
