def move(n, a, b, c): #b是缓冲区
    if n == 1:
        print(a, ' -> ', c)     #把A柱移动到C柱
    else :
        move(n-1, a, c, b)      #把n-1个a柱上的盘子移动到缓冲区b中
        move(1, a, b, c)        #把A中底部最大的移动到C
        move(n-1, b, a, c)      #把剩下的移动到C柱
move(3, 'A', 'B', 'C')
