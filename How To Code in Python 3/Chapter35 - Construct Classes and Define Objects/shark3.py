# Define a class called Shark that has two functions associated with it, one for swimming
# and one for being awesome:

class Shark:

    def __init__(self, name):
        print("This is the constructor method.");
        self.name = name;

    def swim(self):
        # Reference the name.
        print(self.name + " is swimming.");

    def be_awesome(self):
        # Reference the name.
        print(self.name + " is being awesome.");

# Set name of Shark object.
sammy = Shark("Sammy");
sammy.swim();
sammy.be_awesome();