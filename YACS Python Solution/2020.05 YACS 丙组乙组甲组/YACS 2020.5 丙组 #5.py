# YACS 2020.5 丙组 #5
'''
最大回撤
内存限制: 256 Mb时间限制: 1000 ms
题目背景
股票价格瞬息万变。在金融市场上，经常需要统计一只股票的最大回撤。最大回撤是指投资者在某天买入，在之后的某天卖出，可能造成的最大亏损，它可以反应一只股票在历史上的最坏表现。

题目描述
给定一个整数序列 a1 a2 a3...ai，每个 ai 的i表示某只股票的在某一天的价格，请计算这只股票的最大回撤。即寻找两个下标满足 1 ≤ i ≤ j ≤ n，且 ai-aj最大。
注意，由于原油宝事件的出现，不能想当然地以为 ai 都是正数。

输入格式
第一行：单个整数表示 n，
第二行：n 个整数表示 a1 a2 a3....

输出格式
单个整数：表示这只股票的最大回撤，如果股票价格一直上涨，输出 0。

样例数据
输入:
5
2 3 7 6 1 
输出:
6
说明:
7-1=6
输入:
5
1 2 3 4 5
输出:
0
说明:


'''
def f(prices):
    if not prices:
        return 0
    cur_diff = 0
    maxn = 0
    for i in range(1,len(prices)):
        cur_diff = max(cur_diff+prices[i]-prices[i-1],0)
        maxn = max(cur_diff,maxn)
    return maxn
n = int(input())
prices = [-int(x) for x in input().split()]

print(f(prices))