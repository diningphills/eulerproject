# Problem 18

# T(i,j) = V(i,j) + max{T(i-1, j-1), T(i-1, j)}
# T(i,0) = V(i,0) + T(i-1,0)
# T(0,0) = V(0,0)

# ex)
# T(2,2) = V(2,2) + max{T(1,1), T(1,2)}
# T(0,0) = V(0,0)
# T(1,0) = V(1,0) + T(0,0)
# T(1,1) = V(1,1) + T(0,0)

# def Function(parameter):
    # if condition: return
    # for i in range(0, N):
    # print(N)

import os

def algorithm(V, T):
    maxValue = 0

    T[0][0] = V[0][0]

    for i, v_i in enumerate(V):
        for j, v in enumerate(v_i):
            print(V[i][j], i, j)
            # T[2][1] = V[2][1] + max T[1][0], T[1][1]
            if i==0: continue
            if i==j:
                T[i][j] = V[i][j] + T[i-1][j-1]
            elif j==0:
                T[i][j] = V[i][j] + T[i-1][j]
            else:
                T[i][j] = V[i][j] + max(T[i-1][j-1], T[i-1][j])

            if T[i][j] > maxValue:
                maxValue = T[i][j]

    return maxValue


# input
V = list()

f = open(os.path.expanduser("~/Documents/Development/Python/Project/Euler/input/18.txt"), "r")

while True: 
    line = f.readline()
    if not line: break

    V.append([int(n) for n in line.split()])


T = [[0 for col in range(row+1)] for row in range(len(V))]


print(V)
print(algorithm(V, T))

#print(algorithm(V, T))