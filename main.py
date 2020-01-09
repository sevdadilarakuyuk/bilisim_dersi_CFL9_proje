import turtle
import random

import shape

# Ekran genişliği ve yüksekliği için sabitler yaratalım
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 800

selection = ""              # Kullanıcı seçiminin tutulacağım değişken
shape = shape.Shape()       # Shape kütüphanesi nesnesi yarattık

# Turtle çizim ekranını oluşturalım
screen = turtle.Screen()
screen.title("Geometrik Şekil Çizdirme Programı")
screen.bgcolor("blue")
screen.setup(width = SCREEN_WIDTH, height = SCREEN_HEIGHT)

# Şekil seçeneklerini ekrana yazdırmak için text adlı bir Turtle nesnesi yaratalım
text = turtle.Turtle()
text.speed(0)
text.color("yellow")
text.penup()
text.hideturtle()
text.goto(-570, 370)
text.write("Çizmek istediğiniz şeklin rakamına basın", align="left", font=("courier", 18, "normal"))
text.color("white")
text.goto(-570, 350)
text.write("1. Poligon", align="left", font=("courier", 16, "normal"))
text.goto(-570, 330)
text.write("2. Yıldız", align="left", font=("courier", 16, "normal"))
text.goto(-570, 310)
text.write("3. Küp", align="left", font=("courier", 16, "normal"))
text.goto(-570, 290)
text.write("4. Spiral", align="left", font=("courier", 16, "normal"))

# Kullanıcının seçimini ayarlayan fonksiyonları yazalım
def selection_is_polygon():
    global selection 
    selection = "1"

def selection_is_star():
    global selection 
    selection = "2"

def selection_is_cube():
    global selection 
    selection = "3"
    
def selection_is_spiral():
    global selection     
    selection = "4"

#klavye bağlantıları
screen.listen()
screen.onkey(selection_is_polygon, "1")
screen.onkey(selection_is_star, "2")
screen.onkey(selection_is_cube, "3")
screen.onkey(selection_is_spiral, "4")


#program ana döngüsü
while True:
    # 
    screen.update()

    if selection=="1":
        shape.pen.clear()
        side = screen.numinput("POLİGON", "Poligon kenar sayısını giriniz: ", minval=3)
        length = screen.numinput("POLİGON", "Poligon bir kenar uzunluğunu giriniz: ", minval=1)
        shape.Polygon(side, length)
        turtle.getcanvas().focus_force()
        selection=""

    elif selection=="2":
        shape.pen.clear()
        length = screen.numinput("YILDIZ", "Yıldızın bir kenar uzunluğunu giriniz: ", minval=1)
        shape.Star(length)
        turtle.getcanvas().focus_force()
        selection=""

    elif selection=="3":
        pass

    elif selection=="4":
        shape.pen.clear()
        depth = screen.numinput("SPİRAL", "Spiralin derinliğini giriniz: ", minval=10)
        depth = screen.numinput("SPİRAL", "Spiralin derinliğini giriniz: ", minval=10)        shape.Spiral(depth)
        turtle.getcanvas().focus_force()
        selection=""


screen.mainloop()












