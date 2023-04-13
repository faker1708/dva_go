

import dva_go_rdqn


import sys




import pygame
import time
import random

import math
import copy
import sys

class uf_set():
    # 尽量写成流式，而不要直接用固定的数组。
    def __init__(self,set_len):
        self.__set = list()   # 这是个数组  # 注意，外部读取这个数组是个很危险的事情
        for i in range(set_len):
            self.__set.append(i)  # 初始化，每个元素分别在不同的集合，集合就用自己表示
        return 
    
    def print(self):
        print('ufs',end = ' ')
        for _,ele in enumerate(self.__set):
            print(ele,end = ' ')
        print('')

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


                neighbor_set.add(neighbor_1d)


        return neighbor_set

    def get_filter_neighbor(self,pos_1d,target_flag,plate):
        filter_neighbor = set()

        neighbor_set = self.get_neighbor_set(pos_1d)


        for neighbor_1d in iter(neighbor_set):
            n_flag = plate[neighbor_1d]
            if(n_flag== target_flag):
                filter_neighbor.add(neighbor_1d)
        return filter_neighbor


    def update_block(self,plate):


        ufs = uf_set(len(plate))

        for pos_1d,flag in enumerate(plate):
            if(flag):
                same_flag_neighbor_set= self.get_filter_neighbor(pos_1d,flag,plate)   # 选出同色的邻居
                for n in iter(same_flag_neighbor_set):
                    ufs.unite(pos_1d,n)



        return ufs

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

    def pos_legal_1d(self,pos_1d):
        if(pos_1d>=0):
            pos_2d = self.decode_pos(pos_1d)
            out = self.pos_legal(pos_2d)
        else:
            out = 0
        return out

    
    def blank_neighbor_of_one_go(self,pos_1d,plate):
        # 获取一个棋子的所有空邻居
        blank_neighbor_set = set()


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

        return blank_neighbor_set


    def pre_pick_up(self,new_go,new_go_flag,some_plate):
        # 输出击杀信息
        # 这个函数有问题


        bbn = list()    # block_blank_neighbor
        for pos_1d,flag in enumerate(some_plate):
            bbn.append(set())


        # 遍历每个块，把每块中的每个子的空邻居列在一个表里。
        plate = copy.deepcopy(some_plate)   # 虚拟棋盘
        plate[new_go] = new_go_flag# 仿真落子

        # print('棋子',new_go, new_go_flag)

        ufs = self.update_block(plate)
        # ufs.print()
        # ufs = uf_set(len(plate))
        


        for pos_1d,flag in enumerate(plate):
            if(flag):#如果有子
                # 获取这个 子的空邻居
                blank_neighbor_set = self.blank_neighbor_of_one_go(pos_1d,plate)


                # print('blank_neighbor_set',blank_neighbor_set)
                block_head = ufs.find(pos_1d)    # 这个棋子 属于哪个块？
                
                bs = bbn[block_head]
                bs = bs | blank_neighbor_set    # 并集
                bbn[block_head] = bs
        
        kill_flag = set()


        protect_go = -1
        if(self.record):
            protect_go = self.record[-1]

        if(protect_go>=0):
            protect_block = ufs.find(protect_go)   # 新落子的块标记为保护块。当击杀异阵营棋子时，触发保护条款。
            protect_flag = plate[protect_go]
        else:
            # 弃手应该直接 返回 空集合，谁也杀不掉。
            protect_block = -1
            protect_flag =-1

        for pos_1d,flag in enumerate(plate):
            if(flag):#如果有子
                
                block_head = ufs.find(pos_1d)

                bs = bbn[block_head]    # 这个子所在块的所有空邻居


                qi_count = len(bs)
                if(qi_count==0):
                    kill_flag.add(flag)


        protect = 0 # 是否触发豁免

        if protect_flag in kill_flag:
            kill_flag.remove(protect_flag)

        if(kill_flag): # 击杀了其它阵营的玩家了
            # print('触发保护')
            protect = 1
        else:
            # print('不被保护')
            protect = 0



        dead_set = set()
        for pos_1d,flag in enumerate(plate):
            if(flag):#如果有子
                
                block_head = ufs.find(pos_1d)

                bs = bbn[block_head]    # 这个子所在块的所有空邻居


                qi_count = len(bs)


                # if(self.is_terminal()):
                #     if(qi_count ==0):
                #         print(self.decode_pos(pos_1d),flag)

                # print('pre_pick_up',qi_count,pos_1d)
                if(qi_count==0):
                    
                    # 需要建立豁免棋块的概念。
                    
                    if(protect==1):
                        if(block_head==protect_block):
                            continue    #豁免

                    dead_set.add(pos_1d)


        # if(self.is_terminal()):
        #     if(dead_set):
        #         print('pre_pick_up',dead_set,self.decode_pos(new_go),new_go_flag)
        #         print('检查 ',plate[new_go],plate[new_go])


        return dead_set


    def pick_up(self,dead_set,plate):
        # 真的提子了

        for ele in iter(dead_set):
            plate[ele] = 0

        return 0



    def random_pos(self,plate):

        pos_1d = random.randint(-1,len(plate)-1)
        if(pos_1d<=-1):
            pos_1d = random.randint(-1,len(plate)-1)
            if(pos_1d<=-1):
                pos_1d = random.randint(-1,len(plate)-1)
        return pos_1d

    def matrix_to_screen(self,m_pos):
        go_x = m_pos[0]
        go_y = m_pos[1]

        
        scx = self.screen_x
        scy = self.screen_y


        matrix = self.matrix
        mxo = matrix[0]+1
        myo = matrix[1]+1

        road_width = scx/mxo # 每条路的宽度
        road_height = scy/myo


        
        s_pos = (go_x*road_width+road_width,go_y*road_height+road_height)

        return s_pos

    def screen_to_matrix(self,s_pos):
        # 将画布坐标转成棋盘坐标
        sx = s_pos[0]
        sy = s_pos[1]

        scx = self.screen_x
        scy = self.screen_y

        # # 百分比
        # px = sx/
        # py = sy/self.screen_y

        matrix = self.matrix
        mxo = matrix[0]+1
        myo = matrix[1]+1

        rw = scx/mxo # 每条路的宽度
        rh = scy/myo

        sox = sx-rw # 偏移后的当前位置的屏幕坐标
        soy = sy-rw        

        kkx = sox/rw +0.5
        kx = math.floor(kkx)

        kky = soy/rh +0.5
        ky = math.floor(kky)

        # print('坐标',kx,ky)    # 矩阵坐标
        return [kx,ky]


    def pick_b(self,pos_1d,flag,plate):



        rec = -1

        # 如果有劫，要么 更新 ，要么清空


        dead_set = set()
        if(self.pos_legal_1d(pos_1d)):
            that_flag = plate[pos_1d]
            if(that_flag>=1):
                rec = -1    # 已经有子了，判 为弃手
            else:
                # 判断是否禁入，如果禁入，则也判为-1
                rec = pos_1d
                dead_set = self.pre_pick_up(pos_1d,flag,plate)
                # print('ds',dead_set)

                if(len(dead_set)==1):   # 新落子吃了一个子
                    # 先检查劫
                    jie_killer = self.jie[0]
                    jie_dead = self.jie[1]
                    if(self.pos_legal_1d(jie_killer) and self.pos_legal_1d(jie_dead)):
                        # 有劫存在
                        new_killer = pos_1d
                        # new_dead = list(dead_set)[0]
                        if(   jie_killer in dead_set):
                            # 不可落子，触发 劫保护
                            rec = -1

                            # 清除劫
                            
                            self.jie[0] = -1
                            self.jie[1] = -1

                        else:
                            self.jie[0] = pos_1d
                            self.jie[1] = list(dead_set)[0]
                            rec = pos_1d
                    else:
                        # 没有劫
                        self.jie[0] = pos_1d
                        self.jie[1] = list(dead_set)[0]
                        rec = pos_1d

                else:
                    # 吃了0 个或2个或更多子
                    # 清除劫
                    self.jie[0] = -1
                    self.jie[1] = -1

                    

        else:
            # 落子位置 非法
            # 主动弃手


            pass
        

        # 真的落子了
        if(rec>=0):
            plate[rec]=flag

        # 记录
        self.record.append(rec)


        # 返回击杀集合
        return dead_set

    def is_terminal(self):

        out = 0
        if(len(self.record)>=2):
            aa = self.record[-1]
            bb = self.record[-2]

            if(aa==-1 and bb==-1): # 双方 都 弃手时
                out = 1
            else:
                out =0
        return out
    
    def battle_init(self):

        self.record = list()    # 记录对局情况  # 0 2 4 表示 玩家 1 的落子 -1 表示客观弃手。不记录主观的非法行为


        matrix = self.matrix
        self.plate = list()
        plate_len = matrix[0]*matrix[1]
        for i in range(plate_len):
            self.plate.append(0)

        self.flag_count =2  # 围棋 是两个阵营的博弈

        # self.ban_pos = [-1,-1]    # 这个设计不行。


        killer = -1
        dead = -1
        self.jie = [killer,dead]    
        # 对方如果能下在 dead位置 且判断发现 能击杀 killer ，则要判 对方 弃手。
        # 当有一方击杀单个棋子时，就读写这个列表 。
        

    def is_single_self_kill_pos(self,pos,flag,plate):
        # 计算单子自尽点
        out = 0
        dead_set = self.pre_pick_up(pos,flag,plate)
        
        ld = list(dead_set)
        



        if(len(ld)==1):# 如果杀了一个
            if(pos==ld[0]): # 死者的位置是自己的位置
                # 那就是单子自杀
                out = 1
        return out

    def is_territory(self,pos,plate,flag):
        out = 0

        opponent = 3-flag
        that_flag = plate[pos]
        if(that_flag == flag ):
            out = 1
        elif(that_flag==0):
            # 空地
            # 眼是领土的必要条件，但不充分
            if(self.is_single_self_kill_pos(pos,opponent,plate)):
                # print('空地 is_territory',pos,flag)
                out = 1
            else:
                out = 0
        else:
            # 既不是自己的棋子，也不是空地，直接就与自己无关了
            out =0
        return out 

    def count_territory(self,flag,plate):

        territory = 0
        for pos,that_flag in enumerate(plate):
            
            if(self.is_territory(pos,plate,flag)):
                territory+=1
                


        return territory



    def liquidate(self,compensate,plate):

        winner = -1

        ta = self.count_territory(1,plate)
        tb = self.count_territory(2,plate)

        if(ta > tb + compensate):
            winner = 1
        else:
            winner = 2



        return [winner,ta,tb,ta-(tb+compensate)]




    def __init__(self):



        # 显示画面
        self.show_game = 1

        # 画布大小
        # self.screen_x = 1920*0.9
        self.screen_x = 1080*0.9
        self.screen_y = 1080*0.9

        matrix = [9,9] # 列数，行数
        self.matrix = matrix

        table_color = (255,255,64)


        bgc = (255,255,255)
        # bgc = (0,0,0)
        fgc = (255-bgc[0],255-bgc[1],255-bgc[2])

        road_width = self.screen_x/(matrix[0]+1)
        road_height = self.screen_y/(matrix[1]+1)
        

        if(self.show_game):
            #使用pygame之前必须初始化
            pygame.init()
            #设置主屏窗口 ；设置全屏格式：flags=pygame.FULLSCREEN
            self.screen = pygame.display.set_mode((self.screen_x,self.screen_y))
            #设置窗口标题
            pygame.display.set_caption('dva_go')

        
            font = pygame.font.Font(None, 20)
            pre_go = [-2,-2]  # 预览棋子
        
        episode = 0


        player_a = dva_go_rdqn.dva_go_rdqn()


        # flag 0 表示空地 123 表示不同阵营
        # pos_1         -1 表示弃手


        tiemu = 0.5 # 先手方的地盘要比后手方多这么多才行。

        while(1):

            self.battle_init()
            flag = 1
            
            plate = self.plate
            while(1):
                pos_1d = self.random_pos(plate)
                # time.sleep(1)

                dead_set = self.pick_b(pos_1d,flag,plate)


                if(self.is_terminal()):
                    # print('对局结束，开始 清算')
                    # print('棋谱',self.record)
                    result = self.liquidate(tiemu,plate)
                    print('result',result)
                    # time.sleep(1000)
                    break

                flag = 3-flag   # 轮流落子


                # render
                if(self.show_game):
                    self.screen.fill(table_color)
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
                            pygame.draw.circle(self.screen, fgc, pos, go_radius, width=3)


                    s_pos = self.matrix_to_screen(pre_go)
                    pygame.draw.circle(self.screen, 'gray', s_pos, go_radius, width=0)
                        

                    for event in pygame.event.get():    # 关闭游戏
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            sys.exit()


                    pygame.display.flip() #更新屏幕内容


                    # time.sleep(0.1)  # 显卡占用率高，画面卡顿，只能选一个，愚蠢的pygame
                    time.sleep(0.001*0.001)  # 显卡占用率高，画面卡顿，只能选一个，愚蠢的pygame
                # render end

                
                
                self.pick_up(dead_set,plate)


                episode+=1
            # print('over')
        # time.sleep(22)


if __name__ == "__main__":
    # show_game = 1
    dva_go()