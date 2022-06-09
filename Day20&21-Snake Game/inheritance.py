# Inheritance- Process of inheriting behaviour and appearance from existing class is called class Inheritance
# - Inside __init__ add super()

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")

class Fish(Animal):

    def __init__(self):
        super().__init__()  # helps to insert all the behaviour and apperance of Animal class

    def breathe(self):
        super().breathe()
        print("doing this underwater") # adding additional functionality to exisiting one

    def swim(self):
        print("Moving in water")

nemo = Fish() # object from fish class
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)