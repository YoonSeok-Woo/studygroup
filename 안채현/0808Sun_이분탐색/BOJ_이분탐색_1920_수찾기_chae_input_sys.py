import sys

#sys.stdin.readline()

T1 = int(sys.stdin.readline())   #5

A_list = []
for a in range(1):
    A_list = list(map(int, sys.stdin.readline().split(' ')))     #[4, 1, 5, 2, 3]



T2 = int(sys.stdin.readline())   #5

B_list = []
for b in range(1):
    B_list = list(map(int, sys.stdin.readline().split(' ')))     #[1, 3, 7, 9, 5]


#print(A_list)   ##[4, 1, 5, 2, 3]
#print(B_list)   ##[1, 3, 7, 9, 5]


for c in B_list:
    if c in A_list:
        print(1)

    else:
        print(0)


# 1
# 1
# 0
# 0
# 1
