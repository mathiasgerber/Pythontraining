class Item:
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super().__init__(name="Gold",
                         description="A gold coin with Value {}.",
                         value=self.amount)


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super().__init__(name, description, value)

    def __str__(self):
        return "{}\n=====\n{}\nValue: {}\nDamage: {}".format(self.name, self.description, self.value, self.damage)


class Stone(Weapon):
    def __init__(self):
        super().__init__(name="Stone",
                         description="A small stone. You can use it. But well, it doesn't really hurt.",
                         value=0,
                         damage=5)


class Dagger(Weapon):
    def __init__(self):
        super().__init__(name="Dagger",
                         description="A small dagger. It's not really a good Weapon, but it's a start.",
                         value=10,
                         damage=10)

class Sword(Weapon):
    def __init__(self):
        super().__init__(name="Sword",
                         description="An ordinary Sword. Nice to have in an unknown area.",
                         value=20,
                         damage=25)
