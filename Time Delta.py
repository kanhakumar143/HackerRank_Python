# Sample Input 0

# 2
# Sun 10 May 2015 13:54:36 -0700
# Sun 10 May 2015 13:54:36 -0000
# Sat 02 May 2015 19:54:36 +0530
# Fri 01 May 2015 13:54:36 -0000
# Sample Output 0

# 25200
# 88200
# https://www.hackerrank.com/challenges/python-time-delta/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from datetime import datetime as dt

fmt = '%a %d %b %Y %H:%M:%S %z'
for _ in range(int(input())):
    time1 = dt.strptime(input(), fmt)
    time2 = dt.strptime(input(), fmt)
    print(int(abs((time1 - time2).total_seconds())))