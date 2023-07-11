#imports:
from turtle import *
from time import *
from math import *
from tkinter import *

#code:
class Maker:
    def __init__(self):
        while True:
             try:
                 diametre = int(input("How wide do you want your shape to be? (pixels) \n"))
             except ValueError:
                 print("Thats not a number")
                 sleep(1)
             else:
                 break
        sleep(1)
        while True:
             try:
                 speed_turtle = int(input("How fast do you want your turtle to go? \n"))
             except ValueError:
                 print("Thats not a number")
                 sleep(1)
             else:
                 break
        sleep(1)
        while True:
             try:
                 time = int(input("How long you want to wait after the shape has finished being drawn? (seconds) \n"))
             except ValueError:
                 print("Thats not a number")
                 sleep(1)
             else:
                 break

        #math
        π = pi
        radius = diametre / 2
        length = diametre / 4
        circumference = 2*π*radius
        area = π*radius**2
        
        #turtle
        speed(speed_turtle)
        hideturtle()
        title("Shape generated. Area = "+str(area)+" pixels")
            #rgb = lambda inp: [int(cl) for cl in inp.split(',')]
        for i in range(72):
            for j in range(6):
                forward(length)
                right(60)
            right(5)
        sleep(time)
        
        self.diametre = diametre
        self.radius = radius
        self.speed_turtle = speed_turtle
        self.time = time
        self.length = length
        self.circumference = circumference
        self.area = area


    @staticmethod 
    def Help():
        print("""COOL""")

class stats:
    global Maker
    def __init__(self, Classname):
        try:
            Maker = Classname
            print("The radius is "+str(Maker.radius)+" pixels.")
            print("The diametre is "+str(Maker.diametre)+" pixels.")
            print("The circumference is "+str(Maker.circumference)+" pixels.")
            print("The area is "+str(Maker.area)+" pixels.")
            
        except:
            Maker = Maker()
            print()
            print("The radius is "+str(Maker.radius)+" pixels.")
            print("The diametre is "+str(Maker.diametre)+" pixels.")
            print("The circumference is "+str(Maker.circumference)+" pixels.")
            print("The area is "+str(Maker.area)+" pixels.")

    def radius(Classname):
        try:
            Maker = Classname
            print("The radius is "+str(Maker.radius)+" pixels.")

        except:
            Maker = Maker()
            print()
            print("The radius is "+str(Maker.radius)+" pixels.")

    def diametre(Classname):
        try:
            Maker = Classname
            print("The diametre is "+str(Maker.diametre)+" pixels.")

        except:
            Maker = Maker()
            print()
            print("The diametre is "+str(Maker.diametre)+" pixels.")

    def circumference(Classname):
        try:
            Maker = Classname
            print("The circumference is "+str(Maker.circumference)+" pixels.")

        except:
            Maker = Maker()
            print()
            print("The circumference is "+str(Maker.circumference)+" pixels.")

    def area(Classname):
        try:
            Maker = Classname
            print("The area is "+str(Maker.area)+" pixels.")

        except:
            Maker = Maker()
            print()
            print("The area is "+str(Maker.area)+" pixels.")
            
if __name__ == '__main__':
    Maker = Maker()
    print()
    stats(Maker)
