from spooks import Spook, Light, CreepyCrawly


class HauntedHouse(object):
	def __init__(self, name):
		self.name = name
		self.rooms = []

	def addRoom(self, new_room):
		# add room to mansion 
		self.rooms.append(new_room)
		print new_room.room_type, "added to the Haunted Mansion"
		return self

	def knock_knock(self, room_name):
		# hear the sound of each spook in a room, to guess who is inside
		here = None
		for room in self.rooms:
			if room.room_type == room_name:
				here = room
				print room.room_type, "Knock knock!"
				for spook in here.spooks:
			 		print "{} I have a {}, and I can {}.".format(spook.sound, spook.accessory, spook.ability)
		return self

	def illuminate(self, room_name):
		# show all objects in the room, including the items possessed by spooks
		here = None
		for room in self.rooms:
			if room.room_type == room_name:
				here = room
				print room.room_type, "Lumos!"
				for spook in here.spooks:
					print "There is a {}.".format(spook.kind)
				for creepy in here.creepy_crawlies:
					print "There is a {}.".format(creepy.kind)
				for light in here.lights:
					print "There is a {}.".format(light.source)
		return self

	def takeRoll(self):
		# find all instances of spooks, creepies, and lights, and print how many there are total,
		# as well as how many are in which rooms
		return self

class Room(object):
	def __init__(self, room_type):
		self.room_type = room_type
		self.spooks = []
		self.lights = []
		self.creepy_crawlies = []

	def addSpook(self, new_spook, count):
		# add instances of spooks to a room
		for quantity in range(0, (count)):
			self.spooks.append(new_spook)
		print self.room_type, count, new_spook.kind
		return self

	def addLight(self, new_light, count):
		# add instances of lights to a room
		for quantity in range(0, (count)):
			self.lights.append(new_light)
		print self.room_type, count, new_light.source
		return self

	def addCreepies(self, new_creepy, count):
		# add instances of creepy-crawlies to a room
		for quantity in range(0, (count)):
			self.creepy_crawlies.append(new_creepy)
		print self.room_type, count, new_creepy.kind
		return self

	def ghostBusters(self):
		# delete all objects from room
		self.spooks = []
		self.lights = []
		self.creepy_crawlies = []
		print self.room_type, "spooks = ",self.spooks, "creepy-crawlies =", self.creepy_crawlies, "lights =", self.lights
		return self

# Instances
hhouse1 = HauntedHouse("Strange Stuff")

room1 = Room("basement")
room2 = Room("attic")
room3 = Room("kitchen")
room4 = Room("dining room")
room5 = Room("living room")
room6 = Room("study")
room7 = Room("parlour")
room8 = Room("conservatory")
room9 = Room("master bedroom")
room10 = Room("guest bedroom")

spook1 = Spook("ghost", "ooooooOOOO OW! You walked through my face!", "dust bunny", None, "use selective invisibility")
spook2 = Spook("witch", "cackle cackle... Come try this apple, Dearie!", "cat", ("cauldron", "broom"), ("cast spells", "fly on broomstick"))
spook3 = Spook("vampire", "moan...Don't wake me up until it's midnight, and I've had my 'coffee!'", "bat", "coffin", "live for hundreds of years")
spook4 = Spook("skeleton", "rattle...rattle...clickety-clack... I think I lost a patella!", None, None, " do nothing, really" )
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

# Test prints/function calls
hhouse1.addRoom(room1).addRoom(room2).addRoom(room5).addRoom(room7).addRoom(room10)

room1.addLight(light6, 1).addLight(light1, 4).addCreepies(creepy6, 2).addCreepies(creepy1, 4).addSpook(spook3, 1)
room7.addLight(light2, 3).addLight(light4, 1).addLight(light5, 1).addCreepies(creepy4, 1).addSpook(spook6, 1).addSpook(spook1, 1)
room5.addLight(light3, 2).addLight(light4, 1).addCreepies(creepy2, 5).addCreepies(creepy5, 2).addSpook(spook5, 2).addSpook(spook4, 2)
room2.addLight(light6, 1).addCreepies(creepy1, 10).addSpook(spook2, 1).addSpook(spook1, 2).addSpook(spook6, 3)
room10.addLight(light4, 1).addCreepies(creepy2, 20).addSpook(spook4, 1)

# hhouse1.knock_knock("parlour")
# hhouse1.knock_knock("basement")
# hhouse1.knock_knock("living room")
# hhouse1.knock_knock("attic")
# hhouse1.knock_knock("guest bedroom")
# hhouse1.illuminate("parlour")
hhouse1.illuminate("attic")

# room7.ghostBusters()


		