
# 这个是纯后端文件

# 只定义棋盘，不定义围棋规则

class dva_go():

    def reset():
        plate = list()


    def put_down(self,go_step):
        # 落子 提子 判断终局


    def run(self):
        while(1):
            # self.get_a_go(pos_1d,flag)
            
            go_step = self.client.int_put()    # 流式输入一个棋子 格式 [pos_1d,flag] 一维的
            legal = self.obejective(go_step)
            self.client.send(legal)
            if(legal):
                # 如果客观审查通过
                terminal = self.put_down(go_step)  # 把它放到棋盘上。-1 是虚着，判断终局的逻辑也在里面
                


                # 画面刷新

                if(terminal)
            
        
    # gym的逻辑 rest step(action) 

    def __init__(self):
        colunmn_quantity = 19 # 列数    
        row_quantity = 19 # 行数


        self.plate_len = colunmn_quantity* row_quantity
        # plate= list()



        # self.plate =plate

