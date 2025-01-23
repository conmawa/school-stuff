import p5
from random import randint

class Snowflake():
    def __init__(self):
        self.x_pos = randint(0, width)
        self.y_pos = randint(0, height)
        self.radius = randint(5, 10)
        self.speed = randint(15, 25)
        
    def show(self):
        p5.circle(self.x_pos, self.y_pos, self.radius)
    
    def drop(self):
        if self.y_pos < 800:
            self.y_pos = self.y_pos + self.speed
        else:
            self.y_pos = 0
            self.x_pos = randint(0, width)


def setup():
    global  height, width, snowflakes
    height = 800
    width = 1000
    p5.size(1000,800)
    snowflakes = []
    for _ in range(200):
        snowflakes.append(Snowflake())

def draw():
    p5.background(0)
    for flake in snowflakes:
        flake.show()
        flake.drop()

p5.run()