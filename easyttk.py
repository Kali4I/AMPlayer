# -*- coding: utf-8 -*-
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# EasyTTK - make tkinter.ttk easy!
# Author: Ivan Sobolev
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from tkinter import Text,Listbox,Tk
from tkinter.ttk import Style
from tkinter.constants import *

def WEntry(parent='root', side=TOP, text=None, width=None, align=CENTER, expand=None, fill=None, textstyle=None, **options):
    from tkinter.ttk import Entry,Label
    if text:
        l = Label(parent, text=text)
        l.pack(side=side)
        if textstyle:
            l.config(style=textstyle)
    __entry__ = Entry(parent, justify=align, **options)
    if width:
        __entry__.config(width=width)
    __entry__.pack(side=side,fill=fill,expand=expand)
    return __entry__
    
def WButton(parent='root', side=TOP, text=None, width=None, height=None, expand=None, fill=None, **options):
    from tkinter.ttk import Button
    __button__ = Button(parent, text=text, **options)
    if width:
        __button__.config(width=width)
    if height:
        __button__.config(height=height)
    __button__.pack(side=side,fill=fill,expand=expand)
    return __button__

def WLabel(parent='root', side=TOP, text=None, expand=None, fill=None, **options):
    from tkinter.ttk import Label
    __label__ = Label(parent, text=text, **options)
    __label__.pack(side=side,fill=fill,expand=expand)
    return __label__
    
def WEditor(parent='root', side=TOP, text=None, width=None, height=None, scrollbar=None, expand=None, fill=None, **options):
    from tkinter.ttk import Frame,Label,Scrollbar
    frame = Frame(parent)
    if text:
        label = Label(frame, text=text)
        label.pack(side=TOP)
    __editor__ = Text(frame, **options)
    vertbar = Scrollbar(frame)
    vertbar['command'] = __editor__.yview
    if width:
        __editor__.config(width=width)
    if height:
        __editor__.config(height=height)
    if scrollbar:
        vertbar.pack(side=scrollbar,fill='both')
    __editor__.pack(side=BOTTOM,fill=fill,expand=expand)
    frame.pack(side=side,fill=fill,expand=expand)
    return __editor__
    
    # Радио-кнопка
def WRadio(parent='root', side=TOP, text='Radiobutton', var=None, val=None, expand=None, fill=None, **options):
    from tkinter.ttk import Radiobutton
    __radiobutton__ = Radiobutton(parent,text=text,variable=var,value=val, **options)
    __radiobutton__.pack(side=side,fill=fill,expand=expand)
    return __radiobutton__
    
    # Кнопка-галочка
def WCheck(parent='root', side=TOP, text='Checkbutton', var=None, val_on=None, val_off=None, expand=None, fill=None, **options):
    from tkinter.ttk import Checkbutton
    __checkbutton__ = Checkbutton(parent,text=text, variable=var, onvalue=val_on, offvalue=val_off, **options)
    __checkbutton__.pack(side=side,fill=fill,expand=expand)
    return __checkbutton__

    # Рамка
def WFrame(parent='root', side=TOP, width=None, height=None, expand=None, fill=None, **options):
    from tkinter.ttk import Frame
    __frame__ = Frame(parent, **options)
    if width:
        __frame__.config(width=width)
    if height:
        __frame__.config(height=height)
    __frame__.pack(side=side,fill=fill,expand=expand)
    return __frame__

