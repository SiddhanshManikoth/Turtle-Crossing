from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level=0
        self.hideturtle()
        self.penup()
        self.goto(x=-200,y=250)
        self.show_level()


    def level_up(self):
        self.level+=1
        self.show_level()
    def show_level(self):
        self.clear()
        self.write(arg=f"level: {self.level}", align="center", font=FONT)
    def game_over(self):
        self.home()
        self.write(arg="GAME OVER.", align="center", font=FONT)