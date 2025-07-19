#File Name-sphere.py
#By-Manas Jagyasi

from circle import Circle

class Sphere(Circle):
    def area(self):
        return 4*super().area()
    
    def volume(self):
        return (self.area*self.radius)/3