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

class Clownfish(Fish):
    def live_with_anemone(self):
        print("The clownfish is coexisting with sea anemone.");

casey = Clownfish("Casey");
print(casey.first_name + " " + casey.last_name);
casey.swim();
casey.live_with_anemone();