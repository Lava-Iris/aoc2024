from collections import Counter

with open('input.txt', 'r') as f:
    data = list(map(lambda x: x.split('   '), f.read().split('\n')))
    list1 = [entry[0] for entry in data]
    list2 = [entry[1] for entry in data]
    list2 = Counter(list2)
    
    print(sum([int(num) * list2[num] for num in list1]))
