# import sys 
# def maxSubArrSum(a):
#     n = len(a)
#     max_so_far = -sys.maxsize - 1
#     max_ending_here = 0

#     for i in range(0, n):
        
#         max_ending_here = max_ending_here + a[i]
#         if max_so_far < max_ending_here:
#             max_so_far = max_ending_here
#         if max_ending_here < 0:
#             max_ending_here = 0
        
#     return max_so_far


#Time Complexcity = o(n)
#Algorithmic paradigm: DP
# def maxSubArrSum(a):
#     max_so_far = a[0]
#     max_ending_here = 0
#     n = len(a)

#     for i in range(0, n):
#         max_ending_here = max_ending_here + a[i]
#         if max_ending_here < 0:
#             max_ending_here = 0
#         elif max_so_far < max_ending_here:
#             max_so_far = max_ending_here
#     return max_so_far

#KadenS Algorithm  Tc - o(n) 
def maxSubArrSum(a):
    maxSum = 0
    curSum = 0
    n = len(a)
    for i in range(0,n):
        curSum = curSum + a[i]
        if curSum > maxSum:
            maxSum = curSum
        if curSum < 0:
            curSum = 0

    print(curSum, maxSum)
    return maxSum




if __name__ == '__main__':
  # Driver code
  a= [-2, -3, 4, -1, -2, 1, 5, -3]
  print(maxSubArrSum(a))
