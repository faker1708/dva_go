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
                self.screen.blit(text, (i * self.Cell[0], 0))
                pygame.draw.line(self.screen, (0, 0, 0), (i * self.Cell[0], 0), (i * self.Cell[0], self.Size[1]))
                # y轴
                text = font.render(str(i), True, (0, 0, 0))
                self.screen.blit(text, (0, i * self.Cell[1]))
                pygame.draw.line(self.screen, (0, 0, 0), (0, i * self.Cell[1]), (self.Size[0], i * self.Cell[1]))
                

    def __init__(self):


        # 数据编码
        self.show_game = 1
        self.wolrd_x = 19
        self.wolrd_y = 19

        
        if(self.show_game):
            #使用pygame之前必须初始化
            pygame.init()
            #设置主屏窗口 ；设置全屏格式：flags=pygame.FULLSCREEN
            self.screen = pygame.display.set_mode((self.world_x,self.world_y))
            #设置窗口标题
            pygame.display.set_caption('dva_go')
            self.draw_axes()
            




if __name__ == "__main__":
    dva_go()