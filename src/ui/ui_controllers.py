# -*- coding:utf-8 -*-
from Tkinter import Frame, Button, Pack
import tkMessageBox
# TODO: remove to keep only "right"
from Tkinter import *

EVT_CONTROL_QUIT = 0

class UIControllers(object):
    """
        Add buttons to control the game proceedings
        For the moment, only a "Quit" button is added.
       
    """


    def __init__(self, root):
        # Memorise the root
        self._root = root  
        # Create a new frame only for controllers
        self._frame = Frame(self._root) 
        self._frame.pack(side = RIGHT)
        # Bind the close action with our own callback 
        self._root.protocol("WM_DELETE_WINDOW", self._quit_root)
        self._add_quit_button()


    def _add_quit_button(self):
        """
            Add a button to quit the game
        """
        self._quit = Button(self._frame, text = "Quit",
                                command=self._quit_root)
        self._quit.grid(row = 7, column = 13)


    def _quit_root(self):
        """ 
            Own callback to handle "close window" event 
        """
        # Double check the user intentions
        if tkMessageBox.askokcancel("Quit", "Do you really wish to quit?"):
            # If he's sure (at least twice in a row), quit
            self._root.destroy()
            # Notify the event_engine
            self._event[EVT_UI_PLAYER_LEFT]( \
                    self._hands_id_to_position.index("S"))
            exit(0)