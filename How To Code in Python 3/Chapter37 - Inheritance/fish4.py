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