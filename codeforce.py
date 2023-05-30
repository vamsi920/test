t = int(input())
for _ in range(t):
    line = input()
    line = line.split()
    n, k = int(line[0]), int(line[1])
    res = "NO"
    if(n%2==0):
        print("YES")
    else:
        n -= k*int(n/k)
        if(n<k and n<2):
            print("NO")
        else:
            if(n%2==0):
                print("YES")
            else:
                print("NO")

    