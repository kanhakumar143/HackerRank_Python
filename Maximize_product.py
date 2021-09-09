# Output Format

# Output a single integer denoting the value .

# Sample Input

# 3 1000
# 2 5 4
# 3 7 8 9 
# 5 5 7 8 9 10 
# Sample Output

# 206

from itertools import product
K,M = map(int,input().split())
nums = []
for _ in range(K):
    row = map(int,input().split()[1:])
    nums.append(map(lambda x:x**2%M, row))
print(max(map(lambda x: sum(x)%M, product(*nums))))