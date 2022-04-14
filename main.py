import turtle
from random import *
from turtle import *
from freegames import path
from tkinter import *
from time import time

class GUI:
    def __init__(self):
        self.Window = Tk()
        self.Window.withdraw()

        self.login = Toplevel()
        self.login.title("Login")
        self.login.resizable(width=False,
                             height=False)
        self.login.configure(width=400,
                             height=300)
        self.pls = Label(self.login,
                         text="\tԳրեք ձեր անունը",
                         justify=CENTER)

        self.pls.place(relheight=0.15,
                       relx=0.2,
                       rely=0.07)
        self.labelName = Label(self.login,
                               text="-->: ",
                               font="Helvetica 12")

        self.labelName.place(relheight=0.2,
                             relx=0.1,
                             rely=0.2)

        self.entryName = Entry(self.login,
                               font="Helvetica 14")

        self.entryName.place(relwidth=0.4,
                             relheight=0.12,
                             relx=0.35,
                             rely=0.2)

        self.go = Button(self.login,
                         text="Մուտք",
                         font="Helvetica 14 bold",
                         command=lambda: self.goAhead(self.entryName.get()))

        self.go.place(relx=0.4,
                      rely=0.55)
        self.Window.mainloop()

    def goAhead(self, name):
        self.login.destroy()
        game(name)

def game(name:str)->None:
    time_start = time()
    counter = 0
    car = path('car.gif')
    tiles = list(range(32)) * 2
    state = {'mark': None}
    hide = [True] * 64


    def square(x, y):
        up()
        goto(x, y)
        down()
        color('black', 'white')
        begin_fill()
        for count in range(4):
            forward(50)
            left(90)
        end_fill()


    def index(x, y):
        return int((x + 200) // 50 + ((y + 200) // 50) * 8)


    def xy(count):
        return (count % 8) * 50 - 200, (count // 8) * 50 - 200


    def tap(x, y):
        nonlocal counter
        spot = index(x, y)
        mark = state['mark']
        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
        elif counter == 31:
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None
            time_end = time()
            with open("Records.txt",'a') as file:
                file.write(f"{name} ends game at {time_end-time_start}")
            print("END")

        else:
            #Right click
            counter += 1
            hide[spot] = False
            hide[mark] = False
            state['mark'] = None


    def draw():
        clear()
        goto(0, 0)
        shape(car)
        stamp()
        for count in range(64):
            if hide[count]:
                x, y = xy(count)
                square(x, y)
        mark = state['mark']


        if mark is not None and hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 2, y)
            color('black')
            write(tiles[mark], font=('Arial', 30, 'normal'))
        update()
        ontimer(draw, 100)

    shuffle(tiles)
    addshape(car)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done()

if __name__ == '__main__':
    app = GUI()