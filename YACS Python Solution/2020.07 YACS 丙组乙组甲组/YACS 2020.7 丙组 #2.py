# YACS 2020.7 丙组 #2
# 感应门
'''
题目描述
随着社会经济的发展，感应门越来越多的替代了传统的推拉门，成为了商场写字楼的标配。
在某购物商场，当有人经过时，感应门会自动打开，直到x秒后再自动关闭。如果感应门在打开状态时有人经过，那么这个时间会被重置，感应门会从此刻开始继续打开xx秒。
小爱经过了一段时间的观察，记录下了今天购物商场共有n次人员进出，每次人员进出的时间为t_i 。（小爱开始记录的时间记为t=0）请问这段时间内这个购物商场感应门处于开启状态共多少秒？

输入格式
输入共两行：
第一行：两个正整数n,x，分别表示进出人数和每次感应门开启时间。
第二行：nn个正整数t_1,t_2...t_nt 

7 3
1 2 7 10 15 17 22
output = 18
'''

n,x = map(int,input().split(' '))
li = sorted(list(set(map(int,input().split(' ')))))
ans = 0
for i in range(len(li)-1):
    d = li[i+1]-li[i]
    if 0<d<x:
        ans+=d
    else:
        ans+=x
print(ans+x)


# 
n,x = map(int,input().split(' '))
t = list(set(map(int,input().split(' '))))
m = t[n - 1] - t[0]
for i in range(n):
    if t[i + 1] - t[i] > x:
        m = m - (t[i + 1] - t[i]) + x
print(x+m)