def NoBorderWindow(root,button=RIGHT,btnclr='red',btnstyle='FLAT',clr='#a3a3a3',title=None,titleclr='lightgray',titlealign=RIGHT,bar_height=None):
    from tkinter.ttk import Style,Frame,Label,Button
    root.overrideredirect(True)
    
    def movewindow(event):
        root.geometry('+{0}+{1}'.format(event.x_root - windowbar.winfo_width() // 2, event.y_root - windowbar.winfo_height() // 2))
    
    Style().configure("WinFrame.TFrame", relief="flat", background=clr)
    Style().configure("WinFrame2.TLabel", relief="flat", background=titleclr)
    bar = Frame(root,style='WinFrame.TFrame').pack(side=TOP, fill=X)
    windowbar = Label(bar, style='WinFrame.TFrame')
    windowbar.pack(side=TOP, fill=X)
    windowbar.bind('<B1-Motion>', movewindow)
    
    x = (root.winfo_screenwidth() - root.winfo_reqwidth()) / 2
    y = (root.winfo_screenheight() - root.winfo_height()) / 4
    root.geometry("+%d+%d" % (x, y))
    
    if button:
        if btnstyle == 'FLAT':
            from tkinter.ttk import Button as ttkButton
            WStyleMap("QuitButton.TLabel",
            foreground=[('pressed', 'black'),('active', 'lightgray'),('!disabled','gray')],
            background=[('pressed', 'darkred'),('active', 'red'),('!disabled','#F0F0F0')])
            WStyle("QuitButton.TLabel",font='System 10')
            Style().configure("QuitButton.TLabel", relief="flat", background=btnclr,font='System 10')
            __quit__ = ttkButton(windowbar,text='    X',width=5,style='QuitButton.TLabel',command=lambda:root.destroy())
            __quit__.pack(side=button)
            
        elif btnstyle == 'TCL_TK':
            def quitApp_(event):
                root.destroy()
                return None
            from tkinter import Button as tkButton
            __quit__ = tkButton(windowbar,text='X',width=3,relief=GROOVE,background=btnclr)
            __quit__.bind('<Button-1>',quitApp_)
            __quit__.pack(side=button)
        elif btnstyle == 'WIN32':
            Style().configure("WinFrameButton.TButton", relief="flat", background=btnclr,font='System 10')
            from tkinter.ttk import Button as ttkButton
            __quit__ = ttkButton(windowbar,text='X',width=3,style=btnstyle,command=lambda:root.destroy())
            __quit__.pack(side=button)
           
    if title:
        __wintitle__ = WLabel(windowbar,side=titlealign,text=title,style='WinFrame2.TLabel')
        __wintitle__.bind('<B1-Motion>', movewindow)
    return windowbar
    
    # Статусбар
def WStatusbar(parent='root', **options):
    from tkinter.ttk import Label
    __statusbar__ = Label(parent, **options)
    def movewindow(event):
        parent.geometry('+{0}+{1}'.format(event.x_root - __statusbar__.winfo_width() // 2, event.y_root - __statusbar__.winfo_height() // 2))
    __statusbar__.pack(side='bottom', fill=X)
    __statusbar__.bind('<B1-Motion>',movewindow)
    return __statusbar__

    # Тулбар
def WToolbar(parent='root', **options):
    from tkinter.ttk import Frame,Label
    bar = Frame(parent)
    bar.pack(side=TOP, fill=X)
    __toolbar__ = Label(bar, **options)
    __toolbar__.pack(side=TOP, fill=X)
    return __toolbar__

def WListbox(parent='root',side=TOP, scrollbar=None, fill=None, expand=None, width=None, height=None, **options):
    from tkinter.ttk import Frame,Label,Scrollbar
    frame = Frame(parent)
    __listbox__ = Listbox(frame, **options)
    bar = Scrollbar(frame)
    bar['command'] = __listbox__.yview
    __listbox__['yscrollcommand'] = bar.set
    if width:
        __listbox__.config(width=width)
    if height:
        __listbox__.config(height=height)
    if scrollbar:
        bar.pack(side=scrollbar,fill='both')
    __listbox__.pack(side=BOTTOM,fill=fill,expand=expand)
    frame.pack(side=side, fill=fill,expand=expand)
    return __listbox__
    
def WScale(parent='root',side=TOP,fill=None,expand=None,length=None,from_=0,to=10,orient=HORIZONTAL,resolution=None, **options):
    from tkinter.ttk import Scale
    __scale__ = Scale(parent,from_=from_, to=to, orient=orient, resolution=resolution, **options)
    __scale__.pack(side=side, fill=fill, expand=expand)
    return __scale__
    
def WStyle(name='ttkWidgets.TButton', r='FLAT', **options):
    from tkinter.ttk import Style
    return Style().configure(name, relief=r, **options)
    
def WStyleMap(name='ttkWidgets.TButton', **options):
    from tkinter.ttk import Style
    return Style().map(name, **options)
            
def WProgressbar(parent='root',side=TOP,fill=None,expand=None,text=None,orient='horizontal',length=200,mode="indeterminate",max=100,variable=None,**options):
    from tkinter.ttk import Label,Progressbar
    if text:
        label = WLabel(parent, side=side,text=text)
    __progressbar__ = Progressbar(parent, orient=orient,length=length, mode=mode,maximum=max, **options)
    __progressbar__.pack(side=side, fill=fill, expand=expand)
    return __progressbar__
    
def WCombobox(parent='root',side=TOP,fill=None,expand=None,text=None,**options):
    from tkinter.ttk import Label,Combobox
    if text:
        label = Label(frame, text=text)
        label.pack(side=TOP)
    __combobox__ = Combobox(parent, **options)
    __combobox__.pack(side=side, fill=fill, expand=expand)
    return __combobox__
    
def WSeparator(parent='root',side=TOP,fill=None,expand=None,**options):
    from tkinter.ttk import Separator
    __sep__ = Separator(parent, **options)
    __sep__.pack(side=side,fill=fill,expand=expand)
    return __sep__

def WCanvas(parent='root',side=TOP,expand=None,fill=None,**options):
    from tkinter import Canvas
    __canvas__ = Canvas(parent,**options)
    __canvas__.pack(side=side,expand=expand,fill=fill)
    return __canvas__

def example():
    from tkinter import IntVar
    root = Tk()
    WStyle('Statusbar.TLabel',background='lightgray')
    
    _radio_button_ = None
    _check_button_ = None
    pgrbar = IntVar()
    
    NoBorderWindow(root,title='EasyTTK v1.4')
    
    status = WStatusbar(root,style='Statusbar.TLabel')
    tools = WToolbar(root)
    
    def button_clicked():
        print('Works!')
    
    stblbl = WLabel(status, TOP, text='Text label in statusbar.',style='Statusbar.TLabel')
    b = WButton(root, TOP, text="Button",fill=None,command=lambda:button_clicked())
    e = WEditor(root, TOP, text='Text editor:',width=20,height=5,scrollbar=RIGHT)
    WEntry(root, TOP, text='Text field:',fill=X)
    WLabel(tools, TOP, text='Text label in toolbar.')
    WCheck(root, TOP, var=_check_button_, val_on=True, val_off=False, expand=None)
    WRadio(root, TOP, fill='both', state=ACTIVE, text='First Radiobutton', var=_radio_button_, val='первая')
    WRadio(root, TOP, fill='both', state=ACTIVE, text='Second Radiobutton', var=_radio_button_, val='вторая')
    lb = WListbox(root,height=5,width=30,scrollbar=RIGHT)
    sc = WScale(root,TOP,length=10,from_=0,to=10,fill=X)
    pgrbar = sc.get()
    progressbar_1 = WProgressbar(root,TOP,length=200,text='indeterminate',mode='indeterminate',variable=pgrbar)
    progressbar_2 = WProgressbar(root,TOP,length=200,text='determinate',mode='determinate',variable=pgrbar)
    progressbar_1.start(10)
    progressbar_2.start(10)
    
    WCombobox(root,TOP)
    
    for i in 'EasyTTK':
        lb.insert(END,'TEST | '+i)
    
    root.resizable(width=False, height=False)
    root.title('EasyTTK 1.4')
    root.mainloop()
    
if __name__ == "__main__":
    example()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    