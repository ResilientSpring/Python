class MyClass:

    def __int__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    @staticmethod
    def display(ob):
        print(ob.get_value())
        print("\n")
    @staticmethod
    def change(ob):
        ob.set_value(100)
        print("Value of ob inside: ")
        MyClass.display(ob)




