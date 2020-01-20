# Given an integer N, the task is to find the minimum number of coins required to create all the values in the range [1, N].

# Input: N = 5
# Output: 3
# The coins {1, 2, 4} can be used to generate
# all the values in the range [1, 5].
# 1 = 1
# 2 = 2
# 3 = 1 + 2
# 4 = 4
# 5 = 1 + 4
#
# Input: N = 10
# Output: 4


def findMinimum(N):

    list = []
    sum = 0


    for i in range(0, N):
        sum += 2**i
        list.append(sum)

    for value in list:

        if(value>N):
            print(list[0:list.index(value)])
            return (list.index(value) + 1)





if __name__ == "__main__":
    print(findMinimum(100))