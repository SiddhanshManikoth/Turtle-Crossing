from turtle import  Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
     def __init__(self,level):
         super().__init__()
         self.shape("turtle")
         self.penup()
         self.goto(STARTING_POSITION)
         self.setheading(90)
         self.lvl=level




     def move_Timmy_up(self):
         self.setheading(90)
         self.fd(MOVE_DISTANCE)

     def move_Timmy_down(self):
         self.setheading(270)
         self.fd(MOVE_DISTANCE)


     def next_level(self):
         if self.ycor()>FINISH_LINE_Y:
             self.lvl.level_up()
             self.goto(STARTING_POSITION)



