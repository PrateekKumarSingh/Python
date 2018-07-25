def staircase(n):
    for i in range(0,n):
        times = n-i-1
        rem = n-times
        out = " "*times + '#'*rem
        print(out)

staircase(8)