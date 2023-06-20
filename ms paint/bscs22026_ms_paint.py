from ast import Lambda
from email.mime import image
from optparse import Option
from turtle import color
from types import NoneType
from PIL import Image, ImageDraw, ImageTk, ImageGrab
import PIL
import math
from tkinter import *
from tkinter import colorchooser
from tkinter import filedialog
from queue import Queue
from tkinter import simpledialog


WHITE=(255,255,255)


#from PIL import Image 
#from pillow import image  

class PaintApp:
    def __init__(self,width,height,title):
        self.screen = Tk()
        self.screen.resizable(False,False)
        self.screen.iconbitmap(r'paint.ico')
        self.screen.title(title)
        self.screen.geometry(str(width)+'x'+str(height))
        self.pencil_pic=PhotoImage(file='pencil.png')
        self.eraser_pic=PhotoImage(file='eraser.png')
        self.brush_pic=PhotoImage(file='brush.png')
        self.picker_pic=PhotoImage(file='picker.png')
        self.bucket_pic=PhotoImage(file='bucket.png')
        self.zoom_pic=PhotoImage(file='zoom.png')
        self.save_pic=PhotoImage(file='save.png')
        self.load_pic=PhotoImage(file='load.png')
        self.wheel_pic=PhotoImage(file='wheel.png')
        self.undo_pic=PhotoImage(file='undo.png')
        self.selection_pic=PhotoImage(file='selection.png')
        self.clear_pic=PhotoImage(file='clear.png')
        self.circle_pic=PhotoImage(file='circle.png')
        self.oval_pic=PhotoImage(file='oval.png')
        self.square_pic=PhotoImage(file='square.png')
        self.rectangle_pic=PhotoImage(file='rectangle.png')
        self.line_pic=PhotoImage(file='line.png')
        self.triangle_pic=PhotoImage(file='triangle.png')
        self.rtriangle_pic=PhotoImage(file='rtriangle.png')
        self.pentagon_pic=PhotoImage(file='pentagon.png')
        self.hexagon_pic=PhotoImage(file='hexagon.png')
        self.diamond_pic=PhotoImage(file='diamond.png')
        self.star_pic=PhotoImage(file='star.png')
        self.npoly_pic=PhotoImage(file='npoly.png')






        self.image = PIL.Image.new("RGB", (width, height), WHITE)
        self.draw = ImageDraw.Draw(self.image)
       
        #---------Variable------------

        self.stroke_color = StringVar()
        self.stroke_color.set("black")

        self.fill_color = StringVar()
        self.fill_color.set("white")

        self.wall=None
        self.flag=False

        self.shapes=[]

        self.pfill_color = StringVar()
        self.pfill_color.set("white")

        self.pstroke_color = StringVar()
        self.pstroke_color.set("black")

        self.x, self.y = None, None

        self.szopt=[2,4,6,8,10]

        self.stroke_size = IntVar()
        self.stroke_size.set(4)

        
        self.ty=StringVar()
        self.ty.set("s")

        self.shape_id=None
        

        #----------Frame 1 Buttons------------
        self.frame1 = Frame(self.screen,width=1100,height=100)
        self.frame1.grid(row=0,column=0,sticky=NW)
        
        #Tool Frame
        self.toolframe=Frame(self.frame1,width=100,height=100,relief=SUNKEN, borderwidth=3)
        self.toolframe.grid(row=0,column=0)
        self.pencil=Button(self.toolframe,image=self.pencil_pic,height=30,width=30,command=self.on_PencilButton_Presed)
        self.pencil.grid(row=0,column=0)
        self.eraser=Button(self.toolframe,image=self.eraser_pic,height=30,width=30,command=self.on_EraserButton_Presed)
        self.eraser.grid(row=1,column=0)
        self.marker=Button(self.toolframe,image=self.brush_pic,height=30,width=30,command=self.on_markerButton_Presed)
        self.marker.grid(row=2,column=0)
        self.colorPicker=Button(self.toolframe,image=self.picker_pic,height=30,width=30,command=self.on_clrpickButton_Pressed)
        self.colorPicker.grid(row=0,column=1)
        self.bucket=Button(self.toolframe,image=self.bucket_pic,height=30,width=30,command=self.on_bucketButton_Pressed)
        self.bucket.grid(row=1,column=1)
        self.zoom=Button(self.toolframe,image=self.zoom_pic,height=30,width=30,command=self.on_zoomButton_Pressed)
        self.zoom.grid(row=2,column=1)

        #Size Frame
        self.sizeframe=Frame(self.frame1,width=100,height=100,relief=SUNKEN, borderwidth=3)
        self.sizeframe.grid(row=0,column=1)
        self.size=OptionMenu(self.sizeframe,self.stroke_size,*self.szopt)
        self.size.grid(row=1,column=0)
        self.sizelb=Label(self.sizeframe,text="Size",width=5)
        self.sizelb.grid(row=0,column=0)

        #Shape Frame
        self.shapeframe=Frame(self.frame1,width=200,height=100,relief=SUNKEN, borderwidth=3)
        self.shapeframe.grid(row=0,column=2)
        self.circle=Button(self.shapeframe,image=self.circle_pic,height=30,width=30,command=self.on_CircleButton_Pressed)
        self.circle.grid(row=0,column=0)
        self.oval=Button(self.shapeframe,text="oval",image=self.oval_pic,height=30,width=30,command=self.on_OvalButton_Pressed)
        self.oval.grid(row=1,column=0)
        self.square=Button(self.shapeframe,text="square",image=self.square_pic,height=30,width=30,command=self.on_SquareButton_Pressed)
        self.square.grid(row=2,column=0)
        self.rectangle=Button(self.shapeframe,text="rectangle",image=self.rectangle_pic,height=30,width=30,command=self.on_RectangleButton_Pressed)
        self.rectangle.grid(row=0,column=1)
        self.line=Button(self.shapeframe,text="line",image=self.line_pic,height=30,width=30,command=self.on_LineButton_Pressed)
        self.line.grid(row=1,column=1)
        self.triangle=Button(self.shapeframe,text="triangle",image=self.triangle_pic,height=30,width=30,command=self.on_TriangleButton_Pressed)
        self.triangle.grid(row=2,column=1)
        self.rttriangle=Button(self.shapeframe,text="rtriangle",image=self.rtriangle_pic,height=30,width=30,command=self.on_rtTriangleButton_Pressed)
        self.rttriangle.grid(row=0,column=2)
        self.pentagon=Button(self.shapeframe,text="pentagon",image=self.pentagon_pic,height=30,width=30,command=self.on_PentagonButton_Pressed)
        self.pentagon.grid(row=1,column=2)
        self.hexagon=Button(self.shapeframe,text="hexagon",image=self.hexagon_pic,height=30,width=30,command=self.on_HexagonButton_Pressed)
        self.hexagon.grid(row=2,column=2)
        self.dimond=Button(self.shapeframe,text="dimond",image=self.diamond_pic,height=30,width=30,command=self.on_DimondButton_Pressed)
        self.dimond.grid(row=0,column=3)
        self.star=Button(self.shapeframe,text="star",image=self.star_pic,height=30,width=30,command=self.on_StarButton_Pressed)
        self.star.grid(row=1,column=3)
        self.npoly=Button(self.shapeframe,text="n",image=self.npoly_pic,height=30,width=30,command=self.on_npolyButton_Pressed)
        self.npoly.grid(row=2,column=3)

        #Color Frame
        self.colorframe=Frame(self.frame1,width=200,height=100,relief=SUNKEN, borderwidth=3)
        self.colorframe.grid(row=0,column=3)
        self.stroke=Button(self.colorframe,text="",width=5,command=self.stroke_button,bg=self.stroke_color.get())
        self.stroke.grid(row=0,column=0)
        self.fill=Button(self.colorframe,text="",width=5,command=self.fill_button, bg=self.fill_color.get())
        self.fill.grid(row=2,column=0)
        self.red=Button(self.colorframe,text="",width=5,command=self.red_button, bg="red")
        self.red.grid(row=0,column=1)
        self.blue=Button(self.colorframe,text="",width=5,command=self.blue_button,bg="blue")
        self.blue.grid(row=1,column=1)
        self.yellow=Button(self.colorframe,text="",width=5,command=self.yellow_button,bg="yellow")
        self.yellow.grid(row=2,column=1)
        self.green=Button(self.colorframe,text="",width=5,command=self.green_button,bg="green")
        self.green.grid(row=0,column=2)
        self.brown=Button(self.colorframe,text="",width=5,command=self.brown_button ,bg="brown")
        self.brown.grid(row=1,column=2)
        self.pink=Button(self.colorframe,text="",width=5,command=self.pink_button ,bg="pink")
        self.pink.grid(row=2,column=2)
        self.purple=Button(self.colorframe,text="",width=5,command=self.purple_button ,bg="purple")
        self.purple.grid(row=0,column=3)
        self.lime=Button(self.colorframe,text="",width=5,command=self.lime_button ,bg="lime")
        self.lime.grid(row=1,column=3)
        self.orange=Button(self.colorframe,text="",width=5,command=self.orange_button ,bg="orange")
        self.orange.grid(row=2,column=3)
        self.gray=Button(self.colorframe,text="",width=5,command=self.gray_button ,bg="gray")
        self.gray.grid(row=0,column=4)
        self.black=Button(self.colorframe,text="",width=5,command=self.black_button ,bg="black")
        self.black.grid(row=1,column=4)
        self.white=Button(self.colorframe,text="",width=5,command=self.white_button ,bg="white")
        self.white.grid(row=2,column=4)
        self.pallete=Button(self.colorframe,image=self.wheel_pic,height=30,width=30,command=self.pallete_button)
        self.pallete.grid(row=1,column=5)
       
        

        #saveframe----------------------
        self.saveframe=Frame(self.frame1,width=100,height=100,relief=SUNKEN, borderwidth=3)
        self.saveframe.grid(row=0,column=4)
        self.savebut=Button(self.saveframe,image=self.save_pic,height=30,width=30,command=self.save)
        self.savebut.grid(row=1,column=0)
        self.loadbut=Button(self.saveframe,image=self.load_pic,height=30,width=30,command=self.load_image)
        self.loadbut.grid(row=2,column=0)

        #clear frame
        self.clearframe=Frame(self.frame1,width=100,height=100,relief=SUNKEN, borderwidth=3)
        self.clearframe.grid(row=0,column=5)
        self.clear=Button(self.clearframe,image=self.clear_pic,height=30,width=30,text="clear",command=self.clearfun)
        self.clear.grid(row=2,column=0)
        self.select=Button(self.clearframe,image=self.selection_pic,height=30,width=30,text="move",command=self.ismovement)
        self.select.grid(row=1,column=0)
        self.undobut=Button(self.clearframe,image=self.undo_pic,text="undo",height=30,width=30,command=self.undo)
        self.undobut.grid(row=0,column=0)

    
        

        ##Zoom frame
        #self.zoomframe=Frame(self.frame1,width=100,height=100,relief=SUNKEN, borderwidth=3,bg="blue")
        #self.zoomframe.grid(row=0,column=4)
        #self.zoom=Button(self.toolframe,text="zoom",width=5,command=self.on_zoomButton_Pressed)
        #self.zoom.grid(row=0,column=0)

        #-----------Frame 2 Canvas---------------
        self.frame2 = Frame(self.screen,width=1100,height=500,bg="red")
        self.frame2.grid(row=1,column=0)
        self.canvas = Canvas(self.frame2, width=width, height=height, bg="white")
        self.canvas.pack()
        
    #Bind Pencil
    def on_PencilButton_Presed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.canvas["cursor"]="arrow"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.pencil_draw)
        self.canvas.bind("<ButtonRelease-1>", self.pencil_draw_end)
          
    #Bind Eraser
    def on_EraserButton_Presed(self):
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="dotbox"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.eraser_draw)
        self.canvas.bind("<ButtonRelease-1>", self.eraser_draw_end)
       
    #Bind marker
    def on_markerButton_Presed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.canvas["cursor"]="arrow"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.marker_draw)
        self.canvas.bind("<ButtonRelease-1>", self.marker_draw_end)

    #Bind Circle
    def on_CircleButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Circle)
        self.canvas.bind("<ButtonRelease-1>", self.draw_circle_end)
        
    #Bind Oval
    def on_OvalButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Oval)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Oval_end)

    #Bind Square
    def on_SquareButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Square)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Square_end)

    #Bind Rectangle
    def on_RectangleButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Rectangle)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Rectangle_end)

    #Bind Line
    def on_LineButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Line)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Line_end)

    #Bind Triangle
    def on_TriangleButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Triangle)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Triangle_end)

    #Bind rtTriangle
    def on_rtTriangleButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_rtTriangle)
        self.canvas.bind("<ButtonRelease-1>", self.draw_rtTriangle_end)

    #Bind Pentagon
    def on_PentagonButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Pentagon)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Pentagon_end)

    #Bind Hexagon
    def on_HexagonButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Hexagon)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Hexagon_end)

    #Bind Dimond
    def on_DimondButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Dimond)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Dimond_end)

    #Bind star
    def on_StarButton_Pressed(self):
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", self.draw_Star)
        self.canvas.bind("<ButtonRelease-1>", self.draw_Star_end)

    #Bind npoly
    def on_npolyButton_Pressed(self):
        n=simpledialog.askinteger("Input","Enter n",parent=self.screen)
        self.stroke_color.set(self.stroke_color.get())
        self.fill_color.set(self.fill_color.get())
        self.canvas["cursor"]="cross"
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<B1-Motion>", lambda event:self.draw_npoly(event,n))
        self.canvas.bind("<ButtonRelease-1>", self.draw_npoly_end)

    #Bind clrpick
    def on_clrpickButton_Pressed(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<Button-1>",self.clrpick)

    #Bind bucket
    def on_bucketButton_Pressed(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<Button-1>",self.paintbucket)

    #Bind zoom
    def on_zoomButton_Pressed(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<B1-Motion>")
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.bind("<MouseWheel>",self.zooming)
    
    #run
    def run(self):
        self.screen.mainloop()

    

    #PaintBucket
    def paintbucket(self,event):
         item_id = self.canvas.find_closest(event.x, event.y)  # Get the item ID of the closest shape
         color = self.canvas.itemcget(item_id, "fill")  # Get the current fill color of the shape

         # Change the fill color of the shape
         new_fill_color = "red"  # Replace "red" with your desired color
         self.canvas.itemconfig(item_id, fill=self.stroke_color.get())
        

    #ClePick fun
    def clrpick(self,event): 
        if self.x is None:
            self.x, self.y = event.x, event.y

        # Capture the entire canvas as an image
        x, y = self.canvas.winfo_rootx(), self.canvas.winfo_rooty()
        screen_image = ImageGrab.grab((x, y, x + self.canvas.winfo_width(), y + self.canvas.winfo_height()))

        # Get the color at the clicked position
        pixel_color = screen_image.getpixel((event.x_root - x, event.y_root - y))
        color = "#%02x%02x%02x" % pixel_color

        print("Color:", color)
        #self.stroke_color.config(bg=color)
        self.stroke_color.set(color)
        self.x, self.y = None, None


    def selectionarea(self,event):
        if self.shape_id!=None:
            self.canvas.delete(self.shape_id)
        if self.x==None:
            self.x,self.y=event.x,event.y   
        self.shape_id=self.canvas.create_rectangle(self.x,self.y,event.x,event.y,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)
        self.wall=self.shape_id
        self.flag=False

    def startselecting(self,event):
        if self.x == None or self.y==None:
            self.x,self.y=event.x,event.y

        item=[]
        self.selected_item=self.canvas.find_closest(self.x,self.y)
        item=self.canvas.coords(self.selected_item)
        self.obj=self.canvas.find_enclosed(item[0],item[1],item[2],item[3])
 
        if self.flag==False:
           # self.canvas.create_rectangle(item[0],item[1],item[2],item[3],width="1",fill="white",outline="white")
            self.flag=True
        else:
            return
       
    def endselecting(self,event):
        #self.end_x,self.end_y=None,None
        self.x,self.y=None,None
        self.selected_item=None

    def moveselectedarea(self,event):
        if self.selected_item is not None:
            x=event.x-self.x
            y=event.y-self.y

            self.x=self.x+x
            self.y=self.y+y
           
            self.canvas.move(self.selected_item,x,y)
            self.canvas.move(self.obj,x,y)

    def isselectbuttonpressed(self):
        self.canvas["cursor"]="tcross"
        self.canvas.unbind("<B1-Motion>")    
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")

        self.canvas.bind("<B1-Motion>",self.selection_area)
        self.canvas.bind("<ButtonRelease-1>",self.shapeend)

    def ismovement(self):
        self.canvas.unbind("<B1-Motion>")    
        self.canvas.unbind("<ButtonRelease-1>")
        self.canvas.unbind("<Button-1>")
        self.canvas.unbind("<Button-3>")


        self.canvas.bind("<Button-1>", self.startselecting)
        self.canvas.bind("<B1-Motion>", self.moveselectedarea)
        self.canvas.bind("<ButtonRelease-1>", self.endselecting)

        

    #Zoom fun
    def zooming(self,event):
        if(event.delta>0):
            self.canvas.scale(self.canvas.find_closest(event.x,event.y),0,0,1.1,1.1)
        else:
            self.canvas.scale("all",0,0,0.9,0.9)

    #Pencil fun
    def pencil_draw(self, event):
        if(self.x == None):
            self.x, self.y = event.x, event.y
            return
        self.canvas.create_line(self.x, self.y, event.x, event.y, fill=self.stroke_color.get()  ,width=1, capstyle=ROUND)
        self.x, self.y = event.x, event.y

    def pencil_draw_end(self, event):
        self.x, self.y = None, None

    #Eraser fun
    def eraser_draw(self, event):
        if(self.x == None):
            self.x, self.y = event.x, event.y
            return
        self.canvas.create_line(self.x, self.y, event.x, event.y, fill=self.fill_color.get()  ,width=self.stroke_size.get(), capstyle=ROUND)
        self.x, self.y = event.x, event.y

    def eraser_draw_end(self, event):
        self.x, self.y = None, None

    #Pencil fun
    def marker_draw(self, event):
        if(self.x == None):
            self.x, self.y = event.x, event.y
            return
        self.canvas.create_line(self.x, self.y, event.x, event.y, fill=self.stroke_color.get()  ,width=self.stroke_size.get(), capstyle=ROUND)
        self.x, self.y = event.x, event.y

    def marker_draw_end(self, event):
        self.x, self.y = None, None

    #Circle fun
    def draw_Circle(self, event):
        if self.shape_id!=None:
            self.canvas.delete(self.shape_id)
        if self.x==None:
            self.x,self.y=event.x,event.y
        rad = abs(self.x - event.x) + abs(self.y - event.y)
        x1, y1 = (self.x - rad), (self.y - rad)
        x2, y2 = (self.x + rad), (self.y + rad)
        self.shape_id=self.canvas.create_oval(x1,y1,x2,y2,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)

    def draw_circle_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    #Oval fun
    def draw_Oval(self, event):
        if self.shape_id!=None:
            self.canvas.delete(self.shape_id)
        if self.x==None:
            self.x,self.y=event.x,event.y
        self.shape_id=self.canvas.create_oval(self.x,self.y,event.x,event.y,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)

    def draw_Oval_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    #Square fun
    def draw_Square(self, event):
        if self.shape_id!=None:
            self.canvas.delete(self.shape_id)
        if self.x==None:
            self.x,self.y=event.x,event.y
        size = abs(event.x-self.x ) + abs( event.y-self.y )
        x1, y1 = (self.x), (self.y)
        #Rigth Down
        if(self.x<event.x and self.y<event.y):
            x2, y2 = (self.x+size), (self.y+size)
        #Left Up
        elif(self.x>event.x and self.y>event.y):
            x2, y2 = (self.x-size), (self.y-size)
        #Rigth Up
        elif(self.x>event.x and self.y<event.y):
            x2, y2 = (self.x-size), (self.y+size)
        #Left Down
        else:
            x2, y2 = (self.x+size), (self.y-size)
            
        self.shape_id=self.canvas.create_rectangle(x1,y1,x2,y2,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)

    def draw_Square_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None
    
    #Rectangle fun
    def draw_Rectangle(self, event):
        if self.shape_id!=None:
            self.canvas.delete(self.shape_id)
        if self.x==None:
            self.x,self.y=event.x,event.y   
        self.shape_id=self.canvas.create_rectangle(self.x,self.y,event.x,event.y,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)

    def draw_Rectangle_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    #Line fun
    def draw_Line(self, event):
        if self.shape_id!=None:
            self.canvas.delete(self.shape_id)
        if self.x==None:
            self.x,self.y=event.x,event.y
        diffx,diffy = (event.x-self.x ) , (event.y-self.y)
        x1, y1 = (self.x ), (self.y )
        x2, y2 = (self.x + diffx), (self.y + diffy)
        #x1,y1=(event.x-self.x),(event.y-self.y)
        self.shape_id=self.canvas.create_line(x1,y1,x2,y2,fill=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)

    def draw_Line_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    #Triangle fun
    def draw_Triangle(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
            
        if self.x == None:
            self.x,self.y=event.x, event.y
            return
        diffx,diffy=abs(self.x-event.x),abs(self.y-event.y)
        #Rigth down
        if(self.x<event.x and self.y<event.y):
            x3,y3=self.x,event.y
            x2,y2=event.x,event.y
            x1,y1=mp(x2,x3),self.y
           
        #Left down
        elif(self.x>event.x and self.y<event.y):
            x2,y2=self.x,event.y
            x3,y3=event.x,event.y
            x1,y1=mp(x2,x3),self.y
        #Left up
        elif(self.x>event.x and self.y>event.y):
            x2,y2=self.x,self.y
            x3,y3=event.x,self.y
            x1,y1=mp(x2,x3),event.y
        #Rigth up
        else:
            x3,y3=self.x,self.y
            x2,y2=event.x,self.y
            x1,y1=mp(x2,x3),event.y
        self.shape_id= self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)
   
    def draw_Triangle_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None
       
    #Rigth Triangle fun
    def draw_rtTriangle(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
           
        if self.x == None:
            self.x,self.y=event.x, event.y
            return
        diffx,diffy=abs(self.x-event.x),abs(self.y-event.y)
        #Rigth down
        if(self.x<event.x and self.y<event.y):
            x1,y1=self.x,self.y
            x2,y2=event.x,event.y
            x3,y3=x1,event.y
           
        #Left down
        elif(self.x>event.x and self.y<event.y):
            x2,y2=event.x,self.y
            x3,y3=event.x,event.y
            x1,y1=x2+diffx,event.y
        #Left up
        elif(self.x>event.x and self.y>event.y):
            x2,y2=self.x,self.y
            x1,y1=event.x,event.y
            x3,y3=x1,self.y
        #Rigth up
        else:
            x3,y3=self.x,self.y
            x2,y2=event.x,self.y
            x1,y1=x3,y2-diffy
       
        self.shape_id= self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)
       
    def draw_rtTriangle_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None
      
    #Pentagon fun
    def draw_Pentagon(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
           
        if self.x == None:
            self.x,self.y=event.x, event.y
            return
        diffx,diffy=abs(self.x-event.x),abs(self.y-event.y)

        
        my=mp(self.y,event.y)
        if(self.y<event.y):
            x5,y5=self.x,mp(my,mp(my,self.y))
            x2,y2=event.x,y5
            x1,y1=mp(x2,x5),self.y
            x3,y3=mp(x1,x2),event.y
            x4,y4=mp(x1,x5),event.y
        else:
            x5,y5=self.x,mp(my,mp(my,event.y))
            x2,y2=event.x,y5
            x1,y1=mp(x2,x5),event.y
            x3,y3=mp(x1,x2),self.y
            x4,y4=mp(x1,x5),self.y
        self.shape_id= self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)
       
    def draw_Pentagon_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    #Hexagon fun
    def draw_Hexagon(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
           
        if self.x == None:
            self.x,self.y=event.x, event.y
            return
        my=mp(self.y,event.y)

        x6,y6=self.x,mp(my,self.y)
        x5,y5=x6,mp(my,event.y)
        x2,y2=event.x,y6
        x3,y3=x2,y5
        x1,y1=mp(x2,x6),self.y
        x4,y4=x1,event.y
        self.shape_id= self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)
       
    def draw_Hexagon_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    #Dimond fun
    def draw_Dimond(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
           
        if self.x == None:
            self.x,self.y=event.x, event.y
            return
        my=mp(self.y,event.y)
        mx=mp(self.x,event.x)
        x1,y1=mx,self.y
        x2,y2=event.x,my
        x3,y3=mx,event.y
        x4,y4=self.x,my
        self.shape_id= self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)
       
    def draw_Dimond_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    #star fun
    def draw_Star(self, event):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)
           
        if self.x == None:
            self.x,self.y=event.x, event.y
            return
        my=mp(self.y,event.y)
        mx=mp(self.x,event.x)
        if(self.y<event.y):
            x9,y9=self.x,mp(my,mp(my,self.y))
            x3,y3=event.x,y9
            x1,y1=mp(x3,x9),self.y
            x5,y5=mp(x1,x3),event.y
            x7,y7=mp(x1,x9),event.y
            x2,y2=mp(mx,mp(mx,event.x)),y9
            x10,y10=mp(mx,mp(mx,self.x)),y9
            x4,y4=mp(x2,mp(x2,mp(mx,event.x))),mp(my,mp(my,event.y))
            x8,y8=mp(x10,mp(x10,mp(mx,self.x))),y4
            x6,y6=x1,mp(y5,y4)
        else:
            x9,y9=self.x,mp(my,mp(my,event.y))
            x3,y3=event.x,y9
            x1,y1=mp(x3,x9),event.y
            x5,y5=mp(x1,x3),self.y
            x7,y7=mp(x1,x9),self.y
            x2,y2=mp(mx,mp(mx,event.x)),y9
            x10,y10=mp(mx,mp(mx,self.x)),y9
            x4,y4=mp(x2,mp(mx,event.x)),mp(my,mp(my,self.y))
            x8,y8=mp(x10,mp(mx,self.x)),y4
            x6,y6=x1,mp(y5,y4)
        self.shape_id= self.canvas.create_polygon(x1,y1,x2,y2,x3,y3,x4,y4,x5,y5,x6,y6,x7,y7,x8,y8,x9,y9,x10,y10,fill=self.fill_color.get(),outline=self.stroke_color.get(),width=self.stroke_size.get())
        self.shapes.append(self.shape_id)
       
    def draw_Star_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None

    def draw_npoly(self,event,n):
        if self.shape_id is not None:
            self.canvas.delete(self.shape_id)

        if self.x is None:
            self.x, self.y = event.x, event.y
            return

        center_x = (event.x + self.x) / 2
        center_y = (event.y + self.y) / 2
        side_length = math.dist([self.x, self.y], [event.x, event.y]) / 2

        points = []
        for i in range(n):
            angle_deg = 360 * i / n  # Angle of each vertex in degrees
            angle_rad = math.radians(angle_deg)  # Angle in radians
            x = center_x + side_length * math.cos(angle_rad)
            y = center_y + side_length * math.sin(angle_rad)
            points.append(x)
            points.append(y)

        self.shape_id = self.canvas.create_polygon(points, fill=self.fill_color.get(), outline=self.stroke_color.get(), width=self.stroke_size.get())
        self.shapes.append(self.shape_id)

    def draw_npoly_end(self, event):
        self.x,self.y=None, None
        self.shape_id=None
         
    #stroke fun
    def stroke_button(self):
        self.ty.set("s")
        self.stroke.configure(bg=self.stroke_color.get())

    #fill fun
    def fill_button(self):
        self.ty.set("f")
        self.fill.configure(bg=self.fill_color.get())


    #red fun
    def red_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("red")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("red")

    #blue fun
    def blue_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("blue")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("blue")

    #yellow fun
    def yellow_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("yellow")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("yellow")

    #green fun
    def green_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("green")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("green")

    #brown fun
    def brown_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("brown")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("brown")
    
    #pink fun
    def pink_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("pink")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("pink")

    #purple fun
    def purple_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("purple")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("purple")

    #lime fun
    def lime_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("lime")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("lime")

    #orange fun
    def orange_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("orange")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("orange")

    #gray fun
    def gray_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("gray")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("gray")

    #black fun
    def black_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("black")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("black")

    #white fun
    def white_button(self):
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            self.fill_color.set("white")
        else:
            self.pstroke_color.set(self.stroke_color.get())
            self.stroke_color.set("white")

    #pallete fun
    def pallete_button(self):
        selectclr=colorchooser.askcolor(title="Select Color")
        if(self.ty.get()=="f"):
            self.pfill_color.set(self.fill_color.get())
            if(selectclr[1]==None):
                self.fill_color.set(self.pfill_color.get())
                return
            self.fill_color.set(selectclr[1])
        else:
            self.pstroke_color.set(self.stroke_color.get())
            if(selectclr[1]==None):
                self.stroke_color.set(self.pstroke_color.get())
                return
            self.stroke_color.set(selectclr[1])

    def save(self):
        filename = filedialog.asksaveasfilename(initialfile="untitled.png", defaultextension="png", filetypes=[("PNG", "JPG"), (".png", ".jpg")])
        if filename != "":
            x = self.screen.winfo_x()
            y = self.screen.winfo_y()
            image = ImageGrab.grab(bbox=(x, y+150, 1370, 700))
            image.save(filename)

    def load_image(self):
        filename = filedialog.askopenfilename(
            initialdir=".",
            title="Select an image",
            filetypes=[("Image files", ("*.png", "*.jpg", "*.jpeg", "*.gif", "*.bmp"))]
        )
        if filename:
            self.image = Image.open(filename)
            self.draw = ImageDraw.Draw(self.image)
            self.update_canvas()
            print("Image loaded:", filename)
        else:
            print("No image selected.")

    def update_canvas(self):
        # Clear the canvas
        self.canvass.delete("all")
        zoomed_width = int(self.image.width)
        zoomed_height = int(self.image.height)
        resized_image = self.image.resize((zoomed_width, zoomed_height))
        # Convert PIL image to Tkinter PhotoImage
        photo_image = ImageTk.PhotoImage(resized_image)
        self.canvass.create_image(0, 0, anchor="nw", image=photo_image, tags="image")
        self.canvass.image = photo_image
       
    def clearfun(self):
        self.canvas.delete("all")

    def undo(self):
        if self.shapes:
            shape_ = self.shapes.pop()  # Retrieve the ID of the last shape
            self.canvas.delete(shape_)




def mp(x1,x2):
        return (x1+x2)/2

PaintApp(1400,700,"Paint App").run()

