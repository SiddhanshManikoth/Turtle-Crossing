from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
DENSITY=20



class CarManager():
    def __init__(self,score):
        self.x_axis = 0
        self.y_axis = 0
        self.trafficList=[]
        self.lvl=score

    def genrate_Traffic(self):
        for c in range(DENSITY):
            self.new_car=self.add_car()

    def move_traffic(self):
        for car in self.trafficList:
            new_x = car.xcor() - STARTING_MOVE_DISTANCE-(self.lvl.level*MOVE_INCREMENT)
            new_y = car.ycor()
            car.goto(new_x, new_y)

    def add_car(self):
        self.car = Turtle()
        self.car.shape("square")
        self.car.color(random.choice(COLORS))
        self.car.shapesize(stretch_wid=1, stretch_len=2)
        self.car.penup()
        self.y_axis = random.randint(-250, 250)
        self.x_axis = random.randint(300, 900)
        self.car.goto(self.x_axis, self.y_axis)
        self.trafficList.append(self.car)


