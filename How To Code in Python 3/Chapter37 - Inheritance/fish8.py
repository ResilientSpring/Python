class Fish:
    def __init__(self, first_name, last_name="Fish", skeleton="bone", eyelids=False):
        self.first_name = first_name;
        self.last_name = last_name;
        self.skeleton = skeleton;
        self.eyelids = eyelids;

    def swim(self):
        print("This fish is swimming.");

    def swim_backwards(self):
        print("This fish can swim backwards.");

class Trout(Fish):

    def __init__(self, water="freshwater"):

        self.water = water;
        super().__init__(self);

terry = Trout();

# initialize first name.
terry.first_name = "Terry";

# Use parent_init_() through super()
print(terry.first_name + " " + terry.last_name);
print(terry.eyelids);

# Use child_init_() to override
print(terry.water);

# Use parent swim() method
terry.swim();