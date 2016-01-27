import sys
from collections import Counter


test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    count = sorted(list(dict(Counter(c for c in test.lower()\
                    if c.isalpha())).items()), \
                   key= lambda p: p[1], reverse=True)
    last = 0
    value = 26
    for pair in count:
        last += value*pair[1]
        value -= 1 
    print(last)

test_cases.close()