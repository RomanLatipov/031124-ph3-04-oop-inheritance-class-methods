from classes.mammal import Mammal

class Dog(Mammal):

    def __init__(self, name, rested, is_good=True):
        super().__init__(name=name, rested=rested)
        self.is_good = is_good

    def __repr__(self):
        return  f"Dog(name={self.name}, rested={self.rested}, is_good={self.is_good})"

    def make_sound(self):
        return "Bark"

    def sleep(self):
        super().sleep()
        print("Sleeps in your bed")

    def run_around(self):
        super().run_around()
        print("Chases the squirrel")