from classes.mammal import Mammal

class Cat(Mammal):
    def __init__(self, name, rested=False, lives_remaining=9):
        super().__init__(name=name, rested=rested)
        self.lives_remaining = lives_remaining

    def __repr__(self):
        return f"Cat(name={self.name}, rested={self.rested})"
    
    def make_sound(self):
        return "Meow"
    
    def sleep(self):
        super().sleep()
        print("ZZZZZZZzzzzzzzz")

    def take_a_nap(self):
        super().sleep()
        print("napping on your keyboard")