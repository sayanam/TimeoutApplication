#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.2
#  in conjunction with Tcl version 8.6
#    Feb 25, 2020 10:11:44 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import TimeoutSupport
import os


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    TimeoutSupport.set_Tk_var()
    top = Toplevel1 (root)
    TimeoutSupport.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    TimeoutSupport.set_Tk_var()
    top = Toplevel1 (w)
    TimeoutSupport.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        #iconsDir = os.getcwd().replace('UILayer', 'icons')
        iconsDir = os.getcwd()+'\icons'
        #background_color = '#fd4267'
        background_color = '#AEB6BF'
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "-family {Segoe Script} -size 16 -weight bold"
        font7 = "-family {Segoe Script} -size 12 -weight bold"
        font4 = "-family {Segoe Script} -size 9 -weight bold"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("1304x745+54+-11")
        top.minsize(120, 1)
        top.maxsize(1370, 749)
        top.resizable(1, 1)

        top.title("Timeout App - Take a break !!")
        top.configure(background=background_color)
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.TSeparator1 = ttk.Separator(top)
        self.TSeparator1.place(relx=0.007, rely=0.094, relwidth=0.989)

        self.TEntry1 = ttk.Entry(top)
        self.TEntry1.place(relx=0.046, rely=0.121, relheight=0.042, relwidth=0.426)
        self.TEntry1.configure(takefocus="")
        self.TEntry1.configure(cursor="ibeam")
        tooltip_font = "TkDefaultFont"
        ToolTip(self.TEntry1, tooltip_font, '''Enter URL here''', delay=0.5)

        self.UploadButton = tk.Button(top)
        self.UploadButton.place(relx=0.475, rely=0.121, height=33, width=49)
        self.UploadButton.configure(command=TimeoutSupport.UploadUrl)
        self.UploadButton.configure(activebackground="#ececec")
        self.UploadButton.configure(activeforeground="#000000")
        self.UploadButton.configure(background=background_color)
        self.UploadButton.configure(borderwidth=0)
        self.UploadButton.configure(disabledforeground="#a3a3a3")
        self.UploadButton.configure(foreground="#000000")
        self.UploadButton.configure(highlightbackground="#d9d9d9")
        self.UploadButton.configure(highlightcolor="black")
        self.UploadButton.configure(pady="0")
        global uploadImage
        uploadImage = tk.PhotoImage(file=os.path.join(iconsDir, 'plus-green.png'))
        self.UploadButton.configure(image=uploadImage)
        self.UploadButton.configure(text='Upload')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.UploadButton, tooltip_font, '''Upload Url''', delay=0.5)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.015, rely=0.027, height=41, width=270)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background=background_color)
        #self.Label1.configure(compound='center')
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font=font9)
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(justify='left')
        self.Label1.configure(text='Welcome ' + TimeoutSupport.userName)

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.stopButton = tk.Button(top)
        self.stopButton.place(relx=0.038, rely=0.336, height=60, width=60)
        self.stopButton.configure(activebackground="#ececec")
        self.stopButton.configure(activeforeground="#000000")
        self.stopButton.configure(background=background_color)
        self.stopButton.configure(command=TimeoutSupport.stop)
        self.stopButton.configure(disabledforeground="#a3a3a3")
        self.stopButton.configure(foreground="#000000")
        self.stopButton.configure(highlightbackground="#d9d9d9")
        self.stopButton.configure(highlightcolor="black")
        self.stopButton.configure(pady="0")
        self.stopButton.configure(borderwidth="0")
        global stopImage
        stopImage = tk.PhotoImage(file=os.path.join(iconsDir, 'stop-lightBlue.png'))
        self.stopButton.configure(image=stopImage)
        self.stopButton.configure(text='''Stop''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.stopButton, tooltip_font, '''Stops Playlist''', delay=0.5)

        self.Button2 = tk.Button(top)
        self.Button2.place(relx=-0.107, rely=0.537, height=24, width=47)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="black")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Button''')

        self.startButton = tk.Button(top)
        self.startButton.place(relx=0.038, rely=0.228, height=60, width=60)
        self.startButton.configure(activebackground="#ececec")
        self.startButton.configure(activeforeground="#000000")
        self.startButton.configure(background=background_color)
        self.startButton.configure(command=TimeoutSupport.start)
        self.startButton.configure(disabledforeground="#a3a3a3")
        self.startButton.configure(foreground="#000000")
        self.startButton.configure(highlightbackground="#d9d9d9")
        self.startButton.configure(highlightcolor="black")
        self.startButton.configure(pady="0")
        self.startButton.configure(borderwidth="0")
        global startImage
        startImage = tk.PhotoImage(file=os.path.join(iconsDir, 'play-lightblue.png'))
        self.startButton.configure(image= startImage)
        self.startButton.configure(text = 'Start')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.startButton, tooltip_font, '''Start Playlist''', delay=0.5)


        self.shuffleButton = tk.Button(top)
        self.shuffleButton.place(relx=0.038, rely=0.443, height=60, width=60)
        self.shuffleButton.configure(activebackground="#ececec")
        self.shuffleButton.configure(activeforeground="#000000")
        self.shuffleButton.configure(background=background_color)
        self.shuffleButton.configure(command=TimeoutSupport.Shuffle)
        self.shuffleButton.configure(disabledforeground="#a3a3a3")
        self.shuffleButton.configure(foreground="#000000")
        self.shuffleButton.configure(highlightbackground="#d9d9d9")
        self.shuffleButton.configure(highlightcolor="black")
        self.shuffleButton.configure(pady="0")
        self.shuffleButton.configure(borderwidth="0")
        global shuffleImage
        shuffleImage = tk.PhotoImage(file=os.path.join(iconsDir, 'shuffle.png'))
        self.shuffleButton.configure(image=shuffleImage)
        self.shuffleButton.configure(text='''Shuffle''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.shuffleButton, tooltip_font, '''Shuffles Playlist''', delay=0.5)

        # History Listbox
        self.Scrolledlistbox2 = ScrolledListBox(top)
        self.Scrolledlistbox2.place(relx=0.0, rely=0.644, relheight=0.342, relwidth=0.553)
        self.Scrolledlistbox2.configure(background="#d2d2d2")
        self.Scrolledlistbox2.configure(cursor="xterm")
        self.Scrolledlistbox2.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox2.configure(font="TkFixedFont")
        self.Scrolledlistbox2.configure(foreground="black")
        self.Scrolledlistbox2.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox2.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox2.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox2.configure(selectforeground="black")
        for item in TimeoutSupport.userHistoryData:
            temp = item.date + '  ' +item.action + '  '+ item.itemName
            self.Scrolledlistbox2.insert(tk.END, temp)

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.698, rely=0.215, height=24, width=184)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background=background_color)
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(font=font7)
        self.Label3.configure(text='''Playlist''')

        self.Spinbox1 = tk.Spinbox(top, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.859, rely=0.121, relheight=0.027
                , relwidth=0.065)
        self.Spinbox1.configure(activebackground="#f9f9f9")
        self.Spinbox1.configure(background="white")
        self.Spinbox1.configure(buttonbackground="#d9d9d9")
        self.Spinbox1.configure(disabledforeground="#a3a3a3")
        self.Spinbox1.configure(font="TkDefaultFont")
        self.Spinbox1.configure(foreground="black")
        self.Spinbox1.configure(highlightbackground="black")
        self.Spinbox1.configure(highlightcolor="black")
        self.Spinbox1.configure(insertbackground="black")
        self.Spinbox1.configure(selectbackground="#c4c4c4")
        self.Spinbox1.configure(selectforeground="black")
        self.Spinbox1.configure(textvariable=TimeoutSupport.spinbox)
        self.value_list = ['5','10','20','30','40','50']
        self.Spinbox1.configure(values=self.value_list)


        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.782, rely=0.121, height=21, width=94)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background=background_color)
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(borderwidth = 0)
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(font=font4)
        self.Label4.configure(text='''Interval (sec)''')

        # Playlist scrollList
        self.Scrolledlistbox1 = ScrolledListBox(top, selectmode = tk.EXTENDED)
        self.Scrolledlistbox1.place(relx=0.552, rely=0.255, relheight=0.733, relwidth=0.446)
        self.Scrolledlistbox1.configure(background='#d2d2d2')#white
        self.Scrolledlistbox1.configure(cursor="xterm")
        self.Scrolledlistbox1.configure(disabledforeground="#a3a3a3")
        self.Scrolledlistbox1.configure(font="TkFixedFont")
        self.Scrolledlistbox1.configure(foreground="black")
        self.Scrolledlistbox1.configure(highlightbackground="#d9d9d9")
        self.Scrolledlistbox1.configure(highlightcolor="#d9d9d9")
        self.Scrolledlistbox1.configure(selectbackground="#c4c4c4")
        self.Scrolledlistbox1.configure(selectforeground="black")
        for item in TimeoutSupport.playlistData:
            self.Scrolledlistbox1.insert(tk.END,item.songname)

        self.DeleteButton = tk.Button(top)
        self.DeleteButton.place(relx=0.52, rely=0.188, height=44, width=97)
        self.DeleteButton.configure(activebackground="#ececec")
        self.DeleteButton.configure(activeforeground="#000000")
        self.DeleteButton.configure(background=background_color)
        self.DeleteButton.configure(command=TimeoutSupport.deletePlaylistElements)
        self.DeleteButton.configure(disabledforeground="#a3a3a3")
        self.DeleteButton.configure(foreground="#000000")
        self.DeleteButton.configure(highlightbackground="#d9d9d9")
        self.DeleteButton.configure(highlightcolor="black")
        self.DeleteButton.configure(borderwidth=0)
        self.DeleteButton.configure(pady="0")
        global deleteImage
        deleteImage = tk.PhotoImage(file=os.path.join(iconsDir, 'recycle-bin.png'))
        self.DeleteButton.configure(image=deleteImage)
        self.DeleteButton.configure(text='''Delete''')
        tooltip_font = "TkDefaultFont"
        ToolTip(self.DeleteButton, tooltip_font, '''Deletes the selected elements of playlist''', delay=0.5)

        self.TimerLabel = tk.Label(top)
        self.TimerLabel.place(relx=0.176, rely=0.309, height=71, width=310)
        self.TimerLabel.configure(background=background_color)
        self.TimerLabel.configure(font='-family {Terminal} -size 18 -weight bold')
        self.TimerLabel.configure(disabledforeground="#a3a3a3")
        #self.TimerLabel.configure(foreground="#fafd84")
        self.TimerLabel.configure(foreground="#000000")
        self.TimerLabel.configure(text='''00:00''')

        self.HistoryLabel = tk.Label(top)
        self.HistoryLabel.place(relx=0.008, rely=0.604, height=21, width=114)
        self.HistoryLabel.configure(background=background_color)
        self.HistoryLabel.configure(disabledforeground="#a3a3a3")
        self.HistoryLabel.configure(foreground="#000000")
        self.HistoryLabel.configure(font=font7)
        self.HistoryLabel.configure(text='''User History''')

# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================

from time import time, localtime, strftime

class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()

# ===========================================================
#                   End of Class ToolTip
# ===========================================================

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''
    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))
        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')
        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)
        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()
        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledListBox(AutoScroll, tk.Listbox):
    '''A standard Tkinter Listbox widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        tk.Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)
    def size_(self):
        sz = tk.Listbox.size(self)
        return sz



import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()