import default_client
# import queue

import dva_l_queue

class dva_go():

    def reset(game):
        plate = list()

        
        game.plate_len = game.colunmn_quantity* game.row_quantity
        
        blank_flag = -1
        for _ in range(game.plate_len):
            plate.append(blank_flag)


        len = game.flag_quantity*1
        game.patient = dva_l_queue.dva_l_queue(len,1)    #如果连续地虚着，这个队列会全为0，此时游戏结束 
        # for _ in range(game.flag_quantity*1):
        #     patient.put(1)   # 初始化为全1
        # game.patient = patient
        


        game.plate = plate

    def next_flag(game):


        # 换下一个人

        now_flag = game.new_go_flag
        total_flag = game.flag_quantity
        next_flag = (now_flag+1)% total_flag
        game.new_go_flag = next_flag
        return 0

    def put_down(game):
        # 落子 提子 判断终局
        # print('putdown',game.__new_pos_1d,game.new_go_flag)



        
        flag = game.new_go_flag
        pos = game.__new_pos_1d


        if(pos>=0):
            game.plate[pos] = flag
        # 否则 是虚着，直接跳到下一个人走

        return 0
    
    def put_down_go(game):
        flag = game.new_go_flag
        pos = game.__new_pos_1d

        game.plate[pos] = flag
        return 0

    def __obejective_censor(game):
        flag = game.new_go_flag
        pos = game.__new_pos_1d

        # 有子，则不可落
        # 棋局循环，则不可落。这个有点复杂，暂时只用双方单争劫。

        # 两个规则 ，强规则 弱规则 ，强规则要求不能在已有子的地方落子。

        that_flag = game.plate[pos]
        legal = 1

        # print('that_flag',that_flag)
        if(that_flag >=0 ):
            legal = 0
        else:
            # 判断弱规则，其它规则
            pass

        # print('le',legal)
        return legal

    def __is_terminal(game):
        xx = game.patient.sum()
        out = 0
        if(xx == 0):
            out =1
        return out

    # 外部接口，内部不使用 client
    def set_new_go(game,pos):
        game.__new_pos_1d = pos


        return 0        

    def __liquidate(game):
        game.client.win()
        return 

    def run(game):
        if(hasattr(list, 'client')):
            client = game.client
        else:
            client = default_client.default_client()
        client.game = game
        game.client = client
        while(1):
            # game.get_a_go(pos_1d,flag)
            
            client.in_put()    # 流式输入一个棋子 格式 [pos_1d,flag] 一维的
            legal = game.__obejective_censor()
            if(legal):
                # 如果客观审查通过
                # terminal = 
                game.put_down()  # 把它放到棋盘上。-1 是虚着，判断终局的逻辑也在里面
                

                # 画面刷新
                client.show()

                # if(terminal):
                #     break
            # 不合法的落子判断为虚着
            # game.patient.get()
            game.patient.put(legal)
            if(game.__is_terminal()):
                break
            

            game.next_flag()
        game.__liquidate()    # 清算
        
        
    # gym的逻辑 rest state = step(action) 

    def __init__(game):
        # 一些默认配置
        pass
        game.colunmn_quantity = 19 # 列数    
        game.row_quantity = 19 # 行数


        game.new_go_flag = 0
        game.flag_quantity = 2  # 一共有几个阵营？
        # plate= list()


        game.reset()
        # game.plate =plate

