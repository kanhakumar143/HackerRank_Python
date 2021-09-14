# find runner-up score
# Sample Input 0

# 5
# 2 3 6 6 5
# Sample Output 0

# 5

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    P = list(arr)

    Q = set(P)

    R = sorted(list(Q))

    print (R[-2])
