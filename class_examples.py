#################### EXAMPLE 1 - Self and class-level attributes ##############################

class Circle:
    # Class-level attribute for storing the value of pi
    pi = 3.14159 #these are things that generally dont change

    def __init__(self, radius, mult_factor=2): # weird mult_factor oxk
        # Instance-level attribute
        self.radius = radius
        self.mult_factor = mult_factor

    def calculate_area(self):
        # Access class-level attribute using 'self.pi' or 'Circle.pi'
        area = Circle.pi * self.radius ** self.mult_factor
        return area

# Create two instances of the 'Circle' class
circle1 = Circle(5)
circle2 = Circle(10,1) # optional argument

# Access the class-level attribute 'pi' using the class name
print(f"Value of pi: {Circle.pi}")

# Calculate and print the areas of the circles
print(f"Area of circle1: {circle1.calculate_area()}")
print(f"Area of circle2: {circle2.calculate_area()}")


#################### EXAMPLE 2 - Subclasses/inheretence ##############################

# Base class 'Person'
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name}, and I'm {self.age} years old.")

# Subclass 'Student' inherits from 'Person'
class Student(Person):
    def __init__(self, name, age, student_id):
        # Call the constructor of the base class
        super().__init__(name, age)
        self.student_id = student_id

    def study(self, subject):
        print(f"{self.name} is studying {subject}.")

# Subclass 'Teacher' inherits from 'Person'
class Teacher(Person):
    def __init__(self, name, age, teacher_id):
        # Call the constructor of the base class
        super().__init__(name, age)
        self.teacher_id = teacher_id

    def teach(self, subject):
        print(f"{self.name} is teaching {subject}.")

# Create instances of 'Student' and 'Teacher'
student1 = Student("Alice", 20, "S12345")
teacher1 = Teacher("Mr. Smith", 35, "T9876")

# Access attributes and call methods of the objects
student1.introduce()
student1.study("Math")

teacher1.introduce()
teacher1.teach("Science")
