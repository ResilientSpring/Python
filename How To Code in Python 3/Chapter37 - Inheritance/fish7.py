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

class Shark(Fish):
    def __init__(self, first_name, last_name="Shark", skeleton="cartilage", eyelids=True):
        self.first_name = first_name;
        self.last_name = last_name;
        self.skeleton = skeleton;
        self.eyelids = eyelids;

    def swim_backwards(self):
        print("This shark cannot swim backwards, but can sink backwards.");

sammy = Shark("Sammy");
print(sammy.first_name + " " + sammy.last_name);
sammy.swim();
sammy.swim_backwards();
print(sammy.eyelids);
print(sammy.skeleton);