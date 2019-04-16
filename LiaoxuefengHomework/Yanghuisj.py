def triangles():
    L = [1]
    while L:
        yield L
        L = list(L)
        L.insert(0,0)
        L.append(0)
        L = [L[x]+L[x+1] for x in range(len(L)-1)]
# 解释在网站上