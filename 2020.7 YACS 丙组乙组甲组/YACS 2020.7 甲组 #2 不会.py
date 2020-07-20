# YACS 2020.7 甲组 #2
'''
摄像头安装
内存限制: 256 Mb时间限制: 1000 ms
题目描述
在一条大街上，开了 n 家商店，我们需要从这些商店里，选择一部分商店，安装摄像头。第 i 家商店安装摄像头的费用为 ci
请问应该选择哪些商店安装摄像头，使得任意 k家连续的商店里，都至少拥有两个摄像头。

输入格式
第一行：两个整数 n 与 k；
第二行：n 个整数表示 c1,c2,。。。,cn

输出格式
单个整数：表示安装摄像头的最小总费用。
样例数据
输入:
5 3
10 7 5 2 7
输出:
14
说明:
选择第2~4家安装，总费用7+5+2=14
输入:
10 5
3 1 4 1 5 9 2 6 5 3
输出:
9

行号0: 标准输出: 36 标准输入： ['12 4\n', '4 16 15 7 6 13 6 15 8 5 15 19\n']
行号0: 标准输出: 107 标准输入： ['20 4\n', '17 16 20 15 11 3 19 20 9 12 8 9 14 15 17 12 5 9 4 14\n']
行号0: 标准输出: 104 标准输入： ['20 4\n', '6 11 18 20 19 12 11 7 9 18 16 13 12 5 4 3 11 6 17 10\n']
'''
