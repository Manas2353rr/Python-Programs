class Circle:
    def input(self):
        self.radius=eval(input('enter radius'))

    def setRadius(self,r):
        self.radius=r

    def getradius(self):
        return self.radius
    
    def area(self):
        return 3.14*self.radius*self.radius

class Sphere(Circle):
    def area(self):
        return 4*super().area()
    
    def volume(self):
        return (self.area*self.radius)/3

def main():
    ring=Circle()
    ball=Sphere()

    ring.input()
    ball.setRadius(2)

    print('area of ring=',ring.area())
    print('volume of ball=',ball.volume())
    print('radius of ball=',ball.get.Radius())

main()
