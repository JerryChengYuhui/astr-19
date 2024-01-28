#Jerry Cheng Session4 Coding Journal1

class Cat:
    # Class representing a cat with physical characteristics

    def __init__(self, arm_length, leg_length, num_eyes, has_tail, is_furry):
        # Initializes the cat's physical characteristics
        # arm_length: Length of arms (float)
        # leg_length: Length of legs (float)
        # num_eyes: Number of eyes (int)
        # has_tail: Presence of tail (bool)
        # is_furry: Furriness (bool)
        self.arm_length = arm_length
        self.leg_length = leg_length
        self.num_eyes = num_eyes
        self.has_tail = has_tail
        self.is_furry = is_furry

    def describe(self):
        # Prints the cat's physical characteristics
        print(f"Arm length: {self.arm_length} cm")
        print(f"Leg length: {self.leg_length} cm")
        print(f"Number of eyes: {self.num_eyes}")
        print(f"Has a tail: {self.has_tail}")
        print(f"Is furry: {self.is_furry}")

# Creating a cat instance
my_cat = Cat(arm_length=15.0, leg_length=20.0, num_eyes=2, has_tail=True, is_furry=True)

# Describing the cat
my_cat.describe()
