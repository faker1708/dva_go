import sys
import pygame
import time
import random
import dqn
import torch
import numpy as np

import matplotlib.pyplot as plt
import pickle


class dva_go():
    
    # 标注坐标轴
    def draw_axes(self,):
        if self.screen:
            font = pygame.font.Font(None, 20)

            for i in range(11):
                # x轴
                text = font.render(str(i), True, (0, 0, 0))
                # self.screen.blit(text, (i * self.Cell[0], 0))
                pygame.draw.line(self.screen, (0, 0, 0), (i * 10, 0), (i * self.Cell[0], self.Size[1]))
                # y轴
                text = font.render(str(i), True, (0, 0, 0))
                # self.screen.blit(text, (0, i * self.Cell[1]))
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * 10), (self.Size[0], i * self.Cell[1]))
                

    def __init__(self):


        # 数据编码
        self.show_game = 1

        # 画布大小
        self.world_x = 400
        self.world_y = 400


        matrix = [9,9]

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
        
        while(1):
            if(self.show_game):
                self.screen.fill('black')

                font = pygame.font.Font(None, 20)

                for j in range(0,2):
                    for i in range(matrix[j]):
                        
                        # 轴号
                        text = font.render(str(i), True, 'white')
                        text_x = i * road_width+ road_width
                        text_y = road_height/2
                        
                        if(j==1):
                            txx = text_y
                            text_y = text_x
                            text_x = txx
                        
                        self.screen.blit(text, (text_x, text_y))



                        start_pos = (road_width,road_width*(i+1))
                        # end_pos = (road_width * (matrix[0]-1),road_width*(i+1))
                        end_pos = (road_width*matrix[0],road_width*(i+1))
                        if(j==1):
                            start_pos = (road_width*(i+1),road_width)
                            end_pos = (road_width*(i+1),road_width*matrix[0])
                        pygame.draw.line(self.screen, 'white', start_pos,end_pos, 1)




                pygame.display.flip() #更新屏幕内容
                for event in pygame.event.get():    # 关闭游戏
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()

        time.sleep(22)


if __name__ == "__main__":
    dva_go()