from itertools import permutations

string, length = input().split()

# output = ["".join(i) for i in permutations(string,int(length))]
# print(output)
# output.sort()
# print(output)

# print("\n".join(output))

for i in permutations(sorted(string),int(length)):
    print(i)
    print ("".join(i))