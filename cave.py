class Cave:
    def __init__(self, cave_name, cave_size, cave_description, cave_items, cave_character):
        self.name = cave_name
        self.size = cave_size
        self.description = cave_description
        self.items = cave_items
        self.characer = cave_character
        self.linked_caves = {}

    def set_description(self, cave_description):
        self.description = cave_description
    
    def get_description(self):
        return self.description
    
    def describe(self):
        print(f"The {self.get_name()}.")
        print(self.description)

    def link_cave(self, cave_to_link, direction):
        self.linked_caves[direction] = cave_to_link

    def get_name(self):
        return self.name

    def get_details(self):
        for direction in self.linked_caves:
            cave = self.linked_caves[direction]
            print( "The " + cave.get_name() + " is " + direction + ".")




