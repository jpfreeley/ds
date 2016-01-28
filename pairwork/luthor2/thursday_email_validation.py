import sys
import re

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    if re.match(r'^"[a-z|A-Z|0-9|_|-|+|.|@]+"|[a-z|A-Z|0-9|_|-|+|.?]*@{1}[a-z|0-9]+\.{1}[a-z|0-9|-]+\.?[a-z|0-9|-]{2,}', test.strip()):
        print('true')
    else:
        print('false')

test_cases.close()