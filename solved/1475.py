from collections import Counter
k = [i for i in input()]
di = Counter(k)
if di['9'] or di['6']:
    di['6'] = di['6'] + di['9']
    di['6'] = sum(divmod(di['6'], 2))
    del di['9']
print(max(di.values()))