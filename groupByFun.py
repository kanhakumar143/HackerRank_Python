# Sample Input

# 1222311
# Sample Output

# (1, 1) (3, 2) (1, 3) (2, 1)
# Type1
# S = input()
# i=1
# a=[]
# count=1
# while i<len(S):
#     if S[i]==S[i-1]:
#         count+=1
#         i+=1
#     else:
#         a.append((count,int(S[i-1])))
#         i+=1
#         count=1
# a.append((count,int(S[i-1])))
# for i in a:
#     print(i,end=' ')

# Type2
# from itertools import groupby

# io = input()
# for i,j in groupby(map(int,list(io))):
#     print(tuple([len(list(j)), i]) ,end = " ")

# Type3
from itertools import groupby
print(groupby(input()))
for key, group in groupby(input()):
    print((len(list(group)), int(key)), end=' ')