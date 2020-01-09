import turtle

class Shape():
    pen = turtle.Turtle()
    pen.speed("slowest")
    pen.pensize(4)
    pen.color("white")
    pen.up() 
    pen.hideturtle()

    def Polygon(self, side, length):
        self.pen.goto(-150,260)
        self.pen.down(); 
        self.pen.showturtle()

        angle = (side-2)*180/side

        for i in range(int(side)):
            self.pen.forward(length)
            self.pen.right(180-angle)
        
        self.pen.up()
        self.pen.hideturtle()

    def Star(self, length):
        self.pen.goto(-180,120)
        self.pen.down(); 
        self.pen.showturtle()

        for i in range(5):
            self.pen.forward(length)
            self.pen.right(144)
        
        self.pen.up()
        self.pen.hideturtle()

    def Cube(self, length):
        pass 
    
    def Spiral(self, depth):
        self.pen.goto(0,0)
        self.pen.down(); 
        self.pen.showturtle()

        for i in range(int(depth)):
            self.pen.forward(i*5)
            self.pen.right(120)
        
        self.pen.up()
        self.pen.hideturtle()