# Patrouilles aux entrées du village.
# Construisez un "fire-trap" (piège explosif) quand vous voyez un ogre.
# Ne faites exploser aucun paysan!

loop:
    self.moveXY(43, 50)
    topEnemy = self.findNearestEnemy()
    if topEnemy:
        self.buildXY('fire-trap', 43, 50)
        
    self.moveXY(25, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.buildXY("fire-trap", 25, 34)
    self.moveXY(43, 20)
    downEnemy = self.findNearestEnemy()
    if downEnemy:
        self.buildXY("fire-trap", 43, 20)
    
