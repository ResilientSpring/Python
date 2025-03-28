# Define a class called Shark that has two functions associated with it, one for swimming
# and one for being awesome:

class Shark:

    def __init__(self, name, age):
        print("This is the constructor method.");
        self.name = name;
        self.age = age;

    def swim(self):
        # Reference the name.
        print(self.name + " is swimming.");

    def be_awesome(self):
        # Reference the name.
        print(self.name + " is being awesome.");

# Set name of Shark object.
sammy = Shark("Sammy", 5);
sammy.swim();
sammy.be_awesome();
print(sammy.name);
print(sammy.age);

stevie = Shark("Stevie", 80);
stevie.swim();