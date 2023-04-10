#import sys
import pygame
import time
import random


class uf_set():
    # 尽量写成流式，而不要直接用固定的数组。
    def __init__(self,set_len):
        self.set = list()
        for i in range(set_len):
            self.set.append(i)  # 初始化，每个元素分别在不同的集合，集合就用自己表示
        return 
    
    def find(self,x):
        x_father = self.set[x] # 查询x所在的集合
        if(x == x_father):
            out = x_father
            pass
        else:
            xff = self.find(x_father)
            self.set[x] = xff # 将自己指向 父节点的父节点，这步是压缩
            out  = xff
        return out
    def unite(self,x,y):
        xf = self.find(x)
        yf = self.find(y)
        top = min(xf,yf)
        self.set[x] = top
        self.set[y] = top
        return 0

class dva_go():

    def pick_down(self,pos_2d):
        new_pos_1d
        plate[new_pos_1d]=go_cut[i][2]

    def read_cut(self,go_cut,i):
        # 读棋谱
        if(i<=len(go_cut)-1):
            go_x = go_cut[i][0]
            go_y = go_cut[i][1]
            new_pos_1d = go_y*matrix[0]+go_x

        self.new_pos_1d = new_pos_1d
        
        flag = go_cut[i][2]
        pos_2d  = [new_pos_1d,flag]
        return xx
    
    def pick_up(self):
        # print(self.plate)
        print(self.new_pos_1d)

        # 遍历棋盘，如果某个棋子与它左或上方的棋子同阵营，则并。
        uf = self.uf
        for i,ele in enumerate(self.plate):

            uf.unite(go_a,go_b)


        return

    def __init__(self):


        # 显示画面
        self.show_game = 1

        # 画布大小
        self.world_x = 1920*0.7
        self.world_y = 1080*0.7

        # self.world_x = 2**10
        # self.world_y = 2**10

        matrix = [16,9]

        self.plate = list()
        plate_len = matrix[0]*matrix[1]
        for i in range(plate_len):
            self.plate.append(0)

        
        uf= uf_set(len(self.plate)) # 建立一个并查集    用来记录哪些棋子连成了一片

        
        bgc = (255,255,255)
        # bgc = (0,0,0)
        fgc = (255-bgc[0],255-bgc[1],255-bgc[2])

        road_width = self.world_x/(matrix[0]+1)
        road_height = self.world_y/(matrix[1]+1)
        

        # road_width = 40
        # road_height = 40

        if(self.show_game):
            #使用pygame之前必须初始化
            pygame.init()
            #设置主屏窗口 ；设置全屏格式：flags=pygame.FULLSCREEN
            self.screen = pygame.display.set_mode((self.world_x,self.world_y))
            #设置窗口标题
            pygame.display.set_caption('dva_go')

            self.Cell = [1,1]
            self.Cell[0] = 10
            self.Cell[1] = 10

            self.Size = [33,44]
            # self.draw_axes()
        
            font = pygame.font.Font(None, 20)
        
        episode = 0

        # 棋谱 x坐标 y坐标 第三个数表示 黑白
        go_cut = [[1,0,1],[2,0,1],[0,1,1],[3,1,1],[1,2,1],[2,2,1],
                  [1,1,2],[2,1,2]]
        while(1):
            # random_plate_pos = random.randint(0,plate_len-1)
            # plate[random_plate_pos]=random.randint(0,2)
            
            # 落子，流式输入

            pos_3d = self.read_cut(go_cut,episode)  # xy坐标 阵营
            self.pick_down(pos_3d)


            # self.plate = plate
            
            self.pick_up()

            # print(plate)


            if(self.show_game):
                self.screen.fill(bgc)


                for j in range(0,2):
                    for i in range(matrix[j]):
                        
                        # 轴号
                        text = font.render(str(i+1), True, fgc)
                        text_x = i * road_width+ road_width
                        text_y = road_height/2
                        
                        if(j==1):
                            # txx = text_y
                            text_y = i * road_height+ road_height
                            text_x = road_width/2
                        
                        self.screen.blit(text, (text_x, text_y))


                    for i in range(matrix[1-j]):
                        # print(i)
                        start_pos = (road_width,road_height*(i+1))
                        end_pos = (road_width*matrix[0],road_height*(i+1))
                        if(j==1):
                            start_pos = (road_width*(i+1),road_height)
                            end_pos = (road_width*(i+1),road_height*matrix[j])
                            pass
                        pygame.draw.line(self.screen, fgc, start_pos,end_pos, 1)



                for kk ,ele in enumerate(plate):
                    # 画棋子
                    # 棋子在棋盘上的坐标
                    go_y = kk//matrix[0]
                    go_x = kk%matrix[0]

                    # 在画布上的坐标
                    pos = (go_x*road_width+road_width,go_y*road_height+road_height)

                    go_radius = (road_width+road_height)/2/3  # 半径   # 棋子 视觉 大小


                    if(plate[kk]==1):# 黑子 实心圆
                        # print(go_x,go_y,plate[kk])

                        pygame.draw.circle(self.screen, fgc, pos, go_radius, width=0)


                    if(plate[kk]==2):# 白子 空心圆
                        # print(go_x,go_y,plate[kk])

                        # pos = (go_x*road_width+road_width,go_y*road_height+road_height)
                        # radius = (road_width+road_height)/2/4  # 半径   # 棋子 视觉 大小
                        pygame.draw.circle(self.screen, bgc, pos, go_radius, width=0)
                        pygame.draw.circle(self.screen, fgc, pos, go_radius, width=8)


                pygame.display.flip() #更新屏幕内容


                for event in pygame.event.get():    # 关闭游戏
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
            
            episode+=1
            time.sleep(0.01)
        print('over')
        time.sleep(22)


if __name__ == "__main__":
    dva_go()