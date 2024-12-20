def fibu(n):
    ls = [0,1]
    for i in range(1,n):
        ls.append((ls[-1]+ls[-2]))
    return ls

fibu(19)

