# YACS 2020.7 乙组 #1
'''
跑步
小爱在参加一个跑步比赛，需要通过很长的一条路线。这条路线分为n段，每段都悬赏了一个分数，其中第ii段的分数为a_i，得分规则如下：
如果你选择快走，则这段路的得分为0
如果你选择慢跑，则这段路的得分为a_i
如果你选择冲刺，则这段路的得分为2a_i ，但下一段路就只能快走了
你应该如何选择跑完全部线，使得得分之和最大呢？

输入:
4
1 2 3 4
输出:
14
说明:
前面都用慢跑，只有最后一份冲刺，得分计算公式为1+2+3+4*2
26
5 9 7 9 5 2 3 9 5 2 10 8 10 10 10 5 9 2 6 4 6 4 4 5 4 6
输出: 194
'''

n = int(input())
score = list(map(int,input().split(' ')))
dp = [[0]*4 for _ in range(n)]
# dp[i][0] 快走最高得分
# dp[i][1] 慢跑最高得分
# dp[i][2] 冲刺最高得分
# dp[i][3] 冲刺后快走最高得分
dp[0] = [0,score[0],2*score[0],0]
for i in range(1,n):
    dp[i][0] = max(dp[i-1])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + score[i]
    dp[i][2] = max(dp[i-1][0], dp[i-1][1], dp[i-1][3]) + 2*score[i]
    dp[i][3] = dp[i-1][2] 
# print(dp)
print(max(dp[-1]))#[n-1][1], dp[n-1][2], dp[n-1][0]
