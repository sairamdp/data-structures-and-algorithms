program_input = input("").split("\n")
t = program_input[0]

while t != 0:
    n = int(input(""))
    x = input("").split()

    dict = {2 : 4,
             3 : 2,
             4 : 1}
    for i in range(n):
        if x[i] in dict:
            dict[x[i]] += 1
        else:
            dict[x[i]] = 1
    
    for j in dict:
        if dict[j] >= 3:
            print(j)
            break
    else:
        print(-1)