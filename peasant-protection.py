loop:
    enemy = self.findNearestEnemy()
    distance = self.distanceTo(enemy.pos)
    if distance < 10:
        # Attack if they get too close to the peasant.
        self.attack(enemy)
        self.attack(enemy)
    # Else, stay close to the peasant! Use else.
    else:
        self.moveXY(40, 37)