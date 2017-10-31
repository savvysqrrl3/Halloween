
class Spook(object):
	def __init__(self, kind, sound, critter, accessory, ability):
		self.kind = kind
		self.sound = sound
		self.critter = critter
		self.accessory = accessory
		self.ability = ability

class Light(object):
	def __init__(self, source):
		self.source = source
		

class CreepyCrawly(object):
	def __init__(self, kind):
		self.kind = kind
		
		

# Instances

spook1 = Spook("ghost", "ooooooOOOO OW! You walked through my face!", None, None, "selective invisibility")
spook2 = Spook("witch", "cackle cackle... Come try this apple, Dearie!", "cat", ("cauldron", "broom"), ("cast spells", "fly on broomstick"))
spook3 = Spook("vampire", "moan...Don't wake me up until it's midnight, and I've had my 'coffee!'", "bat", "coffin", "live for hundreds of years")
spook4 = Spook("skeleton", "rattle...rattle...clickety-clack... I think I lost a patella!", None, None, "nothing, really" )
spook5 = Spook("zombie", "uuuhhhh....brains....", None, "random eye-ball", "survive in spite of missing body parts")
spook6 = Spook("boggart", "BUMP! What gives YOU nightmares???", "werewolf", "closet or trunk", "imitate whatever scares you most")

light1 = Light("torch")
light2 = Light("candlestick")
light3 = Light("Jack-o-Lantern")
light4 = Light("fireplace")
light5 = Light("chandelier")
light6 = Light("floating green mist")

creepy1 = CreepyCrawly("spiders")
creepy2 = CreepyCrawly("maggots")
creepy3 = CreepyCrawly("worms")
creepy4 = CreepyCrawly("Thing (disembodied walking hand)")
creepy5 = CreepyCrawly("snakes")
creepy6 = CreepyCrawly("centipedes")


# test prints

# print spook6.kind, spook6.sound, spook6.critter, spook6.accessory, spook6.ability

# print light6.source

# print creepy6.kind
