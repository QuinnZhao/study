
__original_author__ = 'iguel Martinez Lopez'
__author__ = 'Quinn Zhao'

from tkinter import PanedWindow as Tk_PanedWindow
from tkinter import VERTICAL, HORIZONTAL
from handle import Vertical_Handle, Horizontal_Handle


# 自定义PanaedWindow类
class PanedWindow(Tk_PanedWindow):
    ORIENT = HORIZONTAL # 默认为水平分割
    HANDLE_CLASS = Horizontal_Handle # 默认为水平方向分割的把手，即垂直方向

    def __init__(self, master, color="gray", size=60, sashpad=2, disallow_dragging=False, on_click=None, image=None,
                 cursor=None, opaqueresize=True):
        Tk_PanedWindow.__init__(self, master, showhandle=False, orient=self.ORIENT, sashpad=sashpad,
                                opaqueresize=opaqueresize)
        self._active_sash = None
        self._on_click = on_click
        self._image = image
        self._color = color
        self._cursor = cursor

        self._configure_callbacks = []

        if not opaqueresize:
            disallow_dragging = True
        self._disallow_dragging = disallow_dragging
        self._handle_list = []
        self._list_of_panes = []

        if self.ORIENT == VERTICAL:
            self._width = size
            self._height = 2 * sashpad
        else:
            self._width = 2 * sashpad
            self._height = size

        if opaqueresize:
            self.bind('<Button-1>', self._on_mark_sash)
            self.bind('<B1-Motion>', self._on_drag_sash)
            self.bind('<ButtonRelease-1>', self._on_release)

    def _on_release(self, event):
        handle_index = self._active_sash
        callback_id1 = self._list_of_panes[handle_index + 1].bind("<Configure>",
            lambda event, handle_index=handle_index: self._on_configure_pane(
                    handle_index), "+")
        callback_id2 = self._list_of_panes[handle_index].bind("<Configure>",
                    lambda event, handle_index=handle_index: self._on_configure_pane(
                                                                  handle_index), "+")
        self._configure_callbacks[handle_index] = (callback_id1, callback_id2)
        self._active_sash = None

    def _on_drag_sash(self, event):
        coord_x = event.x
        coord_y = event.y
        Tk_PanedWindow.sash_place(self, self._active_sash, coord_x, coord_y)
        self._update_position_all_handles()
        return "break"

    def add(self, pane, **kwargs):
        Tk_PanedWindow.add(self, pane, **kwargs)

        self._list_of_panes.append(pane)
        quantity_of_panes = len(self._list_of_panes)
        if quantity_of_panes >= 2:
            handle_index = quantity_of_panes - 2
            handle = self.HANDLE_CLASS(self, handle_index, bg=self._color, height=self._height, width=self._width,
                                       cursor=self._cursor, disallow_dragging=self._disallow_dragging, on_click=self._on_click,
                                       image=self._image)
            if self.ORIENT == VERTICAL:
                handle.place(relx=0.5, anchor="c")
            else:
                handle.place(rely=0.5, anchor="c")
            self._handle_list.append(handle)
            callback_id1 = pane.bind("<Configure>", lambda event, handle_index=handle_index: self._on_configure_pane(handle_index),
                                     "+")
            callback_id2 = self._list_of_panes[handle_index].bind("<Configure>",
                                                                  lambda event, handle_index=handle_index: self._on_configure_pane(
                                                                      handle_index), "+")
            self._configure_callbacks.append((callback_id1, callback_id2))

    def _on_mark_sash(self, event):
        identity = self.identify(event.x, event.y)

        if len(identity) == 2:
            self._active_sash = handle_index = identity[0]
            callback_id1, callback_id2 = self._configure_callbacks[handle_index]

            self._list_of_panes[handle_index + 1].unbind(callback_id1)
            self._list_of_panes[handle_index].unbind(callback_id2)
        else:
            self._active_sash = None

    def _on_configure_pane(self, sash_index):
        x, y = Tk_PanedWindow.sash_coord(self, sash_index)
        if self.ORIENT == VERTICAL:
            self._handle_list[sash_index].place(y=y)
        else:
            self._handle_list[sash_index].place(x=x)

    def _update_position_all_handles(self):
        for sash_index, handle in enumerate(self._handle_list):
            if self.ORIENT == VERTICAL:
                x,y = Tk_PanedWindow.sash_coord(self, sash_index)
                handle.place(y=y)
            else:
                x,y = Tk_PanedWindow.sash_coord(self,sash_index)
                handle.place(x=x)


class Vertical_PanedWindow(PanedWindow):
    '''
    定义垂直分割PanedWindow类
    '''
    ORIENT = VERTICAL
    HANDLE_CLASS = Vertical_Handle

    def _on_configure_pane(self, sash_index):
        '''
        重载基类的相关方法
        :param sash_index:
        :return: None
        '''
        x, y = Tk_PanedWindow.sash_coord(self, sash_index)
        self._handle_list[sash_index].place(y=y)

    def _update_position_all_handles(self):
        '''
        重载基类的相关方法
        :return: None
        '''
        for sash_index, handle in enumerate(self._handle_list):
            x, y = Tk_PanedWindow.sash_coord(self, sash_index)
            handle.place(y=y)


class Horizontal_PanedWindow(PanedWindow):
    '''
    定义水平分割PanedWindow类
    '''
    ORIENT = HORIZONTAL
    HANDLE_CLASS = Horizontal_Handle

    def _update_position_all_handles(self):
        for sash_index, handle in enumerate(self._handle_list):
            x, y = Tk_PanedWindow.sash_coord(self, sash_index)
            handle.place(x=x)

    def _on_configure_pane(self, sash_index):
        x, y = Tk_PanedWindow.sash_coord(self, sash_index)
        self._handle_list[sash_index].place(x=x)
