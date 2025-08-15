
import tkinter as tk
import random
import time

root = tk.Tk()
root.minsize(600, 600)
root.maxsize(600, 600)
root.title("SNAKE GAME OG")
"""--------------------------------------------------------------------------------------------------------------------"""
def on_click():
    start_game.destroy()
    head = snake_head()
    head.movement()

"""--------------------------------------------------------------------------------------------------------------------"""
class snake_head:
    X = random.uniform(50,550)
    Y = random.uniform(50,550)
    def __init__(self):
       self.canva = tk.Canvas(root,width=600,background ="green",height=600)
       self.canva.place(x=0,y=0)
       self.shead = self.canva.create_rectangle(snake_head.X,snake_head.Y,snake_head.X+25.0,snake_head.Y+25.0,fill="white",outline="black")
       self.moving = False  
       self.direction = None
       self.create = food_snake(self.canva)
       self.tail = self.shead
       self.body = [self.shead]

    def movement(self):
        root.bind("<w>", self.start_up)
        root.bind("<d>", self.start_right)
        root.bind("<a>", self.start_left)
        root.bind("<s>", self.start_down)


    def start_up(self, event=None):
        self.direction = "up"
        if not self.moving:  
            self.moving = True
            self.move_snake() 
    
    def start_right(self, event=None):
        self.direction = "right"
        if not self.moving:  
            self.moving = True
            self.move_snake() 
    
    def start_down(self, event=None):
        self.direction = "down"
        if not self.moving:  
            self.moving = True
            self.move_snake()
    
    def start_left(self, event=None):
        self.direction = "left"
        if not self.moving:  
            self.moving = True
            self.move_snake()  

    def stop_movement(self, event=None):
        self.moving = False

    def move_snake(self):
        coords = self.canva.coords(self.shead)
        if(coords[0]<0 or coords[1]<0 or coords[2]>600 or coords[3]>600):
            self.end_game()
        coordsF = self.canva.coords(self.create.food)
        
        if (coordsF[0] >= coords[0] and coordsF[0] <= coords[2] and   coordsF[1] >= coords[1] and coordsF[1] <= coords[3] and  coordsF[2] >= coords[0] and coordsF[2] <= coords[2] and   coordsF[3] >= coords[1] and coordsF[3] <= coords[3]): 
           self.canva.delete(self.create.food)
           self.create = food_snake(self.canva)
           coordT = self.canva.coords(self.tail) 
           self.newcoords =  snake_body(coordT,self.direction)
           self.new = self.newcoords.new_coords
           self.tail = self.canva.create_rectangle(self.new[0], self.new[1], self.new[2], self.new[3], fill="white", outline="black")
           self.body.append(self.tail)
           
        if self.moving: 
            self.positions = [self.canva.coords(segment) for segment in self.body] 
            if self.direction == "up":
                x, y = 0, -10  
            elif self.direction == "down":
                 x, y = 0, 10
            elif self.direction == "right":
                 x, y = 10, 0
            elif self.direction == "left":
                 x, y = -10,0
            self.canva.move(self.shead, x, y)
            for i in range(1, len(self.body)):
                self.canva.coords(self.body[i], *self.positions[i - 1])
            self.canva.after(250, self.move_snake)
            
    def end_game(self):
        self.canva.delete(self.shead)
        self.canva.destroy()
        self.text = tk.Label(root,text="END GAME",fg="black",width=20,height=3).place(x=250,y=300)
        self.res = tk.Button(root,background="black",fg="white",command=self.on_click2,width=20,height=3,text="PLAY AGAIN")
        self.res.place(x=250,y=400)
    def on_click2(self):
        self.res.destroy()
        head = snake_head()
        head.movement()
        
"""--------------------------------------------------------------------------------------------------------------------"""
class food_snake(snake_head):
    def __init__(self, canva):
        self.canva = canva 
        
        self.XF = random.uniform(50, 550)
        self.YF = random.uniform(50, 550)
       
        self.food = self.canva.create_rectangle(self.XF, self.YF, self.XF + 10.0, self.YF + 10.0, fill="orange", outline="black")

"""--------------------------------------------------------------------------------------------------------------------"""
class snake_body:
    new_coords =[0,0,0,0] 
    def __init__(self,coords,key):
       
       self.key =key
       if key == "up":
            snake_body.new_coords = [coords[0], coords[1] - 25, coords[2], coords[3] - 25]
       elif key == "down":
           snake_body.new_coords = [coords[0], coords[1] + 25, coords[2], coords[3] + 25]
       elif key == "right":
           snake_body.new_coords = [coords[0] + 25, coords[1], coords[2] + 25, coords[3]]
       elif key == "left":
            snake_body.new_coords = [coords[0] - 25, coords[1], coords[2] - 25, coords[3]]
       
        

"""--------------------------------------------------------------------------------------------------------------------"""
start_game = tk.Button(root,background="black",fg="white",command=on_click,width=20,height=3,text="PLAY")
start_game.place(x=250,y=300)

root.mainloop()
