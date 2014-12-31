# Only attack enemies of type "munchkin" and "thrower".
# Don't attack a "burl". Run away from an "ogre"!
loop:
    enemy = self.findNearestEnemy()
    if enemy.type is "burl":
        self.say("I'm not attacking that Burl!")
    if enemy.type is "munchkin":
        self.attack(enemy)
    if enemy.type is "thrower":
        self.attack(enemy)
    if enemy.type is "ogre":
        self.moveXY(41, 47)