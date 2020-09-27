def fi(n):
    if n==0 : return 0
    if n==1 : return 1
    return fi(n-2) + fi(n-1)

