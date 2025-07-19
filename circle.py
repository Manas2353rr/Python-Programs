#File Name-circle.py
#By-Manas Jagyasi

class Circle:
    def input(self):
        self.radius=eval(input('enter radius'))

    def setRadius(self,r):
        self.radius=r

    def getradius(self):
        return self.radius
    
    def area(self):
        return 3.14*self.radius*self.radius