# Sample Input 0

# 2
# 1 2
# Sample Output 0

# 3713081631934410656

# https://www.hackerrank.com/challenges/python-tuples/problem?h_r=next-challenge&h_v=zen


if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t=tuple(integer_list)

    print(hash(t))