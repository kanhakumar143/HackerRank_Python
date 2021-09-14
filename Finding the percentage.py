# Sample Input 0

# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika
# Sample Output 0
# 
# 56.00
# https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=next-challenge&h_v=zen

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
output = list(student_marks[query_name])    
per = sum(output)/len(output);
print("%.2f" % per);