#Python Snake Game
import tkinter as tk
import random

#Snake Game

#class SnakeGUI
#==========================================
# Purpose: This class helps to create a visualization of the snake object and the game for the snake.

# Instance variables:
#   No instance variables.

# Methods: (What methods does this class have, and what does each do?)
#    __init__: A constructor that only takes in self and has no other arguments. This constructor takes in the canvas, board, object, enemy object, random x integer and y integer for the food pallet, directions for the object,
#       Whether the game is not over, the restart method, and the gameloop call.

#   restart: A method that has the same variables as the constructor except self.win. If the game is over, then the game will restart. Takes the parameter event since it is allowing the game to restart. 

#   gameloop: A method that will help to make the game running.Doesn't take any parameters but allows the player and the enemy to move to certain directions in order to reach and eat the food pallet.
#           When the game is playing, a new food pallet is created when the player and the enemy consumes the food and they both have new body parts. Returns the boolean value True.
#           If the x and y coordinates of the player snake's head are less than 30 and greater than 630 meaning if the snake goes out of bounds, then the game ends and everything disappears. Returns boolean value True.
#           If the player snake's head makes contact with the player snake's body, then the game ends, everything is deleted. Returns True.
#           If the player snake's head makes contact with the enemy snake's body, then the game ends. Returns True.
#           If the enemy snake's head makes contact with the player snake's body, then the game ends. Returns True. 
#==========================================

class SnakeGUI:
    def __init__(self):
        self.win = tk.Tk()
        self.canvas = tk.Canvas(self.win, width = 660, height = 660)
        self.canvas.pack()
        self.board = self.canvas.create_rectangle(30,30,630,630)
        self.ojb = Snake(330, 330, 'green',self.canvas)
        self.enemy = Snake(60, 60, 'purple',self.canvas)
        self.randitx = random.randint(1,20)*30
        self.randity = random.randint(1,20)*30
        self.foodpallet = self.canvas.create_oval(self.randitx, self.randity,self.randitx+30,self.randity+30, fill = 'green')
        self.win.bind('<Down>',self.ojb.go_down)
        self.win.bind('<Up>',self.ojb.go_up)
        self.win.bind('<Left>',self.ojb.go_left)
        self.win.bind('<Right>',self.ojb.go_right)
        self.Gameover = False
        self.win.bind('r',self.restart)
        self.gameloop()

    def restart(self, event):
        if self.Gameover == True:
            self.canvas.delete(tk.ALL)
            self.board = self.canvas.create_rectangle(30,30,630,630)
            self.ojb = Snake(330, 330, 'green',self.canvas)
            self.enemy = Snake(60, 60, 'purple',self.canvas)
            self.randitx = random.randint(1,20)*30
            self.randity = random.randint(1,20)*30
            self.foodpallet = self.canvas.create_oval(self.randitx, self.randity,self.randitx+30,self.randity+30, fill = 'green')
            self.win.bind('<Down>',self.ojb.go_down)
            self.win.bind('<Up>',self.ojb.go_up)
            self.win.bind('<Left>',self.ojb.go_left)
            self.win.bind('<Right>',self.ojb.go_right)
            self.Gameover = False
            self.win.bind('r',self.restart)
            self.gameloop()


        
        
    def gameloop(self):
        if self.Gameover == False:
            move = self.ojb.move(self.randitx, self.randity,self.foodpallet)
            self.canvas.after(100, self.gameloop)
            move_enemy = self.enemy.enemymovement(self.randitx, self.randity,self.foodpallet)
            self.head = self.canvas.coords(self.ojb.segments[0])
            self.enemyhead = self.canvas.coords(self.enemy.segments[0])
             
            
            if move or move_enemy:
                self.randitx = random.randint(1,20)*30
                self.randity = random.randint(1,20)*30
                self.foodpallet = self.canvas.create_oval(self.randitx, self.randity,self.randitx+30,self.randity+30, fill = 'green')
                return True
   

            if (self.head[0]< 30.0 or self.head[0] > 630.0)  or  (self.head[1] < 30.0 or self.head[1] > 630.0):
                self.Gameover = True
                self.canvas.delete(tk.ALL)
                self.canvas.create_text(330, 330, text = str(len(self.ojb.segments)))
                return True

 
            for i in range(1, len(self.ojb.segments)):
                self.rectangle = self.canvas.coords(self.ojb.segments[i])
                if self.head[0] == self.rectangle[0] and self.head[1] == self.rectangle[1]:
                    self.Gameover = True
                    self.canvas.delete(tk.ALL)
                    self.canvas.create_text(330, 330, text = str(len(self.ojb.segments)))
                    return True

            for i in range(1, len(self.enemy.segments)):
                self.enemyrectangle = self.canvas.coords(self.enemy.segments[i])
                
                
                if self.head[0] == self.enemyrectangle[0] and self.head[1] == self.enemyrectangle[1]:
                    self.Gameover = True
                    print("Gameover")
                    return True


            for i in range(1, len(self.ojb.segments)):
                if self.enemyhead[0] == self.rectangle[0] and self.enemyhead[1] == self.rectangle[1]:
                    self.Gameover = True
                    print("Gameover..")
                    return True

                
                
      


