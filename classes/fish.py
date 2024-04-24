class Fish:

    all_fish = []

    def __init__(self, name, length_in_inches):
        self.name = name
        self.length_in_inches = length_in_inches
        Fish.all_fish.append(self)

    def __repr__(self):
        return f"Fish(name={self.name}, length_in_inches={self.length_in_inches})"

    def make_bubbles(self):
        return "bloop bloop"

    @classmethod
    def num_fish(cls):
        return len(cls.all_fish)
    
    @classmethod
    def all_fish_names(cls):
        return [fish.name for fish in cls.all_fish]
    
    @classmethod
    def average_length(cls):
        return sum([fish.length_in_inches for fish in cls.all_fish]) / len(cls.all_fish)