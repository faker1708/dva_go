

import pygame


# 需求
# 接收 一个数组，表示棋局状态，把它显示到窗口中
# 接收用户的输入


class dva_go_front_pygame():

    def fa(self):
    
        bg_color = (255,255,64) # 深黄
        line_color = (0,0,0)    # 黑


        mx = self.colunmn_quantity
        my = self.row_quantity
        
        road_width = self.screen_x/(mx+1)
        road_height = self.screen_y/(my+1)
        
    def in_put(self):

        return


    def __init__(self):
        kk = 0.8
        self.screen_x = 1080*kk
        self.screen_y = 1080*kk


        # 棋盘大小
        self.plate_x = 777
        self.plate_y = 777

        # 棋盘偏置

        self.plate_offset_x = 99
        self.plate_offset_y = 99

        

        # self.dva_go.colunmn_quantity = 19
        # self.dva_go.row_quantity = 19

