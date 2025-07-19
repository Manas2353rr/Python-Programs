#File Name-using circle and sphere.py
#By-Manas Jagyasi


from circle import Circle
from sphere import Sphere

def main():
    ring=Circle()
    ball=Sphere()

    ring.input()
    ball.setRadius(4)

    print('area of ring=',ring.area())
    print('volume of ball=',ball.volume())
    print('radius of ball=',ball.get.Radius())

main()
