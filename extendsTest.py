class Mammal:
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex

    def breath(self):
        print(self.name + "在呼吸")

    def poop(self):
        print(self.name + "在吃饭")


class Human(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = False

    def read(self):
        print(f"{self.name}" + "阅读")


class Cat(Mammal):
    def __init__(self, name, sex):
        super().__init__(name, sex)
        self.has_tail = True

    def scratch_sofa(self):
        print(self.name + "在抓沙发")


human = Human("小米", "男")
human.read()
human.poop()

cat = Cat("阿花", "母")
cat.scratch_sofa()
cat.poop()
