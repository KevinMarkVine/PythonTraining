#Case 1：字符串拼接
'''
str1=input("请输入一个人的名字：")
str2=input("请输入一个国家的名字：")
print("世界这么大，{}想去{}看看".format(str1,str2))
'''
#Case 2:整数序列求和
'''
n=input("请输入整数N：")
sum=0
for i in range(int(n)):
    sum+=i+1
print("1到N求和结果：",sum)
'''
#Case 3:九九乘法表
'''
for i in range(1,10):
    for j in range(1,i+1):
        print("{}*{}={:2}".format(j,i,i*j),end=' ')
    print(' ')
'''

#Case 4:阶乘运算
