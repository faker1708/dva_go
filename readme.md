

2023
0409
1635
现在可以画任意长宽的棋盘。窗口尺寸也任意

dva_go copy 3
可以画棋子了。

小纠结。我不想让画面出现 太多颜色，所以白棋用空心圆了。视觉上不太方便。


现在要写围棋的提子算法。


bfs?dfs?


看了别人的提子算法，感觉挺麻烦的，不想去阅读他们的了。



2005
在写提子算法



2050

ufs 的set 应该是个私有成员，不应该让用户访问。


2216

需求
鼠标移动时 跟随显示 一个棋子
鼠标点击时，放置一个棋子


2250
dva_go copy 17
在添加鼠标



2320

如果 一个落子，提起了其它阵营的子，则这个子连同它这个块的子都可以豁免。

如果一个落子，没有提起别人的子，则这个子是自杀。正常提子即可。


完成了打劫的逻辑
dva_go copy 19


学习别人

gnugo
gtp





16:30 2023/6/4
最新的项目在dqn_dva中