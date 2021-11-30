def toh(n,s,d,a):
    if n==1:
        print("Move disk",n,"from source",s,"to destination",d)
        return
    toh(n-1,s,a,d)
    print("Move disk",n,"from source",s,"to destination",d)
    toh(n-1,a,d,s)

