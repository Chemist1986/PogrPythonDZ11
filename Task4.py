class Rectangle:
    
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def get_perimeter(self):
        return 2 * (self.length + self.width)

    def get_area(self):
        return self.length * self.width

    def __add__(self, other):
        total_perimeter = self.get_perimeter() + other.get_perimeter()
        return Rectangle(total_perimeter // 4)

    def __sub__(self, other):
        difference = self.get_perimeter() - other.get_perimeter()
        if difference < 0:
            return Rectangle(0)
        else:
            return Rectangle(difference // 4)

    def __str__(self):
        return f"Прямоугольник: Длина={self.length}, Ширина={self.width}"



rectangle1 = Rectangle(5, 3)
print(rectangle1)  
print("Периметр:", rectangle1.get_perimeter())  
print("Площадь:", rectangle1.get_area())  

rectangle2 = Rectangle(4)
print(rectangle2) 
print("Периметр:", rectangle2.get_perimeter())  
print("Площадь:", rectangle2.get_area())  

rectangle3 = rectangle1 + rectangle2
print(rectangle3)  
print("Периметр:", rectangle3.get_perimeter()) 

rectangle4 = rectangle3 - rectangle2
print(rectangle4)  
print("Периметр:", rectangle4.get_perimeter())  