class Item:
    def __init__(self, name: str, description: str, value: int) -> object:
        self.Name = name
        self.Description = description
        assert isinstance(value, int)
        self.Value = value

    def __str__(self) -> object:
        return self.Name + "\n\t" + self.Description


class Container(Item):
    def __init__(self, name, description, value, contents):
        """
        :type name: str
        :type description: str
        :type value: int
        :type contents: Item[]
        """
        super(Container, self).__init__(name, description, value)
        assert isinstance(contents, list)
        self.Contents = contents

    @property
    def __str__(self):
        contents = ""
        for thing in self.Contents:
            assert isinstance(thing, Item)
            contents += "\n" + thing.__str__()

        return str(super(Container, self).__str__()) + contents


class Weapon(Item):
    def __init__(self, name, description, value, damage):
        super(Weapon, self).__init__(name, description, value)
        assert isinstance(damage, int)
        self.Damage = damage


class Shield(Item):
    def __init__(self, name, description, value, defense):
        super(Shield, self).__init__(name, description, value)
        assert isinstance(defense, int)
        self.Defense = defense
