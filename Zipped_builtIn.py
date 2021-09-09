# Sample Input

# 5 3
# 89 90 78 93 80
# 90 91 85 88 86  
# 91 92 83 89 90.5
# Sample Output

# 90.0 
# 91.0 
# 82.0 
# 90.0 
# 85.5  
# https://www.hackerrank.com/challenges/zipped/problem?h_r=next-challenge&h_v=zen


N, X = map(int, input().split())
score = []
for _ in range(X):
    score.append(list(map(float, input().split())))
for stud in list(zip(*score)):
    print((sum(stud) / len(stud)))