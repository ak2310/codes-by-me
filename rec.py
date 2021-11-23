def rec_fact(n):
    if (n==1):
            return n
    else:
        return n*rec_fact(n-1)
        