#import sys
import pygame
import time
import random


class uf_set():
    # 尽量写成流式，而不要直接用固定的数组。
    def __init__(self,set_len):
        self.__set = list()   # 这是个数组  # 注意，外部读取这个数组是个很危险的事情
        for i in range(set_len):
            self.__set.append(i)  # 初始化，每个元素分别在不同的集合，集合就用自己表示
        return 
    

    def set_init(self):
        # 重置，让所有元素都分离
        for i,father in enumerate(self.__set):
            self.__set[i] = i
    
    def find(self,x):
        x_father = self.__set[x] # 查询x所在的集合
        if(x == x_father):
            out = x_father
            pass
        else:
            xff = self.find(x_father)
            self.__set[x] = xff # 将自己指向 父节点的父节点，这步是压缩
            out  = xff
        return out
    def unite(self,x,y):
        xf = self.find(x)
        yf = self.find(y)
        top = min(xf,yf)
        self.__set[x] = top
        self.__set[y] = top
        return 0

class dva_go():


    def encode_pos(self,pos_2d):
        matrix = self.matrix
        x = pos_2d[0]
        y = pos_2d[1]
        mx = self.matrix[0] # 矩阵的列数

        pos_1d = y*mx+x
        return pos_1d

    def decode_pos(self,pos_1d):
        mx = self.matrix[0] # 矩阵的列数 一行能放几个子
        go_y = pos_1d // mx
        go_x = pos_1d % mx
        pos_2d = [go_x,go_y]
        return pos_2d
    

    def get_neighbor_set(self,pos_1d):
        neighbor_set = set()
        # raise(BaseException('dont use'))
        
        
        pos_2d = self.decode_pos(pos_1d)
        pos_x = pos_2d[0]
        pos_y = pos_2d[1]
        up_pos_2d = [pos_x,pos_y-1]
        down_pos_2d = [pos_x,pos_y+1]
        left_pos_2d = [pos_x-1,pos_y]
        right_pos_2d = [pos_x+1,pos_y]
        
        neighbor_list_2d = list()   # 不一定在棋盘内
        neighbor_list_2d.append(   up_pos_2d )
        neighbor_list_2d.append(   down_pos_2d )
        neighbor_list_2d.append(   left_pos_2d )
        neighbor_list_2d.append(   right_pos_2d )

        # 遍历这个子的邻居
        for i,neighbor_2d in enumerate(neighbor_list_2d):
            if(self.pos_legal(neighbor_2d)):    # 如果这个位置在棋盘之内
                neighbor_1d = self.encode_pos(neighbor_2d)


                # print('bug',neighbor_2d,self.encode_pos(neighbor_2d))
                # print('bug',neighbor_1d,len(self.plate),self.decode_pos(neighbor_1d))
                # print(0,self.decode_pos(0))
                # print([1,1],self.encode_pos([1,1]))
                # neighbor_flag = plate[neighbor_1d]
                # if(neighbor_flag == 0 ):
                neighbor_set.add(neighbor_1d)

                    # if(neighbor_1d in [18,34]):
                    #     print('!!!!!!!!!',pos_1d)



        return neighbor_set

    def get_filter_neighbor(self,pos_1d,target_flag):
        filter_neighbor = set()

        neighbor_set = self.get_neighbor_set(pos_1d)
        plate = self.plate
        # nf = 

        # print(neighbor_set)

        for neighbor_1d in iter(neighbor_set):
            # print(neighbor_1d,len(self.plate))

            n_flag = plate[neighbor_1d]
            if(n_flag== target_flag):
                filter_neighbor.add(neighbor_1d)
        return filter_neighbor


    def update_block(self):


        # print('重置 ufs')
        self.ufs.set_init()

        plate = self.plate
        # 遍历棋盘，如果某个棋子与它左或上方的棋子同阵营，则并。
        ufs = self.ufs
        for pos_1d,flag in enumerate(plate):
            if(flag):
                same_flag_neighbor_set= self.get_filter_neighbor(pos_1d,flag)
                for n in iter(same_flag_neighbor_set):
                    ufs.unite(pos_1d,n)

        print('go.update')
        for pos_1d,flag in enumerate(plate):
            if(flag):
                head= ufs.find(pos_1d)
                print(self.decode_pos(pos_1d),' -->',    self.decode_pos(head))

        
        # print(self.ufs._dva_go__set)


    def pos_legal(self,pos_2d):
        x = pos_2d[0]
        y = pos_2d[1]
        matrix = self.matrix
        min_x = 0
        max_x = matrix[0]-1

        min_y = 0
        max_y = matrix[1]-1

        legal = 0
        if(x>=min_x and x<= max_x):
            if(y>=min_y and y<= max_y):
                legal = 1
        return legal

    def pick_down(self,pos_3d):
        
        
        pos_2d = pos_3d[0:2]
        flag = pos_3d[2]
        pos_1d = self.encode_pos(pos_2d)

        plate = self.plate 
        # old_flag = plate[pos_1d]
        
        # if(old_flag ==0):
        plate[pos_1d] = flag
        # else:
        #     print('warning.不支持在有子的地方落子。')

        #如果想在有子的地方替换，则要重度修改block信息，先不实现了，没啥用。
        

        # print('pos_1d',pos_1d)
        self.update_block()
    
    
    def blank_neighbor_of_one_go(self,pos_1d):
        # 获取一个棋子的所有空邻居
        blank_neighbor_set = set()

        plate = self.plate

        flag = plate[pos_1d]
        if(flag):   # 当这个位置有子时
            pos_2d = self.decode_pos(pos_1d)
            pos_x = pos_2d[0]
            pos_y = pos_2d[1]
            up_pos_2d = [pos_x,pos_y-1]
            down_pos_2d = [pos_x,pos_y+1]
            left_pos_2d = [pos_x-1,pos_y]
            right_pos_2d = [pos_x+1,pos_y]
            
            neighbor_list_2d = list()
            neighbor_list_2d.append(   up_pos_2d )
            neighbor_list_2d.append(   down_pos_2d )
            neighbor_list_2d.append(   left_pos_2d )
            neighbor_list_2d.append(   right_pos_2d )

            # 遍历这个子的邻居
            for i,neighbor_2d in enumerate(neighbor_list_2d):
                if(self.pos_legal(neighbor_2d)):    # 如果这个位置在棋盘之内
                    neighbor_1d = self.encode_pos(neighbor_2d)

                    neighbor_flag = plate[neighbor_1d]
                    if(neighbor_flag ==0 ):
                        blank_neighbor_set.add(neighbor_1d)

                        if(neighbor_1d in [18,34]):
                            print('blank_neighbor_of_one_go !!!!!!!!!',pos_1d)
        return blank_neighbor_set


    def pick_up_one_go(self,pos_1d):
        # 如果是任意提子，则要刷新整个块
        # 暂时不写

        # 直接刷新整个棋盘的block算了
        return 


    def pick_up_block(self,block_head_1d):
        # 提掉整块棋。
        #  1 flag 清空
        # block 重置为 坐标
        plate = self.plate
        ufs = self.ufs

        for pos_1d,block_head_1d in enumerate(ufs.set):
            pass


    def pick_up(self):
        # print(self.plate)
        # print(self.new_pos_1d)
        # self.block_blank_neighbor = list()  # 记录一片棋的空邻居，用来计算气。记录一维坐标

        # bbn = self.block_blank_neighbor
        bbn = list()
        for pos_1d,flag in enumerate(self.plate):
            bbn.append(set())


        # 遍历每个块，把每块中的每个子的空邻居列在一个表里。
        ufs = self.ufs
        plate = self.plate
        # for pos_1d,block_1d in enumerate(ufs.set):
        for pos_1d,flag in enumerate(plate):
            # flag = plate[pos_1d]
            if(flag):#如果有子
                # 获取这个 子的空邻居
                blank_neighbor_set = self.blank_neighbor_of_one_go(pos_1d)
                block_head = ufs.find(pos_1d)    # 这个棋子 属于哪个块？
                
                bs = bbn[block_head]
                bs = bs | blank_neighbor_set    # 并集
                bbn[block_head] = bs
        
        print('___')
        for pos_1d,flag in enumerate(plate):
        # for pos_1d,block_1d in enumerate(ufs.set):
            # flag = plate[pos_1d]
            if(flag):#如果有子
                
                block_head = ufs.find(pos_1d)

                bs = bbn[block_head]    # 这个子所在块的所有空邻居


                qi_count = len(bs)   # 终于，我们计算出了一个棋子气的数量
                # print(block_head,qi_count,bs)
                print('pos',self.decode_pos(pos_1d),end=' | ')
                print('head',self.decode_pos(block_head),qi_count,end='|')
                for bb in iter (bs):
                    print(self.decode_pos(bb),end=',')
                # 
                print('')
        
        self.update_block()


        self.block_blank_neighbor = bbn



        return

    def __init__(self,show_game):


        # 显示画面
        self.show_game = show_game

        # 画布大小
        self.world_x = 1920*0.7
        self.world_y = 1080*0.7

        # self.world_x = 2**10
        # self.world_y = 2**10

        matrix = [16,9] # 列数，行数
        self.matrix = matrix

        self.plate = list()
        # self.block_blank_neighbor = list()  # 记录一片棋的空邻居，用来计算气。记录一维坐标

        plate_len = matrix[0]*matrix[1]
        for i in range(plate_len):
            self.plate.append(0)
            # self.block_blank_neighbor.append(set())
        
        self.ufs= uf_set(len(self.plate)) # 建立一个并查集    用来记录哪些棋子连成了一片

        


        # bgc = (255,255,255)
        bgc = (0,0,0)
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
        # go_cut = [[1,0,1],[2,0,1],[0,1,1],[3,1,1],[1,2,1],[2,2,1],
        #           [1,1,2],[2,1,2]]


        go_cut = [[1,0,2],[2,0,2],[0,1,2],[3,1,2],[1,2,2,],[3,2,2],[2,3,2],
                  [1,1,1],[2,1,1],[2,2,1]]
        while(1):
            # random_plate_pos = random.randint(0,plate_len-1)
            # plate[random_plate_pos]=random.randint(0,2)
            
            # 落子，流式输入
            if(episode<=len(go_cut)-1):
                pos_3d = go_cut[episode]
            else:
                pos_3d = [0,0,0]
            self.pick_down(pos_3d)


            # self.plate = plate
            
            self.pick_up()

            # print(plate)


            if(self.show_game):
                self.screen.fill(bgc)
                plate = self.plate

                for j in range(0,2):
                    for i in range(matrix[j]):
                        
                        # 轴号
                        text = font.render(str(i), True, fgc)
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
    show_game = 1
    dva_go(show_game)