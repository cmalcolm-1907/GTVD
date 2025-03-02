class Character:
    # this takes a name, hp, and dialog argument to create a new character
    def __init__(self, name, hp, dialog):
        self.name = name
        self.hp = hp
        self.dialog = dialog

    # this tells the program want to print when it tries to print a character
    def __str__(self):
        # I use a formatted string so I can see what's happening better
        return f"{self.name}\nHP: {self.hp}\nDialog: {self.dialog}"


# let's create an npc
mario = Character("Mario", 2, ["Yahoo", "Itsumi Mario"])


# Mario here can't do much, what if he was a spellcaster, or a tamer?
class Spellcaster(Character):
    # spellcasters have mana and spells in addition to the basics
    def __init__(self, name, hp, dialog, mana, spells):
        self.mana = mana
        self.spells = spells
        # we don't need to rewrite existing self.name etc.. just use a super().__init
        super().__init__(name, hp, dialog)


class Tamer(Character):
    # tamers have a creature in addition to normal stats
    def __init__(self, name, hp, dialog, creature):
        self.creature = creature
        super().__init__(name, hp, dialog)


# we don't have to create mario = Character() either we could just have a list of objects
characters = []
characters.append(Character("Luigi", 2, ["Ahh!", "Oh no!"]))
characters.append(Character("Wally", 1, "found me"))
characters.append(
    Spellcaster("Gandalf", 5, ["..."], 10, ["lightning bolt", "blinding light"])
)
characters.append(
    Tamer("Ash Ketchum", 1, ["Gotta catch 'em all", "Go Pikachu!"], "Pikachu")
)

for character in characters:
    if character.name == "Wally":
        print(character)


# Now create a method to add characters
def user_add_character():
    # 1 find out if the user is adding a character, spellcaster or tamer

    # 2 get name of character

    # 3 get hp of character

    # 4 get dialog of character

    # 5 if character done,

    # 6 elif spellcaster, get mana and spells

    # 7 elif tamer, get creature

    # 8 add instance of character/spellcaster/tamer to the list

    # pass means do nothing, get rid of this when your method is done.
    pass
