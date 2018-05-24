
__original_author__ = 'iguel Martinez Lopez'
__author__ = 'Quinn Zhao'

from tkinter import Frame
from tkinter.ttk import Label


# 定义把手基类
class Handle(Frame):
    def __init__(self, panedwindow, sash_index, disallow_dragging=False, on_click=None, **kw):
        image = kw.pop("image", None) # 取出图片对象，如果不存在则返回None
        Frame.__init__(self, panedwindow, class_="Handle", **kw)
        self._sash_index = sash_index

        if image: # 如果图片对象存在，则加载图片
            self._event_area = Label(self, image=image)
            self._event_area.pack()
        else:
            self._event_area = self

        # 获取PanedWindow的中心点
        self._center = int(self._event_area.winfo_reqwidth() / 2), int(self._event_area.winfo_reqheight() / 2)
        if disallow_dragging: # 如果不允许拖动
            if on_click:
                self._event_area.bind('<Button-1>', lambda event: on_click()) # 绑定鼠标左键点击事件
        else:
            self._event_area.bind('<Button-1>', self._initiate_motion) # 绑定鼠标左键点击事件
            self._event_area.bind('<B1-Motion>', self._on_dragging) # 绑定按住左键拖动事件
            self._event_area.bind('<ButtonRelease-1>', self.master._on_release) # 绑定左键释放事件

    def _initiate_motion(self, event): # 获取拖动前初始位置
        self.master._active_sash = self._sash_index
        self._dx = event.x
        self._dy = event.y

    @property
    def sash_index(self):
        return self._sash_index

    def _on_dragging(self):
        raise NotImplementedError


# 定义竖向把手类
class Vertical_Handle(Handle):
    def _on_dragging(self, event):
        y = event.y_root - self.master.winfo_rooty() - self._dy
        self.master.sash_place(self._sash_index, 1, y)
        self.master._update_position_all_handles()


# 定义横向把手类
class Horizontal_Handle(Handle):
    def _on_dragging(self, event):
        x = event.x_root - self.master.winfo_rootx() - self._dx
        self.master.sash_place(self._sash_index, x, 1)
        self.master._update_position_all_handles()
