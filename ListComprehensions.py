if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    arr = []
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                rs = i + j + k
                if rs != n:
                    arr.append([i, j, k])
    print(arr)

#arr = [[i, j, k] 
    # for i in range(x) 
    # for j in range(y) 
    # for k in range(z) 
    # if i + j + k != n]