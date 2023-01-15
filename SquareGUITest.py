# -*- coding: utf-8 -*-
"""
Created on Sat Jan 14 22:22:49 2023

@author: chris
"""

from tkinter import *

#root = Tk()

#root.title("Image viewer")

#root.resizable(False, True)

def doNothing():
    return

reduceHeight, addWidth = 49, 26
#root.minsize(400, 400)
#root.maxsize(root.winfo_screenheight(), root.winfo_screenheight())


class Root(Tk):
    def __init__(self):
        super(Root,self).__init__()
        
        
        startHeight = 475
        
        self.title("Python Tkinter")
        self.minsize(500,500)
        
        self.geometry("500x" + str(500))
        
        global ratio
        ratio = 500/startHeight
        
        global lastHeight
        global lastWidth
        lastHeight = startHeight
        lastWidth = 500
    
        
        self.resizable(1, 1)
        
        # self.config(bg = '#add123')
        self.wm_attributes('-transparentcolor','#add123')
        #self.attributes('-alpha', 0.3)
        
        self.bind('<Configure>', self._resize)
        
        # self.maxsize(self.winfo_screenheight(), self.winfo_screenheight()*int(ratio))
        self.maxsize(self.winfo_screenheight()-reduceHeight, self.winfo_screenheight())
        self.wm_aspect(1,1,1,1)
        #self.resizable(1, 0)
        
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
    
    def _resize(self, event):
        '''Modify padding when window is resized.'''
        w, h = event.width, event.height
        #print(w, h)
        
        # if(w != h):
        #     size = str(w) + "x" + str(w)
        #     print(size)
        #     #self.geometry(size)
        global lastHeight
        global lastWidth
        
        #old part
        # if(w/h != ratio and lastHeight != h ):
        #     size = str(w) + "x" + str(int(w*ratio))
        #     print(size)
        #     self.geometry(size)
 
        #     lastHeight = int(w*ratio)
        
        #new control with perfectly fitting height for quadratic image
        if(w/h != ratio and lastHeight != h or lastWidth != w):
            size = str(w) + "x" + str(int(w+addWidth))
            print(size)
            self.geometry(size)
 
            lastHeight = int(w+addWidth)
            lastWidth = int(w)

    
#root.attributes('-toolwindow', True)
#root.overrideredirect(1) # will remove the top badge of window
#root.protocol('WM_DELETE_WINDOW', doNothing)
#asdf = root.attributes('-fullscreen', False)

def _takeImage(c):
    lv_x = c.winfo_rootx()
    lv_y = c.winfo_rooty()
    
    width = c.winfo_width()
    height = c.winfo_height()
    
    #https://www.codespeedy.com/how-to-capture-a-particular-portion-of-a-screen-in-python/
    
    print("Orign positon x and z", lv_x, lv_y)
    print("Width and height:", width, height)


root = Root()

canvas = Canvas(root, width=500, height=500)


button = Button(root, text="Take picture", command=lambda: _takeImage(canvas))
button.grid(row=0, column=0, sticky=E+W)

canvas.config(bg = '#add123')
# canvas.grid(row=1, column=0)
#canvas.grid(row=1, column=0, sticky=N+S+E+W)
# root.grid_columnconfigure(1, weight=1)
# root.grid_rowconfigure(1, weight=1)
canvas.grid(row=1, column=0, rowspan=10, sticky=N+S+E+W)


#canvas.pack(fill="both", expand=True)


#stable diffusion videos
#https://www.youtube.com/watch?v=YsbzglFUEVw
#https://www.youtube.com/watch?v=Xur1JeRjjOI
#https://www.youtube.com/watch?v=oDAVk8QFnWg

#Tkinter tut
#https://www.youtube.com/watch?v=YXPyB4XeYLA&t=636s


root.mainloop()