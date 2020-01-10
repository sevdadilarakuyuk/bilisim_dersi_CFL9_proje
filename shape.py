import turtle
import random
import math

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
        self.pen.goto(-180,120)
        self.pen.down(); 
        self.pen.showturtle()
        
        A = []; B = []
        length_p = length / 2

        # ön yüzün kare şekli
        for i in range(4):
            A.append(self.pen.position())
            self.pen.forward(length)
            self.pen.right(90)

        # ikinci kare için pozisyon al
        self.pen.up()
        self.pen.setx(self.pen.xcor() + length_p)
        self.pen.sety(self.pen.ycor() + length_p)
        self.pen.down()

        # arka yüzün kare şekli
        for i in range(4):
            B.append(self.pen.position())
            if i < 2: # ilk iki kenarı düz çizgi
                self.pen.forward(length)
            else: # son iki kenarı kesik çizgi
                for j in range (10):
                    self.pen.up()
                    self.pen.forward(length/20)
                    self.pen.down()
                    self.pen.forward(length/20)
            self.pen.right(90)

        # ara bağlantılar
        for i in range(4):
            self.pen.up()
            self.pen.setposition(A[i])
            self.pen.down()            
            self.pen.goto(B[i])

        self.pen.up()
        self.pen.hideturtle()
    
    def Spiral(self, depth, gap):
        self.pen.goto(0,0)
        self.pen.down(); 
        self.pen.showturtle()
        self.pen.speed("fast")

        depth = int(depth)   # derinlik değerinin kendisini integer yani sayı yapalım
        gap = int(gap)       # Aralık değerinin kendisini integer yani sayı yapalım

        index = random.randint(0, 5)         # rasgele 0-5 arası bir sayı üretelim --> index

        if   index==0: spiral = "daire";   angle = 0;   birSarmal = 40; distance = [1,3,8]
        elif index==1: spiral = "ongen";   angle = 36;  birSarmal = 10; distance = [1,2,4]
        elif index==2: spiral = "altıgen"; angle = 60;  birSarmal = 6;  distance = [2,4,8]      
        elif index==3: spiral = "dörtgen"; angle = 90;  birSarmal = 4;  distance = [6,10,18]    
        elif index==4: spiral = "üçgen";   angle = 120; birSarmal = 3;  distance = [7,12,22]        
        elif index==5: spiral = "yıldız";  angle = 144; birSarmal = 5;  distance = [8,14,26]    

        gap = distance[gap-1]          # o spiral çeşidi için sarmallar arası mesafe --> gap
        step = birSarmal * depth + 1   # İstenen derinliği vermek için tekrar sayısı --> step
        
        # rasgele seçim daire ise arşimed formulü: kaynak: internet
        if index==0:                    
            for i in range(step):
                t = i / 20 * math.pi
                x = (1 + gap * t) * math.cos(t)
                y = (1 + gap * t) * math.sin(t)
                self.pen.goto(x, y)

        # rasgele seçim diğer spiraller ise
        else:
            for i in range(step):
                self.pen.forward(i*gap)
                self.pen.right(angle)

        self.pen.up()
        self.pen.speed("slowest")
        self.pen.hideturtle()