#class Snake
#==========================================
# Purpose: This class helps to create the attributes of the player and the enemy snake.

# Instance variables:
#   x: represents the x integer of the snake.
#   y: represents the y integer of the snake.
#   color: String that represents the color of the snake.
#   canvas: represents how the snake will be visualized on the game and where they'll be moved. 
#   segments: A list that takes in the snake's attributes.
#   vx: This integer represents the snake's velocity in the x direction.
#   vy: This integer represents the snake's velocity in the y direction.


# Methods: (What methods does this class have, and what does each do?)
#    __init__: A constructor that takes in four arguments(not counting self) that initializes the x integer, the y integer, the color, and canvas for the snake.
#    move: A method that takes in three arguments and returns true if the coordinates of the food equal the coordinates of the snake. Furthermore, this lets the snake consume the food.
#          returns False otherwise and deletes the snake attributes out of the segments list.
#    go_down: This method allows the snake to go down based on the snake's velocity of x at 0 and y at 30.
#    go_up:  This method allows the snake to go up based on the the snake's velocity of x at 0 and y at -30.
#    go_left: This method allows the snake to go left based on the snake's velocity of x at -30 and y at 0.
#    go_right: This  method allows the snake to go right based on the snake's velocity of x at 30 and y at 0.
#    enemymovement: This method determines determines the enemy snake's movement of choice based on it's coordinates in comparison to the food pallet's coordinates.
#                   For instance if the x coordinates of the snake is larger than the x coordinates of the food, then the enemy snake will go left. 
#==========================================
class Snake:
    def __init__(self, x, y, color, canvas):
        self.x = x
        self.y = y
        self.color = color
        self.canvas = canvas
        self.segments = []
        self.segments.insert(0,self.canvas.create_rectangle(x,y,x+30,y+30, fill = self.color))
        self.vx = 30
        self.vy = 0

    def move(self,foodx,foody,foodpallet):
        self.x += self.vx
        self.y += self.vy
        self.segments.insert(0,self.canvas.create_rectangle(self.x,self.y,self.x+30,self.y+30, fill = self.color))
        if foodx == self.x and foody == self.y:
            self.canvas.delete(foodpallet)
            return True
        
        else:
            item_id = self.segments.pop()
            self.canvas.delete(item_id)
            return False
        
    def go_down(self, event):
        self.vx = 0
        self.vy = 30
    def go_up(self, event):
        self.vx = 0
        self.vy = -30
    def go_left(self, event):
        self.vx = -30
        self.vy = 0
    def go_right(self, event):
        self.vx = 30
        self.vy = 0

    def enemymovement(self,foodx, foody, foodpallet):
        if self.x > foodx:
            self.vx = -30
            self.vy = 0

        if self.x < foodx:
            self.vx = 30
            self.vy = 0
            
        if self.y > foody:
            self.vx = 0
            self.vy = -30

        if self.y < foody:
            self.vx = 0
            self.vy = 30
            
        return self.move(foodx, foody,foodpallet)


        
            
        

SnakeGUI()
tk.mainloop()


        
