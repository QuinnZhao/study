from manimlib import *
import random
import numpy as np

LEN =4
DX = [0,-1,1,0]
DY = [-1,0,0,1]
DIR = [LEFT, UP, DOWN, RIGHT]

class ClickBlock(Button):
    def __init__(self, index:int, scene:Scene,side_length=1.5, **kwargs):
        self.index= index
        self.scene_ctx = scene
        mobject = VGroup(
            Square(side_length=side_length, color=Color(hsl=(random.random(), 0.5, 0.5))),
            Integer(index)
        )
        super(ClickBlock, self).__init__(mobject, self.on_click)
        self.can_move = ORIGIN

    def on_click(self, mob):
        scene = self.scene_ctx
        if np.all(self.can_move == ORIGIN) or scene.on_anim:
            return
        scene.on_anim = True
        scene.play(self.animate.shift(self.can_move * scene.shift_distance), runtime=0.4)
        scene.swap_array_item(0, self.index)
        scene.update_can_move()
        scene.on_anim = False

class GameScene(Scene):
    CONFIG = {
        "side_length": 1.5,
        "buff": 0.2,
        "box_center": ORIGIN,
        "array": np.roll(np.arange(LEN ** 2), -1),
        "on_anim": False
    }


    def init_gamebox(self):
        # 画一个游戏的方块
        gamebox = Square(
            side_length = LEN*self.side_length + (LEN+1) * self.buff
        )
        gamebox.shift(self.box_center)
        self.add(gamebox)
        self.shift_distance = self.side_length + self.buff

    def init_click_block(self):
        self.boxes = Group()
        for i in range(1, LEN**2):
            cb = ClickBlock(i, self, side_length=self.side_length)
            self.boxes.add(cb)
        self.boxes.arrange_in_grid(LEN, LEN, buff = self.buff)
        self.boxes.shift(self.box_center)
        self.add(self.boxes)

    def update_can_move(self):
        for cb in self.boxes:
            cb.can_move = ORIGIN
        zero_index = np.where(self.array == 0)[0][0]
        x, y = zero_index // LEN, zero_index % LEN
        for i in range(LEN):
            new_x, new_y = x + DX[i], y + DY[i]
            if 0 <= new_x < LEN and 0 <= new_y < LEN:
                new_index = new_y + new_x * LEN
                el = self.array[new_index] - 1
                self.boxes[el].can_move = -DIR[i]

    def swap_array_item(self, i, j):
        x = np.where(self.array == i)[0][0]
        y = np.where(self.array == j)[0][0]
        self.array[x], self.array[y] = self.array[y], self.array[x]

    def setup(self):
        self.init_gamebox()
        self.init_click_block()
        self.update_can_move()
