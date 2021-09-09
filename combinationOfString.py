from itertools import combinations
io = input().split()
print(io)
S = io[0]
k = int(io[1])
print(sorted(S))
for i in range(1,k+1):
    print(i)
    for j in combinations(sorted(S),i):
        print(j)
        print("".join(j))