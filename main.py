from cave import Cave

#Cavern Object
cavern = Cave("cavern", None, None, None, None)
cavern.set_description("A dank and dirty cave.")
cavern.get_description()
cavern.describe()

#Dungeon Object
dungeon = Cave("dungeon", None, None, None, None)
dungeon.set_description("A large cave with a rack")

#Grotto Object
grotto = Cave("grotto", None, None, None, None)
grotto.set_description("A small cave with ancient graffiti")

#Cave Links
cavern.link_cave(dungeon, "south")
grotto.link_cave(dungeon, "east")
dungeon.link_cave(grotto, "west")


print(cavern.get_details())
