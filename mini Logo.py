import random

lista1=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista2=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista3=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista4=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista5=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista6=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista7=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista8=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista9=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
lista10=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

listas=[lista1,lista2,lista3,lista4,lista5,lista6,lista7,lista8,lista9,lista10]

class Location:
    def __init__(self, axis_x, axis_y):
        self.axis_x=axis_x
        self.axis_y=axis_y
    def change_x(self, z):
        self.axis_x+=z
    def change_y(self, z):
        self.axis_y+=z

        
start=Location(1,1)


def display(a,b):
    listas=[]
    for aa in range(1,11):
        ff=[' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
        listas.append(ff)
    listas[b-1][a-1]='*'
    for z in listas:
        print(z)

def move_left(z):
    if start.axis_x==1:
        start.change_x(10-z)
    else:
        start.change_x(-z)

def move_right(z):
    if start.axis_x==10:
        start.change_x(-10+z)
    else:
        start.change_x(z)

def move_up(z):
    if start.axis_y==1:
        start.change_y(10-z)
    else:
        start.change_y(-z)

def move_down(z):
    if start.axis_y==10:
        start.change_y(-10+z)
    else:
        start.change_y(z)        


display(start.axis_x,start.axis_y)

while True:
    respuesta=input("Where to (w a s d)? Enter to exit ")
    if respuesta=='a':
        move_left(1)
        display(start.axis_x,start.axis_y)

    if respuesta=='d':
        move_right(1)
        display(start.axis_x,start.axis_y)

    if respuesta=='w':
        move_up(1)
        display(start.axis_x,start.axis_y)

    if respuesta=='s':
        move_down(1)
        display(start.axis_x,start.axis_y)

    if respuesta=='':
        break

    else:
        print("Sorry mate, no bugs here: everything's a feature!")



